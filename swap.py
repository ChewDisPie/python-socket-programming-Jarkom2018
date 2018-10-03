import subprocess
from finder import find
class Swap:
	def getTotalSwap(self):
		return find('SwapTotal', subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n'))

	def getFreeSwap(self):
		return find('SwapFree', subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n'))
	
	def getAvailableSwap(self):
		result = find('SwapAvailable', subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8').split('\n'))
		if not result == '':
			return result
		else:
			return 'SwapAvailable:         0 kB'
