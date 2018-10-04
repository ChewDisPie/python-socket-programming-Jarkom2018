from socket import *
import threading
from hardware import Hardware
from storage import Storage
from physicalMemory import PhysicalMemory
from swap import Swap
from datetime import datetime
import subprocess

#initialize objects
h = Hardware()
m = PhysicalMemory()
s = Swap()
st = Storage()
logAccess = {}

def analyze(byteMessage):
	message = byteMessage.decode('utf-8')
	if 'hard' in message:
		return analyzeHardware(message).encode('utf-8')
	elif 'mem' in message:
		return analyzePhysicalMemory(message).encode('utf-8')
	elif 'swap' in message:
		return analyzeSwap(message).encode('utf-8')
	elif 'stor' in message:
		return analyzeStorage(message)
	elif 'netstat' in message:
		return checkConnection()
	elif 'log' in message:
		return log().encode('utf-8')
	else: 
		unspecified = 'unspecified request'
		return unspecified.encode('utf-8')

def analyzeHardware(message):
	if message == 'hardware --arch':
		return h.getArchitecture()
	elif message == 'hardware --mod':
		return h.getModelName()
	elif message == 'hardware --cache':
		return h.getCache()
	elif message == 'hardware':
		return h.getArchitecture() + '\n' + h.getModelName() + '\n' + h.getCache()
	else:
		unspecified = 'unspecified request'
		return unspecified.encode('utf-8')

def analyzePhysicalMemory(message):
	if message == 'mem --total':
		return m.getTotalMemory()
	elif message == 'mem --free':
		return m.getFreeMemory()
	elif message == 'mem --avail':
		return m.getAvailableMemory()
	elif message == 'mem':
		return m.getTotalMemory() + '\n' + m.getFreeMemory() + '\n' + m.getAvailableMemory()
	else: 
		unspecified = 'unspecified request'
		return unspecified.encode('utf-8')

def analyzeSwap(message):
	if message == 'swap --total':
		return s.getTotalSwap()
	elif message == 'swap --free':
		return s.getFreeSwap()
	elif message == 'swap --avail':
		return s.getAvailableSwap()
	elif message == 'swap':
		return s.getTotalSwap() + '\n' + s.getFreeSwap() + '\n' + s.getAvailableSwap()
	else: 
		unspecified = 'unspecified request'
		return unspecified.encode('utf-8')

def analyzeStorage(message):
	if message == 'stor --total':
		return st.getTotalStorage()
	elif message == 'stor --avail':
		return st.getAvailableStorage()
	elif message == 'stor --used':
		return st.getUsedStorage()
	elif message == 'stor':
		return st.getAll()
	else: 
		unspecified = 'unspecified request'
		return unspecified.encode('utf-8')


def checkConnection():
	return subprocess.check_output("ping -c1 google.com && echo \"*****INTERNET ONLINE*****\" || echo \"*****INTERNET OFFLINE*****\"", shell=True)

def log():
	return str(logAccess)

def usage():
	return('USAGE:\n\n\
	hardware -> return hardware usage info\n\
	--arch        architecture of the hardware\n\
	--mod         model info like Intel or AMD with core and clock\n\
	--cache       cache info of the computer')


serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
print('The server is ready to receive')
serverSocket.listen(1)
lock = threading.Lock()

def handleClient(socketConnection, address, timeOfConnect):
	while 1:
		sentence = connectionSocket.recv(1024)
		if sentence.decode('utf-8') == 'close':
			lock.acquire()
			logAccess['START: '+ str(timeOfConnect)]='END: '+ str(datetime.now())
			lock.release()
			connectionSocket.close()
			break
		else:
			response = analyze(sentence)
			connectionSocket.send(response)



try:
	while 1:
		connectionSocket, addr = serverSocket.accept()
		lock.acquire()
		logAccess['START: '+ str(datetime.now())] = ''
		lock.release()
		threading.Thread(target = handleClient,args = (connectionSocket,addr, datetime.now())).start()

except Exception as e:
	print(e)
	connectionSocket.close()