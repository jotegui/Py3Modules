# -*- coding: iso-8859-1 -*-
import base64
from xml.dom import minidom
import urllib
import random
import sys

argums = []
baseHelp = '''
Extractor Universal de WebServices
==================================

Usa los siguientes argumentos para efectuar las consultas:

-i: Ruta al archivo donde est� guardada la lista de
    campos a extraer. Si no se indica otra, se toma
    la ruta por defecto: 'C:/fields.txt'.
    Ejemplos: -i"C:/Documents and Settings/prueba.txt"
                  [las dobles comillas son fundamentales
                  si hay espacios en la ruta]
              -i
                  [aqu� se tomar� la ruta por defecto]
    
-o: Ruta al archivo de salida de los datos.
    Si no se indica, se mostrar� el resultado en pantalla.
    Ocurre lo mismo que en -i con los espacios en las rutas.
    OJO! El archivo debe existir previamente.

-s: Separador de campos para el archivo de salida de datos.
    El valor debe ir entrecomillado. Por defecto se usar�n
    tabulaciones.
    Ejemplos: -s',' [para separar por comas]

-r: N�mero de veces que defe efectuarse la consulta.
    Si no se indica, se pedir� al inicio del programa
    Ejemplo: -r3
    
-m: Valor m�nimo que se usar� para crear el valor de ID.
    Si no se indica, se pedir� al inicio del programa
    Ejemplo: -m1

-M: Valor m�ximo que se usar� para crear el valor de ID.
    Si no se indica, se pedir� al inicio del programa
    Ejemplo: -M10000
     
-h: muestra el mensaje de ayuda sobre c�mo formar el archivo de lista de campos a extraer
'''
listaHelp = '''
�C�mo se forma la lista de campos a explorar?
=============================================

En un archivo de texto se debe a�adir la siguiente informaci�n:
la primera l�nea ir� ocupada por la URL del WebService de tal
manera que el programa s�lo tenga que a�adir el ID a consultar
al final de la ruta. En el resto de filas ir�n los campos que
muestra el WebService, un campo por fila. En el caso de que el
campo tenga alg�n tipo de codificaci�n, se debe a�adir al final
del nombre alguno de los siguientes comodines:

* - Si el campo est� encriptado en base64
(esta lista se ampliar� conforme aparezcan WebServices
con distintas codificaciones)

Ej: C:/fields.txt (contiene algunos campos del WebService de uBio)
namebankID
packageName
nameString*  [colocamos * porque el campo est� codificado en base64]

'''
archivocampos = ''
archivosalida = None
veces = None
separador = '\t'
minimo = None
maximo = None

for arg in sys.argv:
    if ( arg[:2] == '-h' ):
        print listaHelp
        sys.exit()
    elif ( arg[:2] == '-i' ):
        archivocampos = arg[2:]
        if ( archivocampos == '' ):
            archivocampos = 'C:/fields.txt'
    elif ( arg[:2] == '-o' ):
        archivosalida = arg[2:]
        if ( archivosalida == '' ):
            archivosalida = None
    elif ( arg[:2] == '-r' ):
        veces = arg[2:]
        if ( veces == '' ):
            veces = None
        else:
            veces = int( veces )
    elif ( arg[:2] == '-s' ):
        separador = arg[2:]
        if ( separador == '' ):
            separador = '\t'
    elif ( arg[:2] == '-m' ):
        minimo = arg[2:]
        if ( minimo == '' ):
            minimo = None
        else:
            minimo = int( minimo )
    elif ( arg[:2] == '-M' ):
        maximo = arg[2:]
        if ( maximo == '' ):
            maximo = None
        else:
            maximo = int( maximo )
    argums.append( arg )

try:
    argums[1]
except IndexError:
    print baseHelp
    sys.exit()
    
print "Valores argumentales:"
print "Entrada: " + str( archivocampos )
print "Salida: " + str( archivosalida )
print "Repeticiones: " + str( veces )
print "Separador: " + str( separador )
print ""

if ( archivocampos == "" ):
    print '''ERROR: no se ha especificado una ruta de origen de campos v�lida.
A�ade -i al comando con la ruta del archivo origen de los campos.
Para obtener ayuda, no a�adas ning�n argumento.
'''
    sys.exit()

campos = []
textocampos = open( archivocampos, 'r' )
line = textocampos.readline()
while line:
    campos.append( line.replace( "\n", "" ) )
    line = textocampos.readline()

urlbase = campos[0]
campos.remove( campos[0] )

if ( veces == None ):
    veces = int( raw_input( 'Repeticiones > ' ) )
if ( minimo == None ):    
    minimo = int( raw_input( 'M�nimo > ' ) )
if ( maximo == None ):
    maximo = int( raw_input( 'M�ximo > ' ) )
if ( archivosalida <> None ):
    salida = open( archivosalida, 'w' )

novalido = 0
id = random.randrange( minimo, maximo )
urlcompleta = urlbase + str( id )
xmldoc = minidom.parse( urllib.urlopen( urlcompleta ) )
for campo in campos:
    if ( campo[-1:] == "*" ):
        valor = xmldoc.getElementsByTagName( campo[:-1] ).item( 0 )
        b64 = True
    else:
        valor = xmldoc.getElementsByTagName( campo ).item( 0 )
        b64 = False
    if ( valor == None ):
        print "No existe el campo '" + campo + "'"
        novalido += 1
if ( novalido > 0 ):
    print "\nHay errores en la lista de campos.\nRev�sala y vuelve a ejecutar el programa"
    sys.exit()

if ( archivosalida <> None ):
    print "Ejecutando.",
vez = 1
while vez <= veces:
    id = random.randrange( minimo, maximo )
    urlcompleta = urlbase + str( id )
    xmldoc = minidom.parse( urllib.urlopen( urlcompleta ) )
    if ( archivosalida <> None ):
        salida.write( str( vez ) + str( separador ), )
        print ".",
    else:
        print str( vez ) + str( separador ),
    for campo in campos:
        if ( campo[-1:] == "*" ):
            valor = xmldoc.getElementsByTagName( campo[:-1] ).item( 0 )
            b64 = True
        else:
            valor = xmldoc.getElementsByTagName( campo ).item( 0 )
            b64 = False
        if ( valor == None ):
            print "No existe el campo '" + campo + "'"
        else:
            if ( valor.firstChild == None ):
                valordentro = 'Null'
            else:
                if ( b64 == True ):
                    valordentro = base64.b64decode( xmldoc.getElementsByTagName( campo[:-1] ).item( 0 ).firstChild.data )
                else:
                    valordentro = xmldoc.getElementsByTagName( campo ).item( 0 ).firstChild.data
            if ( archivosalida <> None ):
                salida.write( str( valordentro ) + separador, )
                print ".",
            else:
                print str( valordentro ) + str( separador ),
    if ( archivosalida <> None ):
        salida.write( '\n' )
        print ".",
    else:
        print "\n"
    vez += 1
