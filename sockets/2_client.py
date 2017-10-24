import socket

sock = socket.socket()

# позволяет соединиться с сервером
sock.connect(('localhost', 8007))

sock.send('hello socket'.encode('utf-8'))

data = sock.recv(1000000)
print('received', data, len(data), 'bytes')

sock.close()





