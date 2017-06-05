from os import fork
from os import wait
from signal import signal
from socket import socket
from thread import start_new_thread
from threading import Thread
from time import sleep
from os import path
from MySQLdb import *
from logincheck import dataBaseCheck

sid = socket()
sid.bind(('192.168.1.5', 3000))
sid.listen(1)
bsid = socket()
bsid.connect(('192.168.1.10',3000))
cid = None
caddr = None
	
class mythread(Thread):
		
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		operation()

def operation():
	
	uid = cid.recv(20)
	status=dataBaseCheck(uid)
	bsid.send(uid)
	cid.send(str(status))	

	if status==1 and cid.recv(1)=='1':
		l = cid.recv(1)
		print l
		fname = cid.recv(int(l))
		print caddr[0], fname
		sleep(1)
		bsid.send(l)
		bsid.send(fname)
	#	path = uid + '/' + fname
	#	fo = open(path, 'a')
	
		while 1:
			data = cid.recv(1)
			if not data:	
				break
			bsid.send(data)
			print data, 
	#	fo.close()
		cid.close()
		bsid.close()
	else:
		cid.close()
		bsid.close()	

def sigchld_handler(x, y):	
	pid, status = wait()
	print 'server knows one child server is dead'
	main()

def main():
	global cid
	global caddr
	global mythread

	signal(17, sigchld_handler)
	while 1:
	
		cid , caddr = sid.accept()
	
		#create a child server for the operation
		if fork()==0: 
			operation()
		#start_new_thread(operation, ())
		#mythread().start()
	
	sid.close()

main()


