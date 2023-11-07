#COLAS
#Estructura de datos tipo fifo
#Es decir First Input First Output (Primero en entrar, Primero en salir)

cola = ["Maria","Alejandro","Mario"]

print(cola)

#Agregar element0 al final de la cola
cola.append("Karla")
cola.append("Flor")

print(cola)

#Sacando elementos por el principio de la cola
'''
cola.pop(0)

print(cola)
'''
#Recordemos que .pop() ademas de sacar el valor tambien te entrega el valor
n = cola.pop(0)
print(f"Atendiendo a {n}")

n = cola.pop(0)
print(f"Atendiendo a {n}")

print(cola)



