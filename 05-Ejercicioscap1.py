#EJERCICIO 1

#Escriba la siguiente expresion en forma de expresion algoritmica
# a^3 x (b^2-2ac)  /  2b
'''
a = float(input("a -> "))
b = float(input("b -> "))
c = float(input("c -> "))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"El resultado es: {resultado}")
'''
#EJERCICIO 2

#Determinar la solución lógica de la siguiente operación
#((3+5x8)<3 and ((-6/3 x4)+2<2)) or (a<b)
'''
a = float(input("a-> "))
b = float(input("b-> "))

resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)

print(f"El resultado es: {resultado}")
'''
#EJERCICIO 3

#Hacer un programa para intercambiar el valor de 2 variables
#Por ejemplo:   a = 10          a = 5
#               b = 5     ->    b = 10
'''
a = input("Digite el valor de a: ")
b = input("Digite el valor de b: ")

a , b = b , a       #Aqui estamos diceindo que dentro de A se debe almacenar el valor de B y viceversa

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
'''
#EJERCICIO 4

#Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia
#área = pi * r^2
#longitud = 2 * pi * r
'''
import math

r = float(input(f"Ingrese el radio: "))
area = math.pi * r ** 2
longitud = (2 * math.pi * r)

print(f"EL área del circulo es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")
'''
#EJERCICIO 5

#Una tienda ofrece un descuento del 15% sobre el total de la compra
# y un cliente desea saber cuánto deberá pagar finalmente por su compra

precio = int(input("Ingrese el precio del producto: "))
descuento = (precio / 100 * 15)
preciofinal = precio - descuento

print(f"El precio final del producto es de: ${preciofinal}")






