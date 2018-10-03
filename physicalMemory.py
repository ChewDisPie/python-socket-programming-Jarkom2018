import subprocess

class PhysicalMemory:
	def getTotalMemory(self):
		return subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n')[0]

	def getFreeMemory(self):
		return subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n')[1]
		
	def getAvailableMemory(self):
		return subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n')[2]
