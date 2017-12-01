from socket import *

def clientSocket():
	HOST = 'localhost'
	PORT = 8002
	BUFSIZ = 1024
	ADDR = (HOST, PORT)

	tcpCliSock = socket(AF_INET, SOCK_STREAM)

	tcpCliSock.connect(ADDR)

	while True:
		data = input(r'>')
		if not data:
			break
		# 发送给服务器端的数据
		tcpCliSock.send(data.encode('utf-8'))
		# 接收服务器端数据
		recvData = tcpCliSock.recv(BUFSIZ)
		if not recvData:
			break
		print(recvData)

	tcpCliSock.close()

def main():
	clientSocket()

if __name__ == '__main__':
	main()