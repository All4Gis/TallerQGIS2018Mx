"""
/***************************************************************************
 Comandos Basicos

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *                              Taller PYQGIS3                             *
 *                                                                         *
 ***************************************************************************/
"""

# Cargamos la capa vertidos

#Acceder al canvas
canvas = iface.mapCanvas()

#Ir al Layer Activo
layer= iface.activeLayer()

#Mostrar metodos
dir(layer)

#Ir a los regiStros de un layer
for f in layer.getFeatures():
  print (f)
  
#Ir a un registro en concreto
for f in layer.getFeatures():
  print (f['NAME'], f['USE'])
  
#Extraer la geometria
for f in layer.getFeatures():
  geom = f.geometry()
  print ('%s, %s, %f, %f' % (f['NAME'], f['USE'],
         geom.asPoint().y(), geom.asPoint().x()))

#Guardamos atributos en un fichero de texto
#path_absolute = QgsProject.instance().readPath("./")+"/"+"output/"
path_absolute = 'D:/tmp/'
output_f = open(path_absolute+'AIRPORTS.txt', 'w')
layer= iface.activeLayer()
for f in layer.getFeatures():
  geom = f.geometry()
  line = '%s, %s, %f, %f' % (f['NAME'], f['USE'],
          geom.asPoint().y(), geom.asPoint().x())
  u_line = line.encode('utf-8')
  output_f.write(str(u_line)+ '\n')
  
output_f.close()

		 
#Encontrar un layer por su nombre
from qgis.core import QgsProject
layer = QgsProject.instance().mapLayersByName("airports")[0]
print (layer.name())

#Cargar un layer vectorial
layer = iface.addVectorLayer(r"lakes.shp","lakes","ogr")

if not layer: 
	print ("""Oooops!!Layer invalido""")

#Cargar un raster
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import QgsProject

fileName = r"mosaico_gdl2017_mascara.tif"
fileInfo = QFileInfo(fileName)
baseName = fileInfo.baseName()
rlayer = QgsRasterLayer(fileName, baseName)
QgsProject.instance().addMapLayer(rlayer)
 
#Lo establecemos como activo
iface.setActiveLayer(layer)

#Obtener todos los layers del proyecto
canvas = iface.mapCanvas()
layers = [canvas.layer(i) for i in range(canvas.layerCount())]

#Obtener sus nombres
layers_names = [ layer.name() for layer in layers ]
print ("layers TOC = ", layers_names)

#Lista de algoritmos
#Que algoritmos existen?
for alg in QgsApplication.processingRegistry().algorithms():
	print("{}:{} --> {}".format(alg.provider().name(), alg.name(), alg.displayName()))

#Ayuda para un algoritmo en concreto
processing.algorithmHelp('qgis:randomselection')

#Metodo
import processing
processing.algorithmHelp("qgis:randomselection")

#Ejecutando un algoritmo
layer= iface.activeLayer()
params = {
    'INPUT': layer,
	'METHOD': 0,
    'NUMBER': 50,
}
processing.run("qgis:randomselection",params)

#Lipiamos la seleccion
layer.removeSelection()

#Tambien podemos borrar la seleccion de todos los layers
canvas = iface.mapCanvas()

for layer in canvas.layers():
    if layer.type() == layer.VectorLayer:
        layer.removeSelection()

canvas.refresh()


#Borrar todos los layers del proyecto  http://qgis.org/api/2.18/classQgsMapLayerRegistry.html
QgsProject.instance().removeAllMapLayers()


###### Barras de herramientas ######

#Borramos una barra de herramientas
toolbar = iface.helpToolBar	()	
parent = toolbar.parentWidget()
parent.removeToolBar(toolbar)

#Volvemos añadirla
parent.addToolBar(toolbar)

#Borrar una accion de una barra de herramientas
actions = iface.attributesToolBar().actions()
iface.attributesToolBar().clear()
iface.attributesToolBar().addAction(actions[4])
iface.attributesToolBar().addAction(actions[3])
 

#Borrar un menu completamente
menu = iface.helpMenu()	
menubar = menu.parentWidget()
menubar.removeAction(menu.menuAction())

#Volvemos añadirla
menubar.addAction(menu.menuAction())

#Añadir un menu completo
 
from PyQt5.QtGui import *
import webbrowser
from PyQt5.QtCore import *

path = r'g_icon.jpg' 

def startZoomIn():
	canvas = iface.mapCanvas()
	canvas.zoomIn()
	return
	
def About():
	url = 'https://es.wikipedia.org/wiki/Guadalajara_(M%C3%A9xico)'
	webbrowser.open(url,new=2)
	return
	
action = QAction(u"Zoom In", iface.mainWindow())
action.triggered.connect(startZoomIn) 

param = QAction(QIcon(path), \
        u"Sobre Guadalajara", iface.mainWindow())
param.triggered.connect(About) 

menu = QMenu()
menu.setTitle(u"&Viva la tierra del tequila")
menu.addActions([action, param])
iface.pluginMenu().addMenu(menu)


# Crear un polygono desde un WKT
layer = QgsVectorLayer('Polygon?crs=epsg:4326', 'Mississippi', 'memory')
pr = layer.dataProvider()
poly = QgsFeature()
geom = QgsGeometry.fromWkt("POLYGON ((-88.82 34.99,-88.0934.89,-88.39 30.34,-89.57 30.18,-89.73 31,-91.63 30.99,-90.8732.37,-91.23 33.44,-90.93 34.23,-90.30 34.99,-88.82 34.99))")
poly.setGeometry(geom)
pr.addFeatures([poly])
layer.updateExtents()
QgsProject.instance().addMapLayers([layer])
