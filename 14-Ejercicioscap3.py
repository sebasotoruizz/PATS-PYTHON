# EJERCICIO 1

#Escriba un programa donde tenga una lista y que, a 
#continuación, elkimine los elementos repetidos, por 
#último mostrar la lista.

lista = [1,2,3,"Sebastian",2,2,1,"Sebastian",3]

conjunto = set(lista)

lista = list(conjunto)

print(conjunto)

### Tambien se puede hacer de otra forma mas rápida
lista = [1,2,3,"Sebastian",2,2,1,"Sebastian",3]

lista = list(set(lista))

print(lista)


# EJERCICIO 2
#Escribe un programa que tenga dos listas y que, a continuación, cree las
#siguientes listas (en las que no debe haber repeticiones):

#-Lista de palabras qye aparecen en las dos listas
#-Lista de palabras que aparecen en la primera lista, pero no la segunda
#-Lista de palabras que aparecen en la segunda lista, pero no la primera
#-Lista de palabras que aparecen en ambas listas.

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

#Elimine los elementos repetidos de ambas listas

a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print(f"Lista de palabras qye aparecen en las dos listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no la segunda: {soloA}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no la primera: {soloB}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")

# EJERCICIO 3
#Escribe un programa donde cree una lista con los siguientes
#personakes del Señor de los anillos.

personajes = [] #Creando una lista vacia

p = {"Nombre":"Aragon","Clase":"Guerrero","Raza":"Dunadan del Norte"}
personajes.append(p) #Agregamos el personaje a la lista

p = {"Nombre":"Gandalf","Clase":"Mago","Raza":"Istar"}
personajes.append(p) #Agregamos el personaje a la lista

p = {"Nombre":"Leholas","Clase":"Arquero","Raza":"Elfo Sindar"}
personajes.append(p) #Agregamos el personaje a la lista

print(personajes)

#Hemos metido diccionarios dentro de una lista



