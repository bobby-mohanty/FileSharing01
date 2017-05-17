
from MySQLdb import *

def dataBaseCheck(uid):
	d = connect('localhost','','')

	c = d.cursor()

	c.execute('use lit;')

	stmt = 'select uid from login where uid = "' + uid + '";'
	print stmt
	
	c.execute(stmt)
	x = c.fetchall()
	
	if (uid, ) in x:
		return 1
	else:
		return 2


