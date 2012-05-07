def prepmapa(results,escala):
	from math import ceil, log, floor
	import os
	
	fileres = os.getcwd()+'\\..\\www\\testpython\\Datos.temp'
	resdata = open( fileres, 'w' )
	
	for i in results:
		for j in i:
			resdata.write(str(j)+"|",)
		if (escala=="exponencial"):
			k=int(ceil(log(j,2)))
		elif (escala=="aritmetica"):
			k=floor(j/200)
		if (k>=11):
			k=11
		resdata.write (str(k)+"\n")
	return 0
	
def prepdiatomea(results,escala,annocentro):
	from math import ceil, log, sin, cos, radians, floor
	from datetime import date
	import os
	
	fileres = os.getcwd()+'\\..\\www\\testpython\\Datos.temp'
	resdata = open( fileres, 'w' )
	
	for i in results:
		anno=i[0].year
		diaannum=(i[0]-date(anno,1,1)).days
		if (ceil(anno/4)==(anno/4) and i[0].month>2):
			diaannum=diaannum+1
		diaradian=radians(diaannum*360/366)
		x=(anno-annocentro)*cos(diaradian)
		y=(anno-annocentro)*sin(diaradian)
		if (escala=="exponencial"):
			k=int(ceil(log(i[1],2)))
		elif (escala=="aritmetica"):
			k=floor(i[1]/200)
		if (k>=11):
			k=11
		resdata.write(str(x)+"|",)
		resdata.write(str(y)+"|",)
		resdata.write(str(i[1])+"|",)
		resdata.write(str(k)+"\n")
	return 0
