def showDatabases( host, user, passwd ):
	'''
 Returns a tuple with the existing MySQL Databases in the given host
 '''
	import pymysql
	
	conx = pymysql.connect( host = host, user = user, passwd = passwd )
	query = "show databases;"
	cur = conx.cursor()
	cur.execute(query)
	res = cur.fetchall()
	
	return res

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
	print("\n")
	
	indexes = showDatabases(host, user, passwd)
	print("Databases in "+host+":\n")
	for i in indexes:
		print(i[0])