from socket import *
from time import ctime

HOST = "localhost"
PORT = 21001
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input(">")
    if not data:
        break
    udpSock.sendto(data.encode("utf-8"), ADDR)

    data, ADDR = udpSock.recvfrom(BUFSIZE)
    print(data.decode("utf-8"))

udpSock.close()
