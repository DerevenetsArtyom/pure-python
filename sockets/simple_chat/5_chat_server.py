import sys
import socket
import select

SOCKET_LIST = []
RECV_BUFFER = 4096  # 4 Kb
PORT = 9009


def chat_server():
    """
    In the code, we're dealing with two cases:

    * If master socket is readable, the server would accept the new connection.
    * If any of client socket is readable, the server would read the message,
    and broadcast it back to all clients except the one who send the message.
    """
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', PORT))
    server_socket.listen(10)

    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)

    print("Chat server started on port " + str(PORT))

    while True:
        # get the list sockets which are ready to be read
        # through select 4th arg time_out  = 0 : poll and never block

        # !! the select() itself is a blocking call (waiting for I/O completion)

        # The select() function monitors all client sockets
        # and server socket for readable activity.
        # If any of the client socket is readable then it means that
        # one of the chat client has send a message.
        ready_to_read, ready_to_write, in_error = select.select(
            SOCKET_LIST,  # potential_readers that we might want to try reading
            [],           # potential_writers we might want to try writing to
            [],           # potential_errs those that we want check for errors
            0             # timeout
        )

        for sock in ready_to_read:
            # a new connection request received
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print("Client (%s, %s) connected" % (sockfd, addr))
                broadcast(
                    server_socket, sockfd,
                    "[%s:%s] entered our chatting room\n" % (sockfd, addr)
                )

            # a message from a client, not a new connection
            else:
                # process data received from client
                try:
                    # receiving data from the socket
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # there is something in the socket
                        broadcast(
                            server_socket, sock,
                            '\r [ {} ] {}.'.format(sock.getpeername(), data)
                        )
                    else:
                        # remove the socket that's broken
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)
                        # at this stage,
                        # no data means probably the connection has been broken
                        broadcast(
                            server_socket, sock,
                            "Client (%s, %s) is offline\n" % addr
                        )  # TODO fix formatting
                except:
                    broadcast(
                        server_socket, sock,
                        "Client (%s, %s) is offline\n" % addr
                    )  # TODO fix formatting
                    continue
    server_socket.close()


# broadcast chat messages to all connected clients
def broadcast(server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)


if __name__ == "__main__":
    sys.exit(chat_server())
