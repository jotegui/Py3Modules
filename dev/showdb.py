def showdatabases( host, user, passwd ):
	import MySQLdb
	
	conx = MySQLdb.connect( host = host, user = user, passwd = passwd )
	query = "show databases;"
	conx.query( query )
	results = conx.store_result()
	indexes = results.fetch_row( maxrows = 0, how = 0 )
	
	return indexes

if __name__ == '__main__':
	from getpass import getpass
	
	host = input("Host name: ")
	user = input("User name: ")
	passwd = getpass()
	
	indexes = showdatabases(host, user, passwd)
	
	for i in indexes:
		if i[0] == 'information_schema':
			pass
		else:
			print(i[0])