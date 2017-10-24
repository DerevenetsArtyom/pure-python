import time
import socket


def send_answer(conn, status="200 OK", typ="text/plain; charset=utf-8",
                data=""):
    data = data.encode("utf-8")
    conn.send(b"HTTP/1.1 " + status.encode("utf-8") + b"\r\n")
    conn.send(b"Server: simplehttp\r\n")
    conn.send(b"Connection: close\r\n")
    conn.send(b"Content-Type: " + typ.encode("utf-8") + b"\r\n")
    conn.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
    conn.send(b"\r\n")  # после пустой строки в HTTP начинаются данные
    conn.send(data)


def parse(conn, addr):  # обработка соединения в отдельной функции
    data = b""

    while not b"\r\n" in data:  # ждём первую строку
        tmp = conn.recv(1024)
        if not tmp:  # сокет закрыли, пустой объект
            break
        else:
            data += tmp

    if not data:  # данные не пришли
        return  # не обрабатываем

    udata = data.decode("utf-8")

    # берём только первую строку
    udata = udata.split("\r\n", 1)[0]
    # разбиваем по пробелам нашу строку
    method, address, protocol = udata.split(" ", 2)

    if method != "GET" or address != "/time.html":
        send_answer(conn, "404 Not Found", data="Не найдено")
        return

    answer = """<!DOCTYPE html>"""
    answer += """<html><head><title>Время</title></head><body><h1>"""
    answer += time.strftime("%H:%M:%S %d.%m.%Y")
    answer += """</h1></body></html>"""

    send_answer(conn, typ="text/html; charset=utf-8", data=answer)


sock = socket.socket()
sock.bind(("", 8080))
sock.listen(5)

try:
    while 1:  # работаем постоянно
        conn, addr = sock.accept()
        print("New connection from " + addr[0])
        try:
            parse(conn, addr)
        except:
            send_answer(conn, "500 Internal Server Error", data="Ошибка")
        finally:
            # так при любой ошибке
            # сокет закроем корректно
            conn.close()
finally:
    sock.close()
# так при возникновении любой ошибки сокет
# всегда закроется корректно и будет всё хорошо
