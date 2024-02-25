#Operadores

#Operadores logicos 


#And "y"
condicionalAnd = False and True
print(condicionalAnd)

#Or "o"
condicionalOr = (1 < 2) or (12)
print(condicionalOr)

condicionalOr = not ((1 < 2) or (12 >= 2))
print(not condicionalOr)

#Not
CondicionalNot = not False
print(not CondicionalNot)

# ==  "Es igual"
esigual = "Jimena" == "jimena"
print(esigual)

# != "Diferente"
esDiferente = 12 != 12.0
print(esDiferente)

# > "Mayor que"
ComparadorNum = 1 > 2
print(ComparadorNum)

# < "Menor que"
comparadorNum = 5 < 8

# > = "Menor que o igual"
comparadorNum = 5 >= 3

# < = "Mayor o igual que"



"""Crear dos variabales numericas de cualquier tipo y
realizar las operaciones aritmetica basicas y almaacenar 
se resultado en una variable que se llame result e imprimir
en consola los resultados (+ - / // ** %)"""

#Declarar las 2 variables con valores numerico
numeroUno = 15
numeroDos = 2

result = numeroUno + numeroDos
print("La suma de los valores es:" ,result)

result = numeroUno - numeroDos
print("La resta de los valores es:" ,result)

result = numeroUno / numeroDos
print("La division de los valores es:" ,result)

result = numeroUno // numeroDos
print("La division aproximada de los valores es:" ,result)

result = numeroUno * numeroDos
print("La multiplicacionde los valores es:" ,result)

result = numeroUno ** numeroDos
print(f"la suma numeros es de: result")

result = numeroUno % numeroDos
print(f"""
      el modulo de la division 
      de{numeroUno} % {numeroDos} 
      es: {result}""")

#Ejercicios (escribe un programa que solicite al usuario ingresar dos numeros enteros y realice las siguierntes operaciones)
# Usar solo 2 variables


numeroUno = int(input("indique un numero entero: \n" ))
numeroDos = int(input("Indique un segundo numero entero: \n"))
print("Los numeros que usted indico son:" , numeroUno , "y", numeroDos)

#Realice una suma de los dos numeros
result = numeroUno + numeroDos
print("La suma de los valores es:" , result)

#Realice una resta del segundo numero al primero
result = numeroDos - numeroUno
print("la resta del segundo numero al primero es:" , result)

#Realice una multiplicacion de los numeros
result = numeroUno * numeroDos
print("la multiplicacion de ambos nu+meros es:" , result)

#Realice una divicion del primer numero entre el segundo
result = numeroUno / numeroDos
print("La division entre los valores dados es:" , result)

#Realice una division entera del segundo numero entre el primero

