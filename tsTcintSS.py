from socket import *

HOST = "localhost"
PORT = 21000
BUFSIZE = 1024
ADDR = (HOST, PORT)



while True:
    tcpSock = socket(AF_INET, SOCK_STREAM)
    tcpSock.connect(ADDR)
    data = input("> ")

    if not data:
        break
    send_str = "%s\r\n"%(data)
    tcpSock.send(send_str.encode("utf-8"))

    data = tcpSock.recv(BUFSIZE)
    if not data:
        break

    print(data.decode("utf-8").strip())

    tcpSock.close()