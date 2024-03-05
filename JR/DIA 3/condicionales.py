"""#1 Cree un programa que ingresando un numero me diga si es mayor o menor de edad 

edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

"""
"""#2 Cree un programa que ingresando un numero me diga si es par o impar 

numero = int(input("Ingrese un numero"))
if numero % 2 == 0:
    print("El numero que ingresaste es par")
else:
    print("El numero ingrresado es impar")   
    

#3 Cree un programa que me reciba el nombre de una persona y su nota del curso si se 
#llama "pepito" y la nota es mayor a 3 imprima "Felicidades nombre aprobaste el curso"

nombre = input ("ingrese su nombre")
nota = float(input("Nota del curso"))"""


    
    
    
    # Calculadora basica, diseñar un diagrama de fujo para una calculadora basica
    #que pueda realizar operaciones de suma, resta, multiplicacion y division con dos numero 
    #dados por el usuario

"""numeroUno = int(input("Indique el primer numero: "))
numeroDos = int(input("indique el segundo numero: "))

suma = numeroUno + numeroDos
print("La suma de los valores que indico es:" ,suma)

resta = numeroUno - numeroDos
print("la resta de los valores es:" , resta)

multiplicacion = numeroUno * numeroDos
print("la multiplicacion de ambos numeros es:" , multiplicacion)

division = numeroUno / numeroDos
print("La division entre los valores dados es:" , division)"""


#Crear  un diagrama que flujo que convierta la temperatura de celsius a Fahrenheit y
# viceversa, segun la eleccion del usuario.
#Grados centigrados =(grados Fahrenheit - 32) * 5/9

opcion = int(input("""Ingrese 1 para convertir celsius a Fahrenheit 
o 2 para convertir de Fahrenheit a Celsius: """))

if opcion == 1:
    grados = float(input("Indique los grados celsius que desea convertir a Fahrenheit: ")) 
    gradosFahrenheit =(grados * 9/5) + 32
    print("Grados Fahrenheit: " , gradosFahrenheit )
    

elif opcion == 2: 
    grados = float(input("Indique los grados Fahrenheit que desea convertir a celsius"))
    gradosCelsius = (grados - 32) * 5/9
    print("Grados Celsius:" , gradosCelsius)
       
