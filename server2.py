import socket        #BT20CSE041 DEEPESH GAWALI
import threading
import re

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())   # we are working both codes on same system from different ide/ cmd so they are same in both client and serve r.py
ADDR = (SERVER, PORT)     #bind requires a tuple of address with port number
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"   #used to disconnect an established socket connection

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     ## socket. AF_NET BELONGS to the ipv4 family if we want to use ipv6 then WE WOULD USE socket.af_inet6
server.bind(ADDR)

def calculate(str):
    try:
        result =eval(str)
        return result
    except:
        return "INVALID EXPRESSION , TRY AGAIN"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                output=calculate(msg)
                print(f"[{addr}] {msg}")
                conn.send(str(output).encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")      # we do minus 1 here because the server itself is a thread rest are clients 


print("[STARTING] server is starting...")
start()