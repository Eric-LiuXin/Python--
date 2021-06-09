from socketserver import (
    TCPServer as TCP,
    StreamRequestHandler as SRH,
)
from time import ctime


HOST = "localhost"
PORT = 21000
BUFSIZE = 1024
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print("。。。connect from: ", self.client_address)
        send_str = '[%s] %s'% (ctime(), self.rfile.readline().decode("utf-8"))
        self.wfile.write(send_str.encode("utf-8"))

tcpServ = TCP(ADDR, MyRequestHandler)
print("。。。wait for connection")
tcpServ.serve_forever()