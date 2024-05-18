import socket

client= socket.socket()

client.connect(('192.168.210.163', int(3000)))

data = client.recv(1024)
print('code:', data)
print('message:', data.decode())

client.close()