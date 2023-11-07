#Conjuntos
#Tipo de coleccion donde los elementos se agregan de forma desordenada
#Principal caracteristica es que no pueden haber duplicados
#No puede haber otro tipo de coleccion dentro
#No pueden haber elementos repetidos

conjunto = set()            #Esta linea es obligatoria para diferenciar el conjunto del diccionario
conjunto = {1,2,3,"Hola",4.56}
                            
print(conjunto)

#Agregar elemento al conjunto
conjunto = set()         
conjunto = {1,2,3,"Hola",4.56}

conjunto.add(5)
conjunto.add("Adios")
conjunto.add('a')

print(conjunto)

#Eliminar elemento de un conjunto
conjunto = set()         
conjunto = {1,2,3,"Hola",4.56}

conjunto.discard(3)

print(conjunto)

#Vaciar todo el conjunto
conjunto = set()         
conjunto = {1,2,3,"Hola",4.56}

conjunto.clear()
print(conjunto)

#Buscar determinado elemento
conjunto = set()         
conjunto = {1,2,3,"Hola",4.56}

print(1 in conjunto)
print(12 in conjunto)
print(3 not in conjunto)

#SI DESDE UN INICIO LE VOY A PONER VALORES AL CONJUNTO
#NO ES NECESARIO ESCRIBIR PRIMERO EL a = set()

a = {1,2,3}
b = {3,4,5}

#Preguntar si 2 conjuntos son iguales
print(a==b)

#Saber cuantos elementos tiene
print(len(a))
print(len(b))

#Unir Conjuntos
a = {1,2,3}
b = {3,4,5}

c= a | b
print(c)

#Interseccion en Conjuntos, mostrar elementos en comun.
a = {1,2,3}
b = {3,4,5}

c = a & b
print(c)

#Diferencia, elementos de a que no esten en b.
a = {1,2,3}
b = {3,4,5}

c = a - b
print(c)

#Diferencia Simetrica
a = {1,2,3}
b = {3,4,5}

c = a ^ b
print(c)

#Determinar si un conjunto, es subconjunto de otro
a = {1,2,3}
b = {3,4,5}
c = {1,2,3,4,5}

print(a.issubset(c))

#Determinar si un conjunto, es superconjunto de otro
a = {1,2,3}
b = {3,4,5}
c = {1,2,3,4,5}

print(c.issuperset(a))

#Saber si ambos conjuntos son disconexos, osea no comparten ningun elemento en común
#Determinar si un conjunto, es subconjunto de otro
a = {1,2,3}
b = {3,4,5}
c = {1,2,3,4,5}

print(a.isdisjoint(b))

#Hacerlos Inmutables
a = frozenset({1,2,3})
b = {3,4,5}

a.add(3)        #No podre usar, ya que ahora el conjunto a es inmutable

print(a)