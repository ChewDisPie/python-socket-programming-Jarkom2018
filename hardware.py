import subprocess
from finder import find

class Hardware(object):
	def getArchitecture(self):
		return find('Architecture',  subprocess.check_output(['lscpu']).decode('utf-8').split('\n'))

	def getModelName(self):
		return find('Model name',subprocess.check_output(['lscpu']).decode('utf-8').split('\n'))

	def getCache(self):
		return subprocess.check_output(['lscpu']).decode('utf-8').split('Virtualization type: full\n')[1].split('NUMA node0 CPU(s):   0-3')[0]

		
