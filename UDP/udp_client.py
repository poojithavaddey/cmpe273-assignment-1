import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping"
m="C"

def send(id,data):
    try:
        msg = str(id) + data 
        s.sendto(msg.encode(), (UDP_IP, UDP_PORT))
        try:
            data, ip = s.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            print ("timed out!, sending again")
            send(id,data)

        else:
            print("Received Ack {} from server".format(data.decode()))
            return data
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()

def readFile():
    try:
        fopen =open("upload.txt",'r')
        lines=fopen.readlines()
        print("Starting a file (upload.txt) upload...")
        for l,line in enumerate(lines):
            MESSAGE =line
            send(l,MESSAGE)
        print("File upload successfully completed!")
        s.sendto(m.encode(),(UDP_IP, UDP_PORT))
    except Exception as e:
        print("idk why",e)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Connected to the server")
s.settimeout(2)
readFile()
