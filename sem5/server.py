import socket

server = socket.socket()

server.bind(('192.168.210.86', 3000))

server.listen(5)
print(server)

con, addr = server.accept()
message = 'за карш не скину'
data = message.encode()
con.send(data)
print('connection_con', con)
print('connection_addr', addr)

con.close()

server.close()