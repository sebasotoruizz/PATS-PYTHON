#Tuplas
#Otro tipo de conjunto
#Son listas inmutables, es decir no podemos modificarlas
#Consumen menos memoria que las listas
#Mucho mas rapida su ejecucion

tupla = (4,"Hola",6.78,[1,2,3],4)

print(tupla)

#Podemos mostrar 1 solo elemento
tupla = (4,"Hola",6.78,[1,2,3],4)

print(tupla[1])

#Mostrar elementos desde un valor a otro
tupla = (4,"Hola",6.78,[1,2,3],4)

print(tupla[1:])

#Comprobar si un valor esta en la tupla
tupla = (4,"Hola",6.78,[1,2,3],4)

print(4 in tupla)

#Saber posicion de un valor
tupla = (4,"Hola",6.78,[1,2,3],4)

print(tupla.index(4))

#Saber cuantas veces hay un valor
tupla = (4,"Hola",6.78,[1,2,3],4)

print(tupla.count("Hola"))

#Indicar cuantos elementos tiene una tupla
tupla = (4,"Hola",6.78,[1,2,3],4)

print(len(tupla))

#Transformar Tupla a Lista
tupla = (4,"Hola",6.78,[1,2,3],4)
lista = list(tupla)

print(lista)
