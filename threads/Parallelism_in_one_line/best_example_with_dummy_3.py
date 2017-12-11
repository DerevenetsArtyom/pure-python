from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from urllib import request


# Make the Pool of workers
pool = ThreadPool(4)

# Последнее выражение делает то же, что и семистрочная функция build_worker_pool
# в приведенном ранее примере: создает кучу доступных воркеров,
# поготавливает их к выполнению задач, и сохраняет их в переменной,
# что бы к ним было легко обратиться.

# В общем случае, если вы используете многопроцессовый пулл
# для ядро-раздельных задач, то больше ядер означает большуую скорость
# (я говорю это с многочисленными оговорками).
# Однако, когда речь идет о многопоточной обработке и делах связанных с сетью,
# это не так, и будет хорошей идеей поэксперементировать с размером пула.


urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    ]

# Open the urls in their own threads and return the results
results = pool.map(request.urlopen, urls)

# close the pool and wait for the work to finish
pool.close()
pool.join()
