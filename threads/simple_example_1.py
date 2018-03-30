import time
from threading import Thread, current_thread


def sleeper(n):
    print(f'Hello, I"m a {current_thread().name}. Going to sleep')
    time.sleep(n)
    print(f'{current_thread().name} is awake')


# This example shows how function executes one after another (synchronously)
def one_by_one():
    start = time.time()
    for _ in range(5):
        sleeper(4)

    print('General time taken:', time.time() - start)


# This example shows how threads could execute in parallel
def in_parallel():
    threads_list = []

    start = time.time()

    for _ in range(5):
        t = Thread(target=sleeper, args=(4, ))
        threads_list.append(t)
        t.start()
        print(f'{t.name} was started')

    for t in threads_list:
        print(f'{t.name} is going to join')
        t.join()

    # Should be 4 sec, the same as argument of sleep
    print('General time taken:', time.time() - start)


if __name__ == '__main__':
    one_by_one()
    # in_parallel()
