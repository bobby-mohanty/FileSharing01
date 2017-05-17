from os import path
from socket import *

sid = socket()

sid.connect(('192.168.1.1', 3000))

userid = raw_input('Enter the userid: ')

sid.send(userid)

status=sid.recv(1)

print status , type(status)

if status=='1':
	print 'welcome '
	fname = raw_input("Enter the file name : ")
	if path.exists(fname):
		sid.send('1')#sending status for path is exist 
		sid.send(str(len(fname)))
		sid.send(fname)

		fo = open(fname, 'r')
		while 1:
			data = fo.read(1)
			sid.send(data)
			if not data:
				break
		fo.close()

	else:
		sid.send('0')
		print 'Path doesn\'t exists'
else:
	print 'You are not a valid user'

sid.close()



