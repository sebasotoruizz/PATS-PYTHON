#PILAS
#Estructura de datos 
#No existe en Python pero podemos
#simularlas con las listas

pila = [1,2,3]

print(pila)

#Agregar elemento a la Pila
pila.append(4)
pila.append(5)

print(pila)

#Sacar elemento de una Pila
'''
pila.pop()

print(pila)
'''
#.pop() tambien te retorna los elementos para que puedas guardarlos
n = pila.pop()
print(f"Sacando el elemento {n}")

n = pila.pop()
print(f"Sacando el elemento {n}")

print(pila)


