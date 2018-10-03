from socket import *
serverName = 'localhost'
serverPort = 12009
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
	clientSocket.connect((serverName,serverPort))
	sentence = input('$ ')
	clientSocket.send(sentence.split('$ ')[0].encode('utf-8'))
	modifiedSentence = clientSocket.recv(1024)
	print (modifiedSentence)
	clientSocket.close()
	
except:
	print("Error connecting to specified server")

	

