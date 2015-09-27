#funcion que evalua las expresiones de las pilas
def evaluaExpresion(pilaOperandos,pilaOperadores):
    ev=[0,0,0]
    ev[2] = pilaOperandos.pop()
    ev[1] = pilaOperadores.pop()
    ev[0] = pilaOperandos.pop()

    #evalua expresiones booleanas
    if ev[1] == '<' or ev[1] == '>' or ev[1]=='<=' or ev[1]=='>=' or ev[1]=='==':
        resultado = eval(''.join(ev))
        pilaOperandos.append(resultado)

    #--__--__--__--__Evalua Expresiones aritmeticas--__--__--__--__--
    elif ev[1] == '+' or ev[1] == '-' or ev[1] =='*' or ev[1]=='/':
        resultado = eval(''.join(ev))
        pilaOperandos.append(str(resultado))
    #--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__
    #operaciones de and y or
    elif ev[1] == 'V' or ev[1] == '^':
        resultado = ev[0] or ev[2]
        pilaOperandos.append(resultado)
    #implicacion
    elif ev[1] == '->':
        resultado = (not ev[0]) or (ev[2])
        pilaOperandos.append(resultado)  

#funcion que evalua las expresiones
def expresiones(expresion):
	#pila de operadores y pila de operandos
    pilaOperadores=[]
    pilaOperandos=[]
    expresion=expresion.split()
    #print(expresion)
    for x in expresion:
        if x == '(':
            pass
        elif x == ')':
            evaluaExpresion(pilaOperandos,pilaOperadores)
        elif x.isdigit():
            pilaOperandos.append(x)
        elif x == 'True':
            pilaOperandos.append(x)
        elif x =='False':
            pilaOperandos.append(x)
        else:
            pilaOperadores.append(x)
    return pilaOperandos
