import asyncore,socket, sys, time

TCP_IP ='127.0.0.1'
PORT = 5000
MESSAGE = "ping"
BUFFER_SIZE =1024


def client():
    cnt =0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, PORT))
    #global MESSAGE
    msg = sys.argv[1] + ":" + MESSAGE
    while True:
        sock.send(msg.encode())
        recv_data = sock.recv(BUFFER_SIZE)
        cnt += 1
        print("Sending Data:", MESSAGE)
        print("Received Data:", recv_data.decode())
        time.sleep(int(sys.argv[2]))
        if (cnt >= int(sys.argv[3])):    
            sock.close()
            print('Connection Closed')
            break

client()