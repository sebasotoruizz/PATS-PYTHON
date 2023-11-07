#DICCIONARIOS
#Otro tipo de coleccion
#Elementos se guardan desordenados
#Tienen 2 elementos por posicion, la clave y el valor

diccionario = {"azul":"blue","rojo":"red","verde":"green"}

print(diccionario)

#Mostrar solo 1 elemento del diccionario
print(diccionario["azul"])
print(diccionario["rojo"])
print(diccionario["verde"])

#Agregar nuevos elementos al diccionario
diccionario["amarillo"] = "yellow"

print(diccionario)
#Modificar el valor de una clave
diccionario = {"azul":"blue","rojo":"red","verde":"green"}
diccionario["azul"] = "BLUE"
print(diccionario)

diccionario["azul"] = "blue"
print(diccionario)

#Eliminar elemento
diccionario = {"azul":"blue","rojo":"red","verde":"green"}
del(diccionario["verde"])

print(diccionario)

#CREAR AGENDA
diccionario = {"Sebastian":[22,1,80],"Alejandro":[22,1.73],"Jose":[21,1.75],"Maria":[22,1.67]}

#Coloque los datos dentro de una lista

print(diccionario)

#DICCIONARIO dentro de un DICCIONARIO
diccionario = {"Sebastian":{"edad":22,"estatura":1.80},"Alejandro":[22,1.73],"Jose":[21,1.75],"Maria":[22,1.67]}

print(diccionario["Sebastian"])

#Crear otro diccionario
equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",17:"Mario Mandzukic"}
print(equipo)

print(equipo.get(6,"no existe un jugador con ese dorsal"))

#Buscar dentro del diccionario
print(10 in equipo)
print(11 in equipo)
print(12 in equipo)

#Mostrar todas las claves del diccionario
print(equipo.keys())

#Mostrar todos los valores del diccionario
print(equipo.values())

#Poner Claves y Valores dentro de TUPLAS
print(equipo.items())

#Mostrar cuantos elementos hay en un diccionario
print(len(equipo))

#Vaciar diccionario
equipo.clear()
print(equipo)