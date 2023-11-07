#EJERCICIO 1
#Hacer un programa que pida 2 números y se de cuenta cuál
#de ellos es par, o si ambos lo son.
'''
num1 = int(input("Digite un número: "))
num2 = int(input("Digite otro número: "))

if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares")
elif num1%2==0 and num2%2==1:
    print("El primer numero es par y el otro es impar")
elif num1%2==1 and num2%2==0:
    print("El primer numero es impar y el otro es par")
else:
    print("Ambos número son impares")
'''
#EJERCICIO 2
#Hacer un programa que pida 3 números y determine cual es el mayor
'''
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
elif num3 >= num1 and num3 >= num2:
    print(f"El numero mayor es: {num3}")
'''
#EJERCICIO 3
#Hacer un programa que pida un carácter e indique si es una vocal o no
'''
caracter = input("Ingresa una letra: ")

if caracter=='a' or caracter=='e' or caracter=='i' or caracter=='o' or caracter=='u':
    print("El caracter ingresado corresponde a una vocal")
else:
    print("El caracter ingresado no corresponde a una vocal")
'''

#EJERCICIO 4
#Construir un programa que simule el funcionamiento de una
#calculadora que puede realizar las cuatro operaciones aritméticas
#básicas (suma, resta, multiplicacion y división). El usuarui debe
#especificar la operacion con el primer caracter del nombre de la operacion
'''
operacion = input("Ingrese la inicial de la operación que desea realizar:\n(Ej: S->suma)")
num1= int(input("Ingrese primer valor: "))
num2= int(input("Ingrese segundo valor: "))

if operacion == 's':
    print(f"El resultado es: {num1 + num2}")
if operacion == 'r':
    print(f"El resultado es: {num1 - num2}")
if operacion == 'd':
    print(f"El resultado es: {num1 / num2}")
if operacion == 'm':
    print(f"El resultado es: {num1 * num2}")
'''
#EJERCICIO 5
#Hacer un programa que simule un cajero automático con un saldo inicial
#de $1000 y tendrá el siguiente menú de opciones:

saldo = 1000

print("\t.:MENU:.")                        #Uso \t para tabular
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

opcion = int(input("Digite una opcion del menu: "))

if opcion==1:
    extra = float(input("¿Cuanto dinero desea ingresar?: "))
    saldo += extra
    print(f"Usted ha ingresado ${extra}")
    print(f"Su saldo actual es de: ${saldo}")               #Poner la f antes de la comilla!
elif opcion==2:
    retiro = float(input("¿Cuanto dinero desea retirar?: "))
    if retiro>saldo:  
        print("No fue posible realizar el retiro!")  
    else:
        saldo -= retiro
        print(f"Usted ha retirado $ {retiro}")
        print(f"Su saldo actual es de: ${saldo}")
elif opcion==3:
    print(f"Dinero disponible en la cuenta: ${saldo}")
elif opcion==4:
    print("Gracias por utilizar su cajero automático")
else:
    print("Opción inválida")
