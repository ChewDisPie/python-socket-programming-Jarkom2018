import subprocess

class Storage:
    def getTotalStorage(self):
        return subprocess.check_output(['df', '-h', '--output=source,size'])

    def getAvailableStorage(self):
        return subprocess.check_output(['df','-h','--output=source,avail'])

    def getUsedStorage(self):
        return subprocess.check_output(['df','-h','--output=source,used'])
    
    def getAll(self):
        return subprocess.check_output(['df','-h','--output=source,size,avail,used']) 
