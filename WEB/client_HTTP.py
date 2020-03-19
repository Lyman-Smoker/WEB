from socket import *

serverName='192.168.101.172'
serverPort=12000

# 创建套接字
clientSocket=socket(AF_INET,SOCK_STREAM)

# 连接服务器
clientSocket.connect((serverName,serverPort))

# 请求行
request_line = 'GET / HTTP/1.1\r\n'

#首部行
headers = "Host:192.168.101.172\r\n"

#报文实体
body = "This is the body\r\n "

#报文数据
data=request_line + headers + '\r\n' +body

#发送报文
clientSocket.send(data.encode('utf-8'))

#接收并解析报文
modifiedSetence=clientSocket.recv(1024)
result=modifiedSetence.decode('utf-8')

# reslult = result.split('\r\n\r\n')[1]
print(result)

#关闭套接字
clientSocket.close()