import socket

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#CREATE A CLIENT SOCKET AND CONNECT TO THE SERVER

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP,DEST_PORT))

#send/receive the messsage 
while True:
    #receive message fro server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    #Quit if the connected server wants to quit, else keep sending message
     
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\n Ending the chat... goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("message: ")
        client_socket.send(message.encode(ENCODER))

#CLOSE THE CLIENT SOCKET
client_socket.close()




