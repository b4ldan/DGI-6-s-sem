import socket

server = socket.socket()

server.bind(('localhost', 3000))

server.listen(5)
print(server)

con, addr = server.accept()
print('connection_con', con)
print('connection_addr', addr)

con.close()

server.close()