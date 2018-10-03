import subprocess

class Swap:
	def getTotalSwap(self):
		return subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n')[14]

	def getFreeSwap(self):
		return subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n')[15]
	
	def getAvailableSwap(self):
		result = subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n')[16]
		if not 'Dirty' in result:
			return result
		else:
			return 'SwapAvailable:         0 kB'
		
