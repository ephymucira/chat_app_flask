#udp server side

import socket
# create a server side socket IPV4 (AF_INET) and UDP (SOCK_DGRAM)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind our new socket to a tuple (Ip address , port address)

server_socket.bind((socket.gethostbyname((socket.gethostname())),12345))

# we are not listening to any connection since it is a udp connection server

message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)