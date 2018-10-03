import subprocess
from finder import find
class PhysicalMemory:
	def getTotalMemory(self):
		return find('MemTotal', subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n'))

	def getFreeMemory(self):
		return find('MemFree', subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n'))
		
	def getAvailableMemory(self):
		return find('MemAvailable', subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n'))
