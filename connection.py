import subprocess

class Connection:
	def checkC(self):
		return subprocess.call("ping -c1 google.com && echo \"*****INTERNET ONLINE*****\" || echo \"*****INTERNET OFFLINE*****\"", shell=True)
