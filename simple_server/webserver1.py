import socket

HOST, PORT = '', 8888

listen_socket = socket.socket()
listen_socket.bind((HOST, PORT))
listen_socket.listen(3)

print('Serving HTTP on port' + str(PORT))

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print('request:', request)
    http_response = """\
    HTTP/1.1 200 OK

    Hello, World!
    """

    client_connection.sendall(http_response)
    client_connection.close()
