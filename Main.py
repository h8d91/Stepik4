import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(1024)
        if data:
            if data.endswith(b"\r\n\r\n"):
                resp = b"HTTP/1.1 200 OK\r\n"
                resp += b"Content-Type: text/html; charset=utf-8\r\n"
                resp += b"Connection: close\r\n"
                resp += b"\r\n"
                resp += b"<html><head><title>Hi</title></head><body><h1>Hello</h1></body></html>\r\n"
                self.send(resp)
                self.close()
           
                #self.close()

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print("Incoming connection from %s" % repr(addr))
            handler = EchoHandler(sock)

server = EchoServer('0.0.0.0', 2222)
asyncore.loop()