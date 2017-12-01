from socket import *

from time import ctime

def serverSocket():
	HOST = ''
	PORT = 8002
	BUFSIZ = 1024
	ADDR = (HOST, PORT)

	# 创建套接字对象
	tcpSerSock = socket(AF_INET, SOCK_STREAM)
	# 绑定地址
	tcpSerSock.bind(ADDR)
	# 监听，5个连接
	tcpSerSock.listen(5)

	while True:
		print('waiting for connection....')
		# 获取连接对象
		tcpSerSock, addr = tcpSerSock.accept()
		print('...connection from :', addr)

		while True:
			# 接收从客户端来的数据
			recvData = tcpSerSock.recv(BUFSIZ)
			if not recvData:
				break
			# 发送数据给客户端
			tcpSerSock.send(('[%s] %s' %(ctime(), recvData)).encode('utf-8'))

		tcpSerSock.close()

	tcpSerSock.close()

def main():
	serverSocket()

if __name__ == '__main__':
	main()