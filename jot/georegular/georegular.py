def frecuenciesExtraction(data):
	
	from jot.basic.checkElementInArray import checkElementInArray
	from jot.basic.countDistinctValues import countDistinctValues
	from jot.basic.segmentArray import segmentArray
	
	datavalues = {}
	array = []
	finaldict = {}
	provlist = list(countDistinctValues(data,0).keys())
	dataSegmented = segmentArray(data)

	for i in dataSegmented:
		datadict = {}
		for j in range(len(i)-1):
			dist = round((((i[j+1][1])-(i[j][1]))**2 + ((i[j+1][0])-(i[j][0]))**2)**(1/2),4)
			
			match = checkElementInArray(dist,list(datadict.keys()))
			if match == True:
				#datadict[dist] = datadict[dist] + i[j][2]
				datadict[dist] = datadict[dist] + 1
			else:
				#datadict[dist] = i[j][2]
				datadict[dist] = 1
		datavalues = countDistinctValues(list(datadict.values()))
		array.append(datavalues)

	for j in range(0,len(provlist)):
		finaldict[provlist[j]] = array[j]

	return finaldict

def generateRandomPoints(minlat, maxlat, minlon, maxlon, latpoints, lonpoints):
	
	import random
	
	testProv = []
	
	for a in range(minlat*latpoints, (maxlat+1)*latpoints):
		for b in range(minlon*lonpoints, (maxlon+1)*lonpoints):
			testProv.append([1,a/latpoints,b/lonpoints])
	for c in range(0,len(testProv)):
		a = round(random.uniform(45,47),2)
		b = round(random.uniform(2,4),2)
		testProv.append([2,a,b])
	
	return testProv

def loadData(path):

	datafilesource = open(path,'r')
	datafile = datafilesource.readlines()
	data = []
	i = 0
	for line in datafile:
		preline = line.strip().split("\t")
		data.append([int(preline[0]),float(preline[1]),float(preline[2]), int(preline[3])])
	datafilesource.close()
	
	return data

def writeOutputToScreen(data):
	
	print("(A)\t(B)\t(C)")
	for i in list(data.keys()):
		for j in list(data[i].keys()):
			print(str(i) + "\t" + str(j) + "\t" + str(data[i][j]))
	print("""
	A = Publisher
	B = Number of times the same distance is repeated
	C = Number of different distances that are repeated B times""")
	
	return 0

def writeOutputToFile(data, path):
	
	resfile = open(path,'w')
	resfile.write("Publisher\tNumber of times the same distance is repeated\tNumber of different distances that are repeated X times\n")
	for i in list(data.keys()):
		for j in list(data[i].keys()):
			resline = str(i)+"\t"+str(j)+"\t"+str(data[i][j])+"\n"
			resfile.write(resline)
	print("Results in tabular form written in result file")
	resfile.close()
	
	return 0