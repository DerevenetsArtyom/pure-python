import asyncio
import os
import urllib.request


async def download_coroutine(url):
    """Сопрограмма для загрузки данных по указанному url"""
    request = urllib.request.urlopen(url)
    filename = os.path.basename(url)

    with open(filename, 'wb') as file_handle:
        while True:
            chuck = request.read(1024)
            if not chuck:
                break
            file_handle.write(chuck)
    msg = 'Завершена загрузка {filename}'.format(filename=filename)
    return msg


async def main(urls):
    """Создет группу сопрограмм и ожидает их завершения"""
    coroutines = [download_coroutine(url) for url in urls]

    # чтобы отследить момент, когда все сопрограммы завешат свою работу,
    # мы используем функцию wait
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())


if __name__ == '__main__':
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(urls))
    finally:
        event_loop.close()
