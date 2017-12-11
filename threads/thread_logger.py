from threading import Thread
import logging


def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("threading.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


def doubler(n, logger):
    logger.debug('doubler function executing')
    result = n * 2
    logger.debug('doubler function ended with: {}'.format(result))


if __name__ == '__main__':
    logger = get_logger()
    thr_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']

    for i in range(5):
        my_thread = Thread(target=doubler, name=thr_names[i], args=(i, logger))
        my_thread.start()
