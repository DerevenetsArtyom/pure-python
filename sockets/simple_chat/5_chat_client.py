import sys
import socket
import select

# http://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php


def chat_client():
    """
    The client code does either listen to incoming messages from the server or
    check user input. If the user types in a message then send it to the server.

    We use select() function to handle both messages:
    one from stdin which is a user input and the other from the server.
    As we recall, the server side usage which is a non-blocking mode,
    we don't do anything on the select(), and we use it as blocking mode.

    So, the select() function blocks (waits) till something happens.
    It will return only when either the server socket
    receives a message or the user enters a message.
    """

    s = socket.socket()
    s.settimeout(2)

    # connect to remote host
    try:
        s.connect((sys.argv[1], int(sys.argv[2])))
    except:
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host. You can start sending messages')
    sys.stdout.write('[Me]: ')
    sys.stdout.flush()

    while True:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, \
            write_sockets, \
            error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                print('try to process incoming message from remote server')
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data:
                    print('\nDisconnected from chat server')
                    sys.exit()
                else:
                    # print data
                    print('data in socket is present!!!!')
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] ')
                    sys.stdout.flush()
            else:
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[Me]: ')
                sys.stdout.flush()


if __name__ == "__main__":
    sys.exit(chat_client())
