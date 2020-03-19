from socket import *


serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('192.168.101.172', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024)
    capotalizedSentence=sentence.upper()
    connectionSocket.send(capotalizedSentence)
    connectionSocket.close()
