from socket import *

HOST = "localhost"
PORT = 21000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.connect(ADDR)

while True:
    data = input("> ")
    if not data:
        break
    tcpSock.send(data.encode("utf-8"))
    res = tcpSock.recv(BUFSIZE).decode("utf-8")
    if not res:
        break
    print(res)
tcpSock.close()