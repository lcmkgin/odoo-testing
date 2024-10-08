import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 1460))

while True:
    message, address = server_socket.recvfrom(1024)
    print(message)
    message.decode("utf-8")
    data = json.loads(message)
    print (data["op"])
    server_socket.sendto(message, address)