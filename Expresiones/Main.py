from Expresiones import *
#ejemplos de expresiones aritmeticas y booleanas
#cada digito, parentesis u operador debe de estar con un espacio en blanco
#

e1 = ' ( ( 4 < 44 ) V ( 3 == 8 ) )'
e2 = '( True ^ False )'
e3 = '( ( True ^ True ) V ( False ) ^ ( 4 > 1 ) )'
e4 = '( ( 7 < 9 ) ^ ( 100 == 300 ) )'
e5 = '( ( 4 + 3 ) + 100 )'
e6 = '( ( 4 > 12 ) ^ ( 100 == 20 ) )'
e7 = '( ( ( 4 - 6 ) * 9 ) * 5 )'
e8 = '( ( 4 > 5 ) V ( 6 == 4 ) )'
e9 = '( 3 <= 3 )'

#expresiones de prueba y ejemplo
print(expresiones('( ( 4 < 44 ) V ( 3 == 8 ) )'))
print(expresiones('( True ^ False )'))
print(expresiones('( ( True ^ True ) V ( False ) ^ ( 4 > 1 ) )'))
print(expresiones('( ( 7 < 9 ) ^ ( 100 == 300 ) )'))
print(expresiones('( ( 4 + 3 ) + 100 )'))
print(expresiones('( ( 4 > 12 ) ^ ( 100 == 20 ) )'))
print(expresiones('( ( ( 4 - 6 ) * 9 ) * 5 )'))
print(expresiones('( ( 4 > 5 ) V ( 6 == 4 ) )'))
print(expresiones('( 3 <= 3 )'))
#implicaciones
print(expresiones('( True -> False )'))
print(expresiones('( ( True -> True ) -> True )'))
print(expresiones('( ( True -> True ) -> False )'))
print(expresiones('( ( 1 < 3 ) -> True )'))
print(expresiones('( ( ( 1 == 3 ) -> True ) ^ ( 4 == 4 ) )'))
