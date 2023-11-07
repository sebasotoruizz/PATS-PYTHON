#LISTAS
#Son parecidos a los arreglos o vectores
#Estructura de datos mas flexibles, pudiendo almacenar valores
#tipo numéricos, booleanos, cadenas, otras listas.

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

print(lista)

#Imprimir solo 1 elemento de la lista
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

print(lista[0])         #El orden dentro de la lista es 0,1,2,3,4
                        #Pero también puede ser -5,-4,-3,-2,-1

#Podemos usar sublistas
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

print(lista[0:3])       #Siempre poner un número más del valor al que quieres llegar

#Podemos almacenar cualquier dato en una lista
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.67,[1,2,3,],True]

print(lista)

#Determinar cuántos elementos tiene una lista
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.67,[1,2,3,],True]

print(len(lista))       

#Agregar un elemento al final
lista = [1,2,3,4,5]
lista.append(6)
lista.append("Sebastian")

print(lista)

#Agregar un elemento en algun lugar especifico
lista = [1,2,4,5]
lista.insert(2,3)   #dentro del parentesis (posicion a ocupar,valor a introducir a la lista)

print(lista)

#Agregar varios elementos
lista = [1,2,3,4,5]
lista.extend([6,7,8])
print(lista)

#Sumar 2 listas
lista1 = [1,2,3,4,5]
lista2 = [6,7,8]

lista3= lista1 + lista2
print(lista3)

#Buscar un determinado elemento en la lista
lista = [1,2,3,4,5,"Sebastian"]

print(3 in lista)

#Saber en que índice se encuentra un elemento
lista = [1,2,3,4,5,"Sebastian"]

print(lista.index(5))

#Saber cuantos valores repetidos existen
lista = [1,2,3,4,5,"Sebastian",1,2,3,1,"Sebastian",1]

print(lista.count(1))

#Eliminar valor en una lista por posicion
lista = [1,2,3,4,5,"Sebastian"]
lista.pop(3)                     #si pongo el () vacio me elimina el ultimo valor
print(lista)

#Eliminar un valor en la lista por valor
lista = [1,2,3,4,5,"Sebastian"]
lista.remove(3)                     
print(lista)

#Vaciar una lista
lista = [1,2,3,4,5,"Sebastian"]
lista.clear()

print(lista)

#Voltear una lista
lista = [1,2,3,4,5,"Sebastian"]
lista.reverse()

print(lista)

#Copiar cada elemento 2 veces
lista = [1,2,3,4,5,"Sebastian"] *2

print(lista)

#Ordenar los elementos de una lista
lista = [5,4,-7,9,0,1,3]
lista.sort(reverse=True)    #Se ordena de mayor a menor
print(lista)

#Transformar Lista a Tupla
lista = [1,2,3,4,5,"Sebastian"]
tupla = tuple(lista)

print(tupla)