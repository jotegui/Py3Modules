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
	status = os.system( " ping -n 1 " + host + " > eraseme.tmp " ) # 0 = alive ; 1 = dead or inex
	if status == 0:
		alive = True
	deleteerase = os.system ( "del eraseme.tmp" )
	
	return alive

if __name__ == '__main__':
	host = input('Host name: ')
	alive = testHost(host)
	
	if alive == True:
		print("Host " + host + " is alive")
	else:
		print("Host " + host + " is dead")