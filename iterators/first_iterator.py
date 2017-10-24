class MyIterator:

    def __init__(self, letters):
        self.letters = letters
        self.position = 0

    def __iter__(self):
        """
        Returns itself as an iterator
        """
        return self

    def __next__(self):
        """
        Returns the next letter in the sequence or
        raises StopIteration
        """
        if self.position >= len(self.letters):
            raise StopIteration
        letter = self.letters[self.position]
        self.position += 1
        return letter


iterator = MyIterator('qwerty')
for let in iterator:
    print(let)
