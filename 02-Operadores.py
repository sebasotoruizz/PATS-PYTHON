#OPERADORES ARITMETICOS

#SUMA RESTA MULTIPLICACION DIVISION
'''Podemos sumar directamente los valores'''
resultado = 10 + 5 * 2 / 4
print(resultado)

'''O podemos traer variables que almacenen un valor'''
num1 = 10
num2 = 5
num3 = 2
num4 = 4
resultado = num1 + num2 * num3 / num4
print(resultado)

num1 = 10
num2 = 3
resultado = num1 / num2 # Podemos utilizar // para redondear hacia abajo
print(resultado)

num1 = 10
num2 = 3
resultado = num1 % num2 # Podemos utilizar % paraa saber el resto de la division
print(resultado)

num1 = 2
num2 = 5
resultado = num1 ** num2 # Podemos utilizar ** para la exponenciacion
print(resultado)

'''OPERACIÓN'''

resultado = 3**3 * (13/5 -(2*4))
print(resultado)

#OPERADORES RELACIONALES

resultado = 10 < 20   #Mayor qué
print(resultado)

resultado = 10 > 20   #Menor qué
print(resultado)

resultado = 10 == 20  #operador de igualdad (no confundir con el = de asignación)
print(resultado)

resultado = 10 != 20  #operador de diferencia
print(resultado)

'''Podemos combinar Operadores Aritmeticos
    con los Operadores Relacionales'''

a = 10
b = 20 
c = 30
resultado = a+b==c
print(resultado)

#OPERADORES LÓGICOS

'''NOT, AND y OR
    EJEMPLO  '''
a=10
b=15
c=20
resultado = ((a<b) and (b<c))
print(resultado)

#OPERADORES DE ASIGNACIÓN

a = 0
a+= 5           #suma en asignación
a-= 2           #resta en asignación
a*= 3           #multiplicación en asignación
a/= 3           #división en asignación
a**=2           #potencia en asignación
a%= 2           #modulo en asignación

print(a)