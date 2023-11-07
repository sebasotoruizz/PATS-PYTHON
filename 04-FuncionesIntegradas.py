#Funciones Integradas
#Sirven para hacer conversiones entre tipos de datos

#Convertir Cadena a Numero Entero
n = int("10")
print(n)

#Convertir Cadena a valor real (flotante)
n = float("10")
print(n)

#Convertir Valor Numerico a Cadena
n = str(12)
print(n)

#Convertir Valor Entero a Valor Binario
n = bin(10)         #Los 2 primeros caracteres, 0b indican que es un valor binario
print(n)

#Convertir Valor Entero a Hexadecimal
n = hex(10)
print(n)

#Convertir Valor Binario a Entero
n = int("0b1010",2)
print(n)

#Convertir Valor Hexadecimal a Entero
n = int("0xa",16)
print(n)

#Valor Absoluto de un número
n = abs(-8)
print(n)

#Redondear un número
n = round(5.6)
print(n)

#Contar Caracteres de una cadena
n = len("Alejandro")
print(n)