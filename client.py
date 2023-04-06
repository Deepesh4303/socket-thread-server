# import argparse

# # Create an argument parser
# parser = argparse.ArgumentParser(description='My server program')

# # Add arguments to the parser
# parser.add_argument('-p', '--port', type=int, default=5555, help='Port number to use')

# # Parse the command-line arguments
# args = parser.parse_args()

# # Use the parsed arguments in your code
# PORT = args.port

# # Now you can use the `port` variable in your code to specify the port number to listen on
#if you want to use command line version of the assignment just copy the  above code in server files and comment out PORT


import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = "192.168.0.108"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))     #we are padding our message to header size , rest are spaces first will be our string yyyyyy
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))    #we have used 2048 as header as it is large buffer , and certainly will contain our message 
    #print(client.recv().decode())

# send("Hello World!")
# input()
# send("Hello Everyone!")
# input()
# # send("Hellowormd")


flag=True
while(flag):
    control=input()
    send(control)
    if(control=="exit"):
        flag=False
        send(DISCONNECT_MESSAGE)