def transposeFile(inipath, endpath, inisep = "\t", endsep = "\t"):
	"""
 Transposes the content of a file (with fields separated by a given character) and stores the result in another file with another separator.
 
 Arguments:
 inipath - full path to the original file
 endpath - full path to the result file. File may not exist, folder must
 inisep - string that acts as a field separator in original file
 endsep - string that will act as a field separator in result file
 
 Author: JOT (javier.otegui@gmail.com)
 """
	
	inidata = []
	enddata = []

	try:
		inifile = open(inipath, 'r')
	except IOError:
		print("No such input file" + inipath)
		return 1
	inilines = inifile.readlines()

	if inisep == "\\t":
		inisep = "\t"
	if endsep == "\\t":
		endsep = "\t"
	
	for line in inilines:
		temp = line.replace("\n","").split(inisep)
		inidata.append(temp)
	inifile.close()
	
	endfile = open(endpath, 'w')
	for i in range(len(inidata[0])):
		for j in range(len(inidata)):
			if j+1 == len(inidata):
				linetoadd = inidata[j][i]
			else:
				linetoadd = inidata[j][i] + endsep
			endfile.write(linetoadd);
		endfile.write("\n")
	endfile.close()
	
	return 0

if __name__ == '__main__':
	path = input("Path of the source file (current default): ")
	ininame = input("Name of the input file: ")
	endname = input("Name of the output file: ")
	inisep = input("Separator of the source file (tab default): ")
	endsep = input("Separator of the output file (tab default): ")
	
	if path == '':
		import os
		path = os.getcwd() + "\\"
	if inisep == '':
		inisep = "\t"
	if endsep == '':
		endsep = "\t"
	
	inipath = path + ininame
	endpath = path + endname
	
	output = transposeFile(inipath, endpath, inisep, endsep)
	if output == 0:
		print("done")
	else:
		print("Something went wrong. Check output")
