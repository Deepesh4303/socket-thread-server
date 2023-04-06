import socket        #BT20CSE041 DEEPESH GAWALI
import threading



# import argparse

# # Create an argument parser
# parser = argparse.ArgumentParser(description='My server program')

# # Add arguments to the parser
# parser.add_argument('-p', '--port', type=int, default=5555, help='Port number to use')

# # Parse the command-line arguments
# args = parser.parse_args()

# # Use the parsed arguments in your code
# port = args.port

# # Now you can use the `port` variable in your code to specify the port number to listen on
#for testing argumentless code is easier



is_handling_client= False
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

    global is_handling_client
    

    if is_handling_client:
        wait_message = "The server is currently handling another client. Please wait..."
        conn.send(wait_message.encode())
        return
    else:
        is_handling_client= True
    

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
        is_handling_client = False
   # conn.send("done".encode())
    conn.close()
    
    
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    is_handling_client = False
    while True:
        conn, addr = server.accept()
        handle_client(conn,addr)
    #     thread = threading.Thread(target=handle_client, args=(conn, addr))
    #     thread.start()
    #     print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")      # we do minus 1 here because the server itself is a thread rest are clients 


print("[STARTING] server is starting...")
start()



#unless you exit from one client other output wont show as global flag is_handling  is set alternatively