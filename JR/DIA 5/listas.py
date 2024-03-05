# lista = ["Jimena" , int (21) , False , "Fememneino" ,[0,12,7]] 
# print(lista[0])
# print(lista[3])

# lista [3] = 3209326136
# print(lista)


#CREAR LISTA

# #SENCILLA
# lista1 = [1,2,3 "Hola", True]

# entero = 12
# flotante = 12.3 
# texto = "Adios" 
# boleano = False 

# listainterna = ["Estoy dentro" , True]
#con variables

# lista2 = [entero, flotante, texto,boleano, listainterna] 
# print(lista2)

""""Buscar dentro de una lista"""
#un solo indice 
# # print(lista1[1])
# print(lista2[2])
# print(lista2[9]) "esta fuera del rango"
# print(lista1[-4])


""""Modificar una lista"""
#Un solo indice
# lista1[-1] = 123456789
# print(lista1)

#Un bloque o rango de posiciones[:l
# lista1[1:3] = 12,2,5,5,6
# print(lista1)

# lista1[0:4] = [12]
# lista1 = []
# print(lista1)

# """Agregar a una lista"""
# .insert(indice, valor)
# lista2.insert(0, "Me modificaron")
# lista2.insert(0 , listainterna)
# print(lista2)

# .append(Valor)
# lista2.append(listainterna)

# """Unir 2 listas"""
# #. extend
# lista1.extend(lista2)
# lista2.extend(lista1)
# lista1.extend(lista1)
# print(lista1)

# Para agregar algo a la lista al final
# lista1.append("Hola")
# print(lista1)

# """Borrar elementos de una lista"""
#remove()
# lista.remove("Hola")
# lista.remove("Hola")
# lista.remove("Hola")
# lista.remove("Hola")
# print(lista1)

#remove
# lista3 =[12,1,1,2,[1,2,[1,2]]]
# print(lista3)
# print(lista3[4])
# lista3[4][2].remove(1)
# print(lista3[4][2])

# lista3[4].remove(1)
# lista3.remove(1)
# lista3.remove(1)
# print(lista3)

#Clear
# lista3.clear()
# print(lista3)

#pop() elimina la ultima posicion
# print(lista3)
# lista3.pop()
# print(lista3)
# lista3.pop(0)
# print(lista3)

"""organizar elementos de una lista"""
"""Como organizar una lista que tenga numeros
y letras dandole prioridad a los numeros y despues a las letras"""

# .sort()
"""Investigar"""
#.count()
#.find()
#.index
#.reverse()

#Ejercicios de lista 
#Hacerlo con civclo for o ciclo while, y luego buscar si hay algun metodo
#que lo haga

# Suma de elementos
#Escribe una funcion que tome una lista de numeros y devuelva la suma de todos los elementos 


# suma = 0
# lista = [11,12,13,14]
# for i in lista:
#     suma = suma + i 
# print("La suma de todos los elementos es" , [suma])

# #Multiplicacion de elementos: 
# #EScribe una multiplicacion que tomr una lista de numeros y devuelva 
# #el producto de todos los elementos 

# multiplicacion = 2
# lista = [1,2,6,8,2]
# for x in  lista:
#     multiplicacion = multiplicacion * x
# print("La multiplicacion de los valores es" , multiplicacion)

#3 Inversion de lista 
#Escribe una funcion que invierta una lista dada con un ciclo

# lista1 = [1,2,3,4,5,6]

# lista1.reverse()
# print(f"\nlista1: {lista1}")



# lista4 = [3,-2,1,-1,0,4]
# numeros = (len(lista4)-1)
# for x in range (numeros-1,-1,-1):
#     print(lista4[x])


#     listaNormal = [1,"Hola" , "Soy" , True ,-1, "hola"]:
#     ListaInvertida = [1]

# for posicion in range(len(listaNormal)-1,-1-1):
#     ListaInvertida.append(listaNormal[posicion])

#     print(listaNormal)
