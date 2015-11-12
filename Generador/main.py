#Generador de numeros
import blowfish
from generador import *


# 199,151,317,448
# variable para guardar la clave de 4 a 56 bytes (32 a 448 bits)
def getKey(p,q,x0,s):
	# Genera una lista de numeros pseudoaleatorios
	# Utilizando el algoritmo blum blum shub
	numeros = generadorBlumBlumShub(p,q,x0,s)
	
	# Genera la clave en binario
	clave_binario = generaClaveBinaria(numeros)

	# obtenemos una lista con la clave en bytes
	# para el algoritmo se obtendra un arreglo
	# de 54 bytes.
	clave_HEXADECIMAL = divideCadena(clave_binario,54)

	# convertimos el arreglo de bytes en uno 
	# equivalente a su codigo ascii
	asciiArreglo = convierteToAscii(clave_HEXADECIMAL)

	# obtenemos una palabra la cual sera nuestra clave 
	# para el algoritmo de cifrado simetrico (blowfish)
	claveAscii = concatenaArreglo(asciiArreglo)

	# convertimos la cadena a bytes
	key = bytes(str(claveAscii),encoding='UTF-8')

	return key

def getNonce(longitud):
	#genera una cadena aleatoria 
	nonce = generaNonce(longitud)

	#la convierte a hexadecimal
	nonceHexadecimal = divideCadena(nonce,4)

	#la convierte a su respectivo codigo ascii
	nonceAscii = convierteToAscii(nonceHexadecimal)
	
	#lo une todo en una palabra de 32 bits (4 bytes)
	nonceFinal = concatenaArreglo(nonceAscii)
	return nonceFinal

def getContador():
	#iniciamos el contador en un numero entre 1 -64
	contador_decimal = iniciaContador()
	#convertimos el numero a binario
	contador_binario = concatenaCeros(contador_decimal)

	#convertimos el contador a hexadecimal
	contador_HEXADECIMAL = divideCadena(contador_binario,4)

	#convertimos el valor del contador en ascii
	contador_ascii = convierteToAscii(contador_HEXADECIMAL)

	contador_Final = concatenaArreglo(contador_ascii)
	return contador_decimal,contador_Final

def generaBITS(numero):
	#si el numero es par retorna un cero
	if numero % 2 == 0:
		return "0"
	else:
	#de otro modo retorna un 1
		return "1"
	i = i + 1

def modificaContador(c):
	c = c + 1
	ConBin = concatenaCeros(c)
	conHex = divideCadena(ConBin,4)
	contadorAscii = convierteToAscii(conHex)
	contadorFinal = concatenaArreglo(contadorAscii)
	return c,contadorFinal

def generadorNumerosPseudoaleatorios(n):

	#se genera la clave
	key = getKey(239,251,3,448)
	#se genera el nonce
	nonce = getNonce(32)

	#obtenemos el contador
	contador,counter = getContador() 

	# creamos los objetos necesarios para que
	# funcione el algoritmo de cifrado
	cipher = blowfish.Cipher(key)
	cipher_little = blowfish.Cipher(b"my key", byte_order = "little")

	#cadena donde se guardara la cadena aleatoria
	cadena_aleatoria = ""

	i = 0
	while i < n:
		#concatena el nonce con el contador
		mensaje = nonce + counter

		#convierte la cadena a bytes
		mensajeBYTES = bytes(mensaje,encoding='iso 8859-1')

		#ciframos la cadena de bytes
		ciphertext = cipher.encrypt_block(mensajeBYTES)

		#convertimos a numero
		c = int.from_bytes(ciphertext, byteorder='little')
		#concatenamos un cero o un uno dependediendo del numero 
		cadena_aleatoria = cadena_aleatoria + generaBITS(c)
		
		# aumentamos el contador
		contador,counter = modificaContador(contador)
		# modificamos el numero para no caer en un loop infinito
		i = i + 1 
	return cadena_aleatoria

