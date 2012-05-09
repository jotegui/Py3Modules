def showDbSize( host, user, passwd ):
	'''
 Returns a tuple with the existing MySQL Databases in the given host and their sizes
 '''
	import pymysql
	
	conx = pymysql.connect( host = host, user = user, passwd = passwd )
	query = "SELECT table_schema \"Data Base Name\", sum( data_length + index_length )/1024/1024 \"Data Base Size in MB\" FROM information_schema.TABLES GROUP BY table_schema;"
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
	
	indexes = showDbSize(host, user, passwd)
	print("Databases in "+host+":\n")
	for i in indexes:
		size = ""
		if len(str(round(i[1],0)))<=3:
			size = str(round(i[1],3))+"Mb"
		elif len(str(round(i[1],0)))>3 and len(str(round(i[1],0)))<=6:
			size = str(round(i[1]/1000,2))+"Gb"
		else:
			size = str(round(i[1]/1000000,2))+"Tb"
		print(i[0]+": "+size)