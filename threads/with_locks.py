import threading


total = 0
lock = threading.Lock()


def update_total(amount):
    global total

    # VERSION 1: lock and unlock manually
    # lock.acquire()  # lock before we finish
    # try:
    #     total += amount
    # finally:
    #     lock.release()

    # VERSION 2: lock and unlock with context manager
    with lock:
        total += amount

    print(total)


if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(target=update_total, args=(5,))
        my_thread.start()
