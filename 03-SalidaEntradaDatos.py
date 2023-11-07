##########SALIDA DE DATOS##########

#01-Imprimir por CONSOLA
nombre = 'Sebastian'
edad = 19

print("Hola",nombre,"tienes",edad,"años")

#02-Formateo de cadenas
#método f-strings
nombre = 'Sebastian'
edad = 19
print(f"Hola {nombre} tienes {edad} años")

#método ,format()
nombre = 'Sebastian'
edad = 19

print("Hola {} tienes {} años".format(nombre,edad))


##########ENTRADA DE DATOS##########

#Datos de tipo Cadena
nombre = input("Ingresa tu nombre: ")

print(f"Hola {nombre}")

#Datos de tipo Numérico

#guardar entero
numero = int(input("Ingresa un número: "))

print(f"El número es {numero}")

#guardar decimales
numero = float(input("Ingresa un número: "))

print(f"El número es {numero}")
