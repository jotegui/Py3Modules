def colChecker(checkSource = 'online', namesPath, resPath):
	
	if checkSource == 'db':
		import MySQLdb
	
	namesList = []
	founds = {}

	namesFile = open(namesPath)
	logFile = open(logPath, 'w')

	for line in namesFile:
		namesList.append(line.replace('"','').rstrip().lstrip().upper().split(" "))

	namesFile.close()
	del namesList[0]
	maxlength = len(namesList)

	resFile = open(resPath, 'w')

	pos = 1
	
	if checkSource == 'db':
		conx = MySQLdb.connect(host="pegaso.si.unav.es", user="jot", passwd="tellechea", db="icol2011ac5Dec")
		print "Connection established"
	
	for i in namesList:
		
		if checkSource == 'online':
			numrows = onlineCheck(i)
		elif checkSource == 'db':
			numrows = dbCheck(i)
		
		if numrows == 0:
			print " not found"
		else:
			print " found !!!!!"
			resFile.write(" ".join(i))
			resFile.write("\n")
		
		for j in founds.keys():
			if j == numrows:
				match = 1
				goodJ = j
		
		if match == 0:
			founds[numrows] = 1
		else:
			founds[goodJ] += 1
		
		pos += 1


def onlineCheck(i):
	
	import urllib2
	from xml.dom import minidom
	from xml.parsers.expat import ExpatError
	
	URL = "http://www.catalogueoflife.org/annual-checklist/col/webservice?name=" + "+".join(i)
	checkporn = urllib2.urlopen(URL)
	
	try:
		xmldoc = minidom.parse(checkporn)
	except ExpatError:
		print "found to be pron"
		continue
	
	numrows = int(xmldoc.firstChild.attributes["total_number_of_results"].value)
	
	return numrows

def dbCheck(i):
	
	query = 'select * from jot_col_taxonomy where scientific_name="' + " ".join(i) + '";'
	conx.query(query)
	
	result = conx.store_result()
	numrows = result.num_rows()
	
	return numrows