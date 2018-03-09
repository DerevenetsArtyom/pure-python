class HashTable:
    def __init__(self):
        self.size = 79  # Static for now, better to be a prime number
        self.slots = [None] * self.size  # Contains list of keys
        self.data = [None] * self.size  # Contains list of values

    @property
    def len_slots(self):
        return len(self.slots)

    def hash_function(self, key, size=None):
        """Simple implementation using modulo"""
        if size is None:
            # hack to have an opportunity to use property
            size = self.len_slots
        return key % size

    def rehash(self, old_hash, size=None):
        if size is None:
            # hack to have an opportunity to use property
            size = self.len_slots
        return (old_hash + 1) % size

    def put(self, key, data):
        # return some number 0 < n < len(slots)
        hash_value = self.hash_function(key)

        # free slot for current hash_value
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        # replace data for current hash_value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data

            else:
                next_slot = self.rehash(key)
                # condition = (self.slots[next_slot] is not None
                #              and self.slots[next_slot] != key)

                while (self.slots[next_slot] is not None
                             and self.slots[next_slot] != key):
                    print('condition')
                    next_slot = self.rehash(key)
                    print('next_slot', next_slot)
                    print('end condition')

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data

                elif self.slots[next_slot] == key:
                    self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash_function(key)

        data = None
        stop = found = False
        position = start_slot

        while self.slots[position] is not None and not(found and stop):
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(key)
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key, value)
