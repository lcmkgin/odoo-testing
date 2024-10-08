import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 1460))

while True:
    message, address = server_socket.recvfrom(1024)
    message = message.upper()
    server_socket.sendto(message, address)