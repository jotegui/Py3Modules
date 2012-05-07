def testHost( host ):
	"""
 Description
 Tests whether a given host is reachable or not in the current network.
 
 Arguments:
 host - string with the desired host name.
 
 Returns: boolean.
 
 Author: jot (javier.otegui@gmail.com)
 """
	import os
	import string
	import sys
	
	alive = False
	system = sys.platform
	
	if system == 'linux2':
		status = os.system("ping -c 1 " + host + " > /dev/null")
	elif system == 'win32':
		status = os.system( " ping -n 1 " + host + " > eraseme.tmp " )
		os.system ( "del eraseme.tmp" )
		
	if status == 0:
		alive = True
	
	return alive

if __name__ == '__main__':
	host = input('Host name: ')
	alive = testHost(host)
	
	if alive == True:
		print("Host " + host + " is alive")
	else:
		print("Host " + host + " is dead")
