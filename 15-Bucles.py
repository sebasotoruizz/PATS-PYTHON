#BUCLES
#Codigo que se va a repetir un numero determinado de veces
#Un loop, un ciclo

#BUCLE WHILE
#Tiene un numero indeterminado de iteraciones, donde
#necesitamos que se cumpla una determinada condicion, para
#que el bucle se siga repitiendo n veces
#Se va a ejecutar siempre y cuando la condicion se cumpla

#Sacar raiz cuadrada de un número con WHILE

import math     #Para poder usar luego el sqrt (raiz cuadrada)

numero = int(input("Ingrese un número: "))

while numero < 0:
    print("Error -> Debes ingresar un número positivo")
    numero = int(input("Ingrese un número: "))

print(f"La raíz cuadrada de {numero} es: {(math.sqrt(numero)):.2f}")

#Mostrar un mensaje n veces con WHILE

i = 0

while i<10:
    print(i)
    i += 1

#BUCLE FOR
#Bucle con un numero determinado de iteraciones, osea
#nosotros sabremos cuantas veces se va a repetir.

#Variable Iteradora ecorre la coleccion elemento por elemento
for i in [1,2,3,4,5]:
    print("Hola mundo")

#Mostrar el valor de la variable iteradora
for i in [1,2,3,4,5]:
    print(f"Elemento: {i}")

#Tambien podemos trabajar con diccionarios
diccionario = {"Alejandro":22,"Maria":23,"Jose":45,"Luis":12}

for i in diccionario:
    print(f"Elemento: {i}")         #Asi muestro la clave

for i in diccionario:
    print(f"{diccionario[i]}")      #Asi muestro el valor

# Y si quiero que me imprima ambos?

for i in diccionario:
    print(f"{i} -> {diccionario[i]}")     

# Tambien existe otra manera de hacerlo

for clave,valor in diccionario.items():
    print(f"{clave} -> {valor}")  

#Tambien podemos trabajar con CADENAS

cadena = "Sebastian"

for i in cadena:                       #La variable recorrera elemento por elemento nuestra cadena
    print(f"{i}")                      #Asi se imprimira "Sebastian" caracter por caracter

for i in cadena:
    print(f"{i}",end=" ")               #Imprimir "Sebastian" sin salto de linea
