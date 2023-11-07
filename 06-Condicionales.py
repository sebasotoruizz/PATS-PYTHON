# CONDICIONALES
# Sirven para comparar 2 valores, dandome un valor lógico
# Es decir o un verdadero o un falso


#Indica si es mayor o menor de edad
'''
edad = int(input("Digite su edad: "))

if edad >= 18 and edad < 150:
    print("Eres mayor de edad")
elif edad < 18 and edad > 0:
    print("Eres menor de edad")
else:
    print("¡Edad inválida!")
'''

#CONDICIONALES COMBINADOS

edad = int(input("Digite su edad: "))

if 0<edad<100:
    print("Edad correcta")
    if edad>=18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")
