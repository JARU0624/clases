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


