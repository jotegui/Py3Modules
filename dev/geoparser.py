def geoparser ( filedat, fileres ):
    
    import urllib
    import re

    f = open( filedat )
    g = open( fileres, 'w' )
    Vacio = 0
    Inexistente = 0
    Correcto = 0
    Invertido = 0
    Erroneo = 0
    NE = 0
    Regs = 0
    i = 0
    preurl = 'http://ws.geonames.org/countryCode?style=full'
    for line in f:
        Regs = Regs + 1
        fields = re.split( '\t', line )
        print 'Procesando Reg# ' + str( Regs )
        #print fields[0] + ' ' + fields[1] + ' ' + fields[2] + ' ' + fields[3] # debugging
        posturl = '&lat=' + fields[1] + '&lng=' + fields[2]
        datos = ''
        Estado = ''
        if ( fields[1] == '' or fields[2] == '' ) or fields[3].strip() == '':
            Estado = 'Incompleto'
            Vacio = Vacio + 1
        else:
            urlcompleta = preurl + posturl
            print urlcompleta # debugging
            datos = urllib.urlopen( urlcompleta ).read().strip()
            iso_orig = fields[3].strip()
            if datos == iso_orig:
                Estado = 'Correcto'
                Correcto = Correcto + 1
            else:
                posturlinv = '&lat=' + fields[2] + '&lng=' + fields[1]
                urlcompletainv = preurl + posturlinv
                print urlcompletainv # debugging
                datosinv = urllib.urlopen( urlcompletainv ).read().strip()
                if datosinv == iso_orig:
                    Estado = 'Invertido'
                    Invertido = Invertido + 1
                elif len( datos ) > 2:
                    Estado = 'Inexistente'
                    Inexistente = Inexistente + 1
                else:
                    Estado = 'Erroneo'
                    Erroneo = Erroneo + 1
        print fields[0] + ' ' + Estado # debugging
        g.write( fields[0] + '\t' + fields[1] + '\t' + fields[2] + '\t' + fields[3].strip() + '\t' + Estado )
        g.write( '\n' )
    TotCorr = str( Correcto * 100 / Regs )
    TotInv = str( Invertido * 100 / Regs )
    TotErr = str( Erroneo * 100 / Regs )
    TotNE = str( Inexistente * 100 / Regs )
    TotVac = str ( Vacio * 100 / Regs )

    Results = ['Correctos: ' + str( TotCorr ) + '%', 'Invertidos: ' + str( TotInv ) + '%', 'Erroneos: ' + str( TotErr ) + '%', 'Inexistentes: ' + str( TotNE ) + '%', 'Incompletos: ' + str ( TotVac ) + '%', fileres]
    print '------- \n'
    return Results

import msvcrt
print '''
/------------------------------------------------------------------------\\
| Bienvenido al parseador de coordenadas made in JOT.                    |
|                                                                        |
| Este programilla requiere un archivo de entrada de datos               |
| estructurado con los campos Id, Latitud, Longitud y codigo de pais     |
| ISO de 2 letras, cada uno separado del otro por un espacio.            |
|                                                                        |
| A continuacion se pregunta la ruta del archivo que contiene los datos  |
| y un nombre para el archivo que contendra los resultados.              |
|                                                                        |
| Gracias por usar Software programado por JOT                           |
\------------------------------------------------------------------------/
'''
char = 0
print '''Toma el tiempo necesario para preparar el archivo tal y como pone en la intro y pulsa cualquier tecla'''
while not char:
    char = msvcrt.getch()
entrada = raw_input( 'Archivo de entrada: ' )
salida = raw_input( 'Archivo de salida: ' )
Results = geoparser( entrada , salida )
i = 0
while i < 5:
    print Results[i]
    i = i + 1
print 'Los resultados se encuentran en el archivo ' + salida
