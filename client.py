from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
	clientSocket.connect((serverName,serverPort))
	while 1:
		sentence = input('$ ')
		clientSocket.send(sentence.split('$ ')[0].encode('utf-8'))
		modifiedSentence = clientSocket.recv(1024).decode('utf-8')
		if not sentence.lower() == 'close':
			print (modifiedSentence)
		else:	
			clientSocket.close()		
			break
	
except:
	print("Error connecting to specified server")

finally:
	clientSocket.close()