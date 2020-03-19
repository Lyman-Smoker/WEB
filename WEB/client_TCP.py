from socket import *

serverName='192.168.101.172'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input('Input lowercase sentence:')
clientSocket.send(sentence.encode('utf-8'))
modifiedSetence=clientSocket.recv(1024)
print('From Server:',modifiedSetence.decode('utf-8'))
clientSocket.close()