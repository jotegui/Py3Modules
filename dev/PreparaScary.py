# Programilla para crear tablas de preparacion de Scarys, directamente a partir de consultas.

import MySQLdb

a = [] #Matriz individual para cada subserie
b = [] # Super-Matriz donde se van almacenando las a[]

# Contadores para la creacion de la matriz final
i = 0
j = 0

fileres = raw_input( "Archivo para los resultados: " )
filas = int( raw_input( "Filas: " ) )
cols = int( raw_input( "Columnas: " ) )
conx = MySQLdb.connect( host = "zercon", user = "jot", passwd = "jotellechea", db = "GBIF200904" )
querydata = "select * from jot_test"
c = conx.cursor()
cuentafil = 0
cuentacol = 0


while cuentacol < cols:
    querydata = "select resource from jot_gbifes_created where created is not null order by modified limit " + str( cuentacol * filas ) + "," + str( filas )
    c.execute( querydata )
    resultado = c.fetchall()
    while cuentafil < filas:
        try:
            temp = resultado[cuentafil][0]
        except IndexError:
            temp = ""
        a.append( temp )
        cuentafil += 1
    b.append( a )
    cuentafil = 0
    cuentacol += 1
    print cuentacol, "columna/s procesada/s"
    a = []

print "Termina el procesamiento del sql"
print len( b ), "columnas"
print len( b[0] ), "filas"

resdata = open( fileres, "w" )

while i < len( b[0] ):
    try:
        while j < len( b ):
            try:
                resdata.write( str( b[j][i] ) + "\t", )
            except IndexError:
                pass
            j += 1
    except IndexError:
        pass
    j = 0
    i += 1
    print i, "fila escrita"
    resdata.write( "\n" )
