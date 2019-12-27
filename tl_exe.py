#encoding:UTF-8
#! python3

import uuid

from time import strftime, localtime, time
import idledetect
import threadname
import csvlogwrite as logwrite
import sys
import os

scriptMode = 'byjus'

if scriptMode == 'test':
	#baseDir = 'W:\\Projects\\Byjus\\TimeServer\\'
	baseDir = 'C:\\Projects\\Byjus\\TimeServer\\'
	idleThres = 5.0
elif scriptMode == 'byjus':
	baseDir = '\\\\192.168.150.33\\nexus\\timelogger\\logs\\'
	#baseDir = '\\\\192.168.150.6\\alt_temp\\logs\\'	
	idleThres = 60.0 #seconds
#baseDir = 'E:\\timelogger\\timelogger\\logs\\'

	
lastIdle = 0.0
Data = {}
idleSoFar = 0.0

#baseDir = os.path.dirname(__file__)
#LogFile = os.path.join(baseDir, 'logs\\' + strftime("%Y-%b-%d", localtime()))

def initData():

	global Data
	Data = {'User Name': '', 'Machine Name': '',
	'Start Time': 0.0, 'End Time': 0.0,
	'Total Duration': 0.0 , 'Total Idle': 0.0, 'Active Duration': 0.0,
	'App Name': '', 'App Title': '', 'App Details': '',
	'Category': '', 'Sub Category': ''}


def initApp():
	
	global Data
	import time

	initData()

	#Data               = {}
	# call SetFreshData() to get time and any other available data
	SetFreshData()
	LogFile = getLogFile()
	# write a session startup entry
	logwrite.Write(Data,LogFile)
	# most always set fresh data after logging
	SetFreshData()

	while(True):
		Log()
		time.sleep(0.25)
	
   
def getLogFile():

	import getpass

	user_name = getpass.getuser()
	
	y, mo, m, d = strftime("%Y-%b-%m-%d", localtime()).split('-')
	logDir = os.path.join(baseDir, y, mo, d)
	
	if not os.path.isdir(logDir):
		os.makedirs(logDir)

	csvName = user_name + '_' + d + m + y + '.csv'
	LogFile = os.path.join(logDir, csvName)
	Head = {}
	if not os.path.isfile(LogFile):
		

		Head['C1'] = 'User Name'
		Head['C2'] = 'Machine Name'
		Head['C3'] = 'Start Time'
		Head['C4'] = 'End Time'
		Head['C5'] = 'Total Duration'
		Head['C6'] = 'Idle'
		Head['C7'] = 'Active Duration'
		Head['C8'] = 'App Name'
		Head['C9'] = 'App Title'
		Head['C10'] = 'App Details'
		Head['C11'] = 'Category'
		Head['C12'] = 'Sub Category'


		logwrite.Write(Head, LogFile)

	#print (LogFile)
	return LogFile


#logic in this function keeps it from logging an entry every second.
#instead it keeps adding up the idle stime
#tracks when the app window first went active
#writes tracking data upon change to next window
def Log():

	global Data, lastIdle, idleSoFar
	from win32gui import GetWindowText, GetForegroundWindow

	#LogFile = os.path.join(baseDir, 'logs\\' + strftime("%Y-%b-%d", localtime()))
	

	idle = idledetect.get_idle_duration()

	
	if lastIdle <  idle and idle > idleThres:
		lastIdle = idle - idleThres
		Data['Total Idle'] = idleSoFar + lastIdle
		#print (idleSoFar, lastIdle, Data['Total Idle'])
  	
	if lastIdle > idle: #means we had activity since last
		idleSoFar = Data['Total Idle']
		lastIdle = 0
		#print ('>>', Data['Total Idle'])

	currAppTitle = GetWindowText(GetForegroundWindow())
	if Data['App Title'] != currAppTitle and currAppTitle:

		if idle > 1.0:
			moveKey()
			

		idleSoFar = 0.0
		lastIdle = 0.0

		LogFile = getLogFile()
		print ('DIFFFF', Data['App Title'],currAppTitle)
		#p = threadname.get_threadname(Data['App Title'])
		#Data['App Name']   = str(p.name).split('name=\'')[1].split('.')[0]
		#Data['AppThreadID'] = p.pid
		Data['End Time']  = strftime("%d %b %Y - %H:%M:%S")
		setCategory()
		#print Data
		#print ('##', Data['Total Idle'])
		logwrite.Write(Data, LogFile)
		#print Data
	  # reset data after log is written.
		
		SetFreshData()

def moveMouse():

	import win32api
	win32api.SetCursorPos((0,0))

def moveKey():

	import win32com.client as comclt
	wsh= comclt.Dispatch("WScript.Shell")
	wsh.SendKeys("{RIGHT}")

def setCategory():

	global Data
	Data['Category'] = 'Core'
	Data['Sub Category'] = 'Editing'

def SetFreshData():

	global Data
	from win32gui import GetWindowText, GetForegroundWindow

	print ('setting fresh data >>')
	fg_obj = GetForegroundWindow()
	p = threadname.get_threadname(fg_obj)
	if p:
		#Data.clear()
		initData()
		Data['App Title'] = GetWindowText(GetForegroundWindow())
		Data['App Name'] = str(p.name).split('name=\'')[1].split('.')[0]
		lastIdle = 0

		Data['Total Idle'] = 0.0
		Data['Start Time'] = strftime("%d %b %Y - %H:%M:%S")
	

def Now():
	localtime = int(time()) 
	return localtime

  
initApp()
