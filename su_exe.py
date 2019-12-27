import subprocess
setupDir = 'E:\\timelogger'

def initSetup():
	import os
	pywin32Path = os.path.join(setupDir, 'pywin32-224-cp37-cp37m-win_amd64.whl')
	psutilPath = os.path.join(setupDir, 'psutil-5.6.3-cp37-cp37m-win_amd64.whl')
		
	try:
		from win32gui import GetWindowText, GetForegroundWindow
	except ImportError:
		#subprocess.call(['pip','install','pywin32'])
		subprocess.call(['pip','install', pywin32Path])
		#os.system('pip --retries 20 install pywin32')

	try:
		import win32api
	except ImportError:
		print  ('error')
		#subprocess.call(['pip','install','win32api'])
		#os.system('pip --retries 20 install win32api')

	try:
		import psutil
	except ImportError:
		subprocess.call(['pip','install', psutilPath])
		#subprocess.call(['pip','install','psutil'])
		#os.system('pip --retries 20 install psutil')

	try:
		import win32process
	except ImportError:
		print ('error')
		#subprocess.call(['pip','install','win32process'])
		#os.system('pip --retries 20 install win32process')

if __name__ == '__main__':
	initSetup()
