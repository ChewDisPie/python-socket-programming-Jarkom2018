from socket import *
from hardware import Hardware

#initialize objects
h = Hardware()

def analyze(message):
	if message.decode('utf-8') == 'hardware --arch':
		return h.getArchitecture()

	elif message.decode('utf-8') == 'hardware --mod':
		return h.getModelName()
	elif message.decode('utf-8') == 'hardware --cache':
		return h.getCache()
	else: 
		return 'unspecified request'


serverPort = 12009
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	response = analyze(sentence).encode('utf-8')
	connectionSocket.send(response)
	connectionSocket.close()
	

