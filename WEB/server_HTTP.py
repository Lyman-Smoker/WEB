from socket import *
import datetime

serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('192.168.101.172', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024)

    #响应报文
    #状态行
    status_line='HTTP/1.1 200 OK\r\n'

    #首部行
    #连接状态
    connection='Connection: close\r\n'
    #当前相应时间
    date='Date: '+str(datetime.datetime.now())+'\r\n'
    #形式：
    type='Content-Type: text/html\r\n'

    # 数据
    data="Hello , welcome to " + '192.168.101.172\r\n'

    #相应报文
    massage=status_line + connection + date + type + '\r\n' + data
    connectionSocket.send(massage.encode('utf-8'))
    connectionSocket.close()
