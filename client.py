import socket

#Create a server side socket using ipv4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the socket to a server located at a given IP and Port

client_socket.connect((socket.gethostbyname(socket.gethostname()),12345))

#reeceive a message from the serveer .. You must specify the number of bytes to receive

message = client_socket.recv(1024)
print(message.decode("utf-8"))
print(type(message))

#close the client scket
client_socket.close()

