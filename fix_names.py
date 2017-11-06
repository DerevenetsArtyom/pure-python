import datetime
import os
import time

TARGET = '/media/derevenets/Media/Документы/Мои документы/Мои видео_аудио/Диктофон2'
os.chdir(TARGET)

FIRST = 'Гитара(фикс)'
SECOND = 'Какие-то записи гитары(фикс)'
LAST = 'нормально переименовать(фикс)'

# print(os.getcwd())

# for root, dir, file in os.walk(TARGET):
#     print(dir, file)

# for current in (FIRST, SECOND, LAST):
for current in (FIRST, ):
    os.chdir(
        os.path.join(TARGET, current)
    )
    print(os.getcwd())
    for i in os.listdir():
        date, name = i.split(maxsplit=1)
        day, mth, year = date.split('.')
        new_date = '.'.join([year, mth, day])
        new_name = '{} {}'.format(new_date, name)
        print(new_name)
        os.rename(i, new_name)

    # t = os.path.getmtime(i)
    # dt = datetime.datetime.fromtimestamp(t)
    # os.rename(i, dt.strftime('%Y.%m.%d %X'))
