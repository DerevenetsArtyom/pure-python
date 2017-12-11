""" A more realistic thread pool example """

import time
import threading
import queue as Queue
from urllib import request

# Работает отлично, но посмотрите на весь этот код!
# Здесь методы инициализации, списки потоков для отслеживания работы,
# и что хуже всего, если вы склонны к обработке блокировок как и я,
# куча вызовов метода join. А впоследствии будет еще сложнее!

# А что было сделано? Да практически ничего.
# Вышеприведенный код представляет собой хрупкую конструкцию.
# Это внимательное следование шаблону, это высокая вероятность ошибок
# и это писать много кода и получать мало функционала.
# К счастью, есть гораздо лучший способ.


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            content = self._queue.get()
            if isinstance(content, str) and content == 'quit':
                break
            response = request.urlopen(content)
            print(response)
        print('Bye byes!')


def Producer():
    urls = [
        'http://www.python.org',
        'http://www.yahoo.com',
        'http://www.scala.org',
        'http://www.google.com',
    ]
    queue = Queue.Queue()
    worker_threads = build_worker_pool(queue, 4)
    start_time = time.time()

    # Add the urls to process
    for url in urls:
        queue.put(url)
    for worker in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()

    print('Done! Time taken: {}'.format(time.time() - start_time))


def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        worker.start()
        workers.append(worker)
    return workers

if __name__ == '__main__':
    Producer()
