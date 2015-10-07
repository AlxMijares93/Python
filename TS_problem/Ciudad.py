import math
import random

class Ciudad:

	"""constructor de la clase Ciudad"""
	def __init__(self,nombre,x,y):
		self.nombre = nombre
		self.x = x
		self.y = y

	"""Obtener la distancia de la ciudad dada a la actual"""
	def obtenerDistacia(self,ciudad):
		xDis = fabs(self.x-ciudad.x)#obtenemos la distancia en x de las ciudades
		yDis = fabs(self.y-ciudad.y)#obtenemos la distancia en y de las ciudades
		distancia = sqrt(pow(xDis,2)+pow(yDis,2)) #sacamos la distancia entre los nodos
		return distancia

	#representacion del objeto como string
	def __repr__(self):
		return "Ciudad: "+str(self.nombre)+"("+str(self.x)+", "+str(self.y)+")"
