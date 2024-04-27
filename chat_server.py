#chat server side

import socket

#Define constants to be used

HOST_IP =socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#CREATE A SERVER SOCKET, BIND IT TO A IP/PORT , AND LISTEN
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST_IP,HOST_PORT))
server_socket.listen()

#accept any incoming connection and let them know
print("Server is running..\n")
client_socket, client_address = server_socket.accept()
client_socket.send("You are connected to the server ..\n".encode(ENCODER))

#send/rceive messages

while True:
    #Receive info from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    #   Quit if the client socket wants to quit , ese dispaly the message

    if message == "quit":
        client_socket.send("Quit".encode(ENCODER))
        print("\n End the chat...goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("message:")
        client_socket.send(message.encode(ENCODER))

#close the server 
server_socket.close()

