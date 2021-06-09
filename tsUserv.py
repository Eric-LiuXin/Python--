from socket import *
from time import ctime

HOST = "localhost"
PORT = 21001
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSock = socket(AF_INET, SOCK_DGRAM)
udpSock.bind(ADDR)

while True:
    res, addr = udpSock.recvfrom(BUFSIZE)
    print(res.decode("utf-8"))
    send_str = '[%s] %s' % (ctime(), addr)
    udpSock.sendto(send_str.encode("utf-8"), addr)

udpSock.close()
