#http://code.google.com/p/psutil/wiki/Documentation#Classes




def get_threadname(HWND):

	import psutil 
	from win32process import GetWindowThreadProcessId
	
	pprocess = GetWindowThreadProcessId(HWND)
	
	try:
		p = psutil.Process(pprocess[1])
	except:
		p = []
	
	return p
