def showprocess(host, user, passwd, secs = -9):
	"""
 Shows the current threads working on a given MySQL server instance. Specifically, shows PID, Elapsed Time, current action and query for each process in the server.
 
 Arguments:
 host: a valid MySQL server host name
 user: a user with enough privileges on the server
 passwd: the users' password
 secs: the number of seconds that the information will be shown. Default is endless
 
 Returns: nothing, output is shown on screen
 
 Author: jot (javier.otegui@gmail.com)
 """
	import pymysql
	import os
	import time
	
	try:
		conx = pymysql.connect(host = host, user = user, passwd = passwd)
	except pymysql.err.OperationalError as errno:
		print("Something went wrong with the connection.")
		errcode = int(str(errno).split(",")[0][1:])
		if errcode == 2003:
			print("The host " + host + " does not seem to have a MySQL server instance running")
		elif errcode == 1045:
			print("Invalid user / password combination")
		return 1
	
	query = 'show full processlist'
	
	if secs == 0:
		secs = -9
	secs = int(secs)
	try:
		while secs >= 0 or secs == -9:
			os.system( "cls" )
			cur = conx.cursor()
			cur.execute(query)
			res = cur.fetchall()
			print("""
Process list for MySQL server instance on {0}
				""".format(host))
			for i in res:
				print("ID: " + str(i[0]))
				print("  Elapsed time: " + str(i[5]))
				print("  Action: " + str(i[6]))
				print("  Query: " + str(i[7]))
				print()
			
			if secs == -9:
				print("\n\nPress Ctrl+C at any time to exit")
			elif secs > 1:
				print ("\n\n",str(secs), "seconds left")
			elif secs == 1:
				print ("\n\n",str(secs), "second left")
			time.sleep( 1 )
			
			if secs >= 0:
				secs = secs - 1
	except KeyboardInterrupt:
		pass
	finally:
		cur.close()
		conx.close()
		return 0

if __name__ == '__main__':
	import getpass
	from jot.basic.testHost import testHost
	
	print('''Favourites:
	[1] -> pegaso.si.unav.es
	[2] -> Custom host
	''')
	host = input("Host: ")
	if (host==str(1)):
		host='pegaso.si.unav.es'
	elif (host==str(2)):
		exists = False
		while exists == False:
			host=input("Host name: ")
			exists = testHost(host)
			if exists == False:
				print("Could not find " + host + " host")
	user = input("User: ")
	if (user==str(1)):
		user='jot'
		passwd='tellechea'
	else:
		passwd = getpass.getpass('Password: ')
	secs = input( "How many seconds? (empty for unlimited): " )
	if secs == '':
		secs = 0
	
	showprocess(host, user, passwd, secs)
	
