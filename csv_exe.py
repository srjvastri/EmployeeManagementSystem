#encoding:UTF-8

#@change: for above see http://www.python.org/dev/peps/pep-0263/
#@change: switch to using simplejson when available attempting to remove erros
try: import simplejson as json
except ImportError: import json

from time import localtime, time, strftime
import uuid
import csv
def Write(data, logfile):
	
	#logfile = logfile + '.csv'
	#data['Timestamp'] = strftime("%H:%M:%S")
	#data['GUID'] = str(uuid.uuid4())
	#data['date_time_stamp'] = strftime("%d %b %Y - %H:%M:%S")
	#if 'ActiveText' in data:
	#	data['ActiveText'] = str(data['ActiveText'])
	#data['ActiveText'] = str(data['ActiveText']).encode('UTF-8')
	#print (data.keys())
	#print (data.values())
	if not 'C1' in data.keys():
		if not precheckData(data):
			return

		data = fillDetails(data)

	#print (data)
	#data['ActiveText'] = data['ActiveText']
	#add more data to make it freindly to Drupal date module
	#text = json.dumps(data, separators=(',',':')) #compact
	#print (text)
	#f = open(logfile, 'a', )
	#f.write (text + "\n")
	#f.close()
	try:
		outputFile = open(logfile, 'a', newline='', encoding = 'utf-8')
		output = csv.writer(outputFile)
		#enData = [(each).encode("utf-8") for each in list(data.values())]
		#print (data.values())
		output.writerow(data.values())
		outputFile.close()
	except IOError as io:
		print(io)
	except Exception as e:
		print (e)



def precheckData(data):
	
	if not data['App Name'] or not data['App Title']:
		return False

	inactiveWindows = ['Task Switching', 'Windows Default Lock Screen', 'UnlockingWindow']
	if data['App Title'] in inactiveWindows:
		return False


	return True

def fillDetails(data):

	data['User Name'] = getUserName()
	data['Machine Name'] = getMachineName()
	totalDuration = getDuration(data['Start Time'], data['End Time'])
	data['Total Idle'] = round(data['Total Idle'] / 60.0, 2)
	data['Total Duration'] = totalDuration
	activeDuration = round(totalDuration - data['Total Idle'], 2)
	if activeDuration > totalDuration:
		activeDuration = totalDuration
	if activeDuration < 0:
		activeDuration = 0
	data['Active Duration'] = activeDuration
	
	return data

def getUserName():

	import getpass
	return getpass.getuser()

def getMachineName():

	import socket
	return socket.gethostname()

def getDuration(startTime, endTime):

	import datetime

	startDT = datetime.datetime.strptime(str(startTime), "%d %b %Y - %H:%M:%S")
	if not endTime:
		endDT = startDT
	else:
		endDT = datetime.datetime.strptime(str(endTime), "%d %b %Y - %H:%M:%S")

	difference = round((endDT - startDT).total_seconds()/60.0, 2)

	return difference

