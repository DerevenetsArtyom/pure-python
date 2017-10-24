import time


def timetest(input_func):

    def timed(*args, **kwargs):
        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print("Method Name - {0}, Args - {1}, Kwargs - {2}, Execution Time - {3}".format(
            input_func.__name__, args, kwargs, end_time - start_time)
        )
        return result

    return timed


@timetest
def foobart(*args, **kwargs):
    time.sleep(0.3)
    print('inside foobart')
    print(args, kwargs)


foobart('hello', 'world')
