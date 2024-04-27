#TCP server side
import socket

#Create a server side socket using ipv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#see how to get ip address dynamically
# print(socket.gethostname())#hostname
# print(socket.gethostbyname(socket.gethostname()))#ip address of the given hostname

#bind our new socket to a tuple( IP address , Port Address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

#put the socket into listening mode to listen for any possible connections
server_socket.listen() 

#listen forever to accept any connection
while True:
    #Accept every single connection and store two pieces of information
    client_socket, client_address = server_socket.accept()
    # print(type(client_socket))
    # print(client_socket)
    # print(type(client_address))
    # print(client_address)

    print(f"connected to {client_address}!\n")

    #send a message to the client who just connected
    client_socket.send("You are connected!".encode("utf-8"))
   
   #close the server connection

    server_socket.close()

    break






