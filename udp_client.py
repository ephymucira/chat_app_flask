import socket

#create a socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some info through the udp prtocol

client_socket.sendto("Hello server world!!!".encode("utf-8"),(socket.gethostbyname(socket.gethostname()), 12345))
