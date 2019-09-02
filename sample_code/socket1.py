import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('http://data.pr4e.org/', 80))
print('conn succ')


cmd = 'GET http://data.pr4e.org/authors.txt HTTP/1.2\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
