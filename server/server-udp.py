#!python
import time

import socket

UDP_IP = socket.gethostbyname(socket.gethostname())
UDP_PORT = 5005
BUFFER = "0"
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    #print("Hello world!")

    print("criando sock")
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((socket.gethostbyname("server"), UDP_PORT))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    print("inicio loop")
    for i in range(10):
        
        print("esperando msg do core")
        pre_buffer = sock.recvfrom(1024)[0].decode()

        print(f"pre_buffer: {pre_buffer}")

        BUFFER = int(pre_buffer) # 2 bits

        print(f"recebeu {BUFFER}!")

        time.sleep(.5)