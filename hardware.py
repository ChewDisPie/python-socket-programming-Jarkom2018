import subprocess

class Hardware(object):
	def getArchitecture(self):
		return subprocess.check_output(['lscpu']).decode('utf-8').split('\n')[0]

	def getModelName(self):
		return subprocess.check_output(['lscpu']).decode('utf-8').split('\n')[12]

	def getCache(self):
		return subprocess.check_output(['lscpu']).decode('utf-8').split('Virtualization type: full\n')[1].split('NUMA node0 CPU(s):   0-3')[0]

		
