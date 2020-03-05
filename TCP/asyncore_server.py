import asyncore,socket

TCP_IP = '127.0.0.1'
PORT = 5000
MESSAGE ="pong"
no_of_conn= 0
counted_con = 0

class HandlerClass(asyncore.dispatcher_with_send):

    def handle_read(self):
        recv_data= self.recv(1024)
        global counted_con
        if recv_data:
            self.send(MESSAGE.encode())
            data = str(recv_data.decode())
            if(counted_con < no_of_conn):
                print("Connected Client:" ,data.split(":")[0])
                counted_con += 1
            print("Message from Client: ",recv_data.decode())


class Echo(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.bind((host, port))
        self.listen(5)
        print("Server started at port 5000.")

    def handle_accepted(self, sock, addr):
        global no_of_conn
        no_of_conn+=1
        handler = HandlerClass(sock)
        

server = Echo(TCP_IP,PORT)
asyncore.loop()