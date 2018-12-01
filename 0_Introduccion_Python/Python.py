"""
/***************************************************************************
 Ejercicios

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *                              Taller PYQGIS3                             *
 *                                                                         *
 ***************************************************************************/
"""
# Ejemplo muy tipico (Saber si un texto es una permutacion de otro)

import itertools
#¿Que problema tiene esta opcion?
def is_permutation(word,another):
    for permutation in itertools.permutations(word):
        if permutation == tuple(another):
            return True
    return False
    
value=is_permutation("amor","roma")
print (value)

# Mas sencillo
def is_permutation(word,another):
	if sorted(word)==sorted(another):
		return True
	return False


# Ejemplo Basico de python

import collections
import math

# Que es Punto?
Punto = collections.namedtuple("Punto", "x y z")

fake = Punto(x=2, y=5, z=100)

print ('Fake Punto : ', fake )

# Otro ejemplo
class Triangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return (self.base * self.altura) / 2.0

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de base {1} y altura {2}"
        return msg.format(clase, self.base, self.altura)

t = Triangulo(2, 3)
print (t)
print ("Area:", t.area)



# Ejemplo Herencia Multiple

#Clase 1
class c1(object):
    def __init__(self):
        self.x=10

#Clase 2
class c2(object):
    def __init__(self):
        self.y=20        

#Clase 3 que hereda de las otras
class c3(c1,c2):
    def __init__(self):
        self.z=30
        c1.__init__(self)
        c2.__init__(self)
        
a=c3()
print (a.x)
print (a.y)
print (a.z)

#Errores más comunes y gestión de errores

#Ejemplo Basicos

dividendo = 5
divisor = 0
print('variable: {}, divisor: {}'.format(dividendo, divisor))
print('dividendo: {0}, divisor: {1}'.format(dividendo, divisor))
dividendo / divisor

def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print ("El divisor no puede ser cero")
        
dividir (dividendo,divisor)

# Pequeñas utilidades

# Crear un carpeta 
import os
def createFolderByName(path, name):
	''' Create Folder by Name '''
	directory = os.path.join(path, name)
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
			print ('Creado')
	except OSError:
		print ('Error: Creando el directorio. ' + directory)

# Borrar un carpeta
import os
import shutil
def removeFolderByName(path, name):
	directory = os.path.join(path, name)
	try:
		if os.path.exists(directory):
			shutil.rmtree(directory, ignore_errors=True)
			print ('Borrado')
	except OSError:
		print ('Error: Borrando el directorio. ' + directory)













