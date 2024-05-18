import socket

client= socket.socket()

client.connect(('172.20.10.3', int(3000)))

client.close()