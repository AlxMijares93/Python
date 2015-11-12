#archivo para hacer el generador de una clave blumblumshub
import math
import random

"""
	p y q deben ser dos numeros primos muy grandes 
	tales que p mod 4 = 3 and q mod 4 = 3
	esto permite aegurar que cada residuo posee una 
	raiz cuadrada 
"""
def valida(p,q):
	#si p y q cumplen la condicion retorna verdadero
	if (p % 4 == 3) and (q % 4 == 3):
		return True
	# de otro modo retorna false
	return False


"""
	funcion que generara una secuencia de numeros pseudoaleatorios
	de acuerdo con el algoritmo blum blum shub,
	devolvera una lista vacia si los numeros p y q no son primos
"""
def generadorBlumBlumShub(p,q,x0,s):
	i = 0 # variable auxiliar 
	M = p*q # m es igual a la multiplicacion de p y q
	x_siguiente = 0 #variable para calcular la x siguiente
	x_anterior = x0 #x anterior
	numeros = [] #lista donde se iran guardando los numeros generados
	#si se cumple la condicion se realizara el algoritmo
	if valida(p,q):
		##ciclo para generar s iteraciones
		while i < s:
			x_siguiente = math.pow(x_anterior,2) % M # calculamos x_i+1 = xi^2 mod M
			numeros.append(int(x_siguiente)) #guardamos el numero generado
			x_anterior = x_siguiente #cambiamos la x 
			i = i +1 #incrementamos el contador
	#devolvemos la lista de numero, si no se cumplen las condiciones de p y q
	#la lista estara vacia
	return numeros


"""
	funcion que nos servira para generar una cadena bits aleatoria
"""
def generaClaveBinaria(numeros):
	clave = ""
	#ciclo para generar n bits
	for x in numeros:
		if (x % 2) == 0:
			clave = clave + str(0) # si la clave es par guarda un cero
		else:
			clave = clave + str(1) # si la clave es non guarda un uno
	#devuelve la clave como cadena
	return clave


"""
	funcion para generar un Nonce del numero de bits que 
	solicite el usuario
"""
def generaNonce(n):
	Nonce = ""
	numero = 0
	for i in range(0,n):
		numero = random.randint(1,2**16)
		if numero % 2 == 0:
			Nonce = Nonce +  "0"
		else:
			Nonce = Nonce + "1"
	return Nonce


"""
	funcion que sirve para dividir una cadena de bits
	en un arreglo de bytes
"""
def divideCadena(cadena,n):
	a = 0
	b = 8
	hexadecimales=[]
	decimal = 0
	hexa = ''
	nhexa=''
	for i in range(0,n):
		decimal = int(cadena[a:b],2)
		hexa = hex(decimal)
		#nhexa = bytes(hexa,encoding="UTF-8")
		hexadecimales.append(hexa)
		a = a + 8
		b = b + 8
	return hexadecimales

"toma una lista y lo convierte en una cadena concatenando los elementos"
def concatenaArreglo(hexadecimales):
	cadena=""
	for x in hexadecimales:
		cadena = cadena + x
	return cadena

def convierteToAscii(hexadecimales):
	caracteres = []
	c = 0
	for i in hexadecimales:
		c = int(i,16)
		if c < 32:
			c = c + 32
		elif c > 126 and c < 190:
			c = c - 2**6
		elif c > 190:
			c = c - 2**7
		caracteres.append(chr(c))	
	return caracteres


def iniciaContador():
	c = random.randrange(1,1024)
	return c

def concatenaCeros(numero):
	cb = bin(numero)[2:]
	i = len(cb)
	i = 32 - i
	cb = '0'*i + cb
	return cb
