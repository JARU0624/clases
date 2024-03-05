#Programa para calcular la edad de una persona ingresando su año de nacimiento.
#1. Se solicitará al usuario el año de nacimiento


# fechaNacimiento = int(input("Indica tu fecha de nacimiento"))
# edad = 2024 - fechaNacimiento
# print(f"Tu tienes {edad} años")

 
 #Seguimiento de in gresos y gastos 
# Tarea 1
#Solicitued de salario 

def salario_Mensual():
    salario = float(input("Indica tu salario mensual"))
    return salario

salario = salario_Mensual()

#Se crean las categorias
alimentos = float(input("Indique sus gastos en alimentacion"))
transporte = float(input("indique sus gastos en transporte"))
vivienda = float(input("indique sus gastos en vivienda"))
entretenimiento = float(input("indique sus gastos en entretenimiento"))

#lista de categorias
categorias = [alimentos, transporte, vivienda,entretenimiento]



while True:

    new_gasto =int(input("Ingrese 1 para agregar un nuevo gasto y 0 para no agregar nada:"))
    if new_gasto == 0:
        break

    new_costo = int(input("ingrese un nuevo gasto"))
    opcion = int(input("seleccione la categoria\n 1.Alimentos\n 2.Transporte\n 3.Vivienda\n 4.Entretenimiento "))
    
    if opcion == 1:
        categorias[0] += new_costo

    elif opcion == 2:
        categorias[1]+= new_costo

    else:
        print("Este valor no pertenece a ninguna categoria")
        continue
            


def gastos_mensuales(categorias):
    totalG = sum(categorias)
    return totalG

salActual = (salario) - (gastos_mensuales(categorias))
print(float(input(f"El saldo que le queda luego de sus gastos es {salActual}")))





