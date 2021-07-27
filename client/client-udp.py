#!python
import time

import socket

UDP_IP = "server"
UDP_PORT = 5005

if __name__ == "__main__":
    
    print(f"meu IP: {socket.gethostbyname(socket.gethostname())}")

    print("criando sock")
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP

    msg = 0
    msg_bytes = ""

    print("iniciando loop")
    for _ in range(10):
        print("mandando msg")
        msg_bytes = f"{msg}".encode()
        print(f"mandando msg {msg_bytes} para {socket.gethostbyname(UDP_IP)}")
        sock.sendto(msg_bytes, (socket.gethostbyname(UDP_IP), UDP_PORT))

        msg += 1
        if msg >= 4:
            msg = msg % 4
        
        time.sleep(0.5)