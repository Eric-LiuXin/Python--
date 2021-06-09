from socket import *
from time import ctime

HOST = "localhost"
PORT = 21000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.bind(ADDR)
tcpSock.listen(1)

while True:
    tcpCliSock, addr = tcpSock.accept()
    while True:
        data = tcpCliSock.recv(BUFSIZE).decode("utf-8")
        if not data:
            break

        send_str = '[%s] %s' % (ctime(), data)
        tcpCliSock.send(send_str.encode("utf-8"))

    tcpCliSock.close()

tcpSock.close()

