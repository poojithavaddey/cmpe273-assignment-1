import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print("Server started at port " +str(UDP_PORT))
    print("Accepting a file upload...")

    while True:
        data, id = s.recvfrom(BUFFER_SIZE)
        if data.decode(encoding="utf-8").strip()== 'C':
           print("Upload successfully completed!")
        #print("{}: {}".format(id, data.decode(encoding="utf-8").strip()))
        ack_num = data.decode(encoding="utf-8").strip().split(":")
        s.sendto(ack_num[0].encode(), id)
       

listen_forever()