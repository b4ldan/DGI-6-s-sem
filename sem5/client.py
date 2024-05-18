import socket

client= socket.socket()

client.connect(('192.168.210.163', int(3000)))

data = client.recv(1024)
print('code:', data)
print('message:', data.decode())

message = 'за карш не скину'
data = message.encode()
client.send(data)

while True:
    message = input('Input your message:')
    data = message.encode()
    client.send(data)
    data = client.recv(1024)
    print('code:', data)
    print('message:', data.decode())
    if message == 'Close!':
        break

client.close()