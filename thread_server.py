import socket, threading

#define constants to be used
HOST_IP =socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#create a server socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#create two blank lists to store connected clint sockets and their names

client_socket_list = []
client_name_list = []






