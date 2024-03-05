"""Ejercicio 3"""

#Tarea 1

# listaEmpleados = [
#     ["antony" ,10],
#     ["david",2]] 

# listaNombre = ["antony" , "david"]
listaAñosIng = [10, 2, 1, 3, 0]
contadorIng = 0
for yearIng in listaAñosIng:
    if yearIng > 2:
        # contadorIng = contadorIng +1

print(f"La suma de los ing con +2 años : {yearIng}")


#For son ciclos que tiene definidas la cantidad 
#de repeticiones que va hacer 

# En python :
#for "cadeElemento" in [listaElementos]
#Una respeticion 
        


# Tarea 2 
#Gastos = float(input("Dime los gastos"))
#presupuesto = float(input("Dime el presupuesto"))

presupuesto = 2000000
gastos = 1000000
#restante = presuesto - gastos (Buena practica)
print(presupuesto - gastos) #aqui se cumple con lo que piden
print(f"El restante : {restante}") #el deber ser la variable se mete en llaves 
#cuando se utiliza la f


#Tarea 3

duracionViaje = 2 #dias 
consumoHora = 10 #galones 
#essta info se le puede pedir al usurio 
#pero no especificaron eso 

combustible = consumoHora * (duracionViaje * 24)
print(combustible)

# tarea 4
duracionViaje = 12
