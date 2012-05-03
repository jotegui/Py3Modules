'''
Created on 01/03/2011
@author: jotellechea
'''
from xml.dom import minidom
import urllib

preurl = 'http://data.gbif.org/occurrences/'
posturl = '/providerMessage.xml'
archivoids = 'C:/ids.txt'

textoids = open( archivoids, 'r' )
line = textoids.readline()

while line:
    line2 = line.strip()
    if ( line2 <> '"id"' ):
        url = preurl + line2 + posturl
        print url
    line = textoids.readline()
    
xmldoc = minidom.parse( urllib.urlopen( url ) )
valor = xmldoc.getElementsByTagName( campo ).item( 0 )
