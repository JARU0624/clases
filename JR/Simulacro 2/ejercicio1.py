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




# # Programa para realizar factuacion con nombre, cedula, lista productos
# y valor de los productos

# Listas vacias para almacenar la informacion
nombres=["Kathe","Laura","James"]
documentos=["123","456","789"]
productos=["Colgate","Empanadas","Quesito","Arepas","Condones"]
precios=[5000,6000,10000,3000,50000]

# Creamos una funcion para ejecutar el programa------------------------

def menu():
    registrarND(nombres,documentos)
    op=1
    while(op!=5):
        print("""
              FACTURACION:
               1. Registrar nombre y documento
               2. Registrar productos
               3. Lista actual de productos
               4. Generar facturar
               5. Salir del programa
               """)                     
        op=int(input("Que desea hacer?: "))
        if (op==1):
            registrarND(nombres,documentos)
        if (op==2):
            registrarP(productos,precios)           
        if (op==3):
            listaP(productos,precios)
        if (op==4):
            factura(nombres,documentos,productos,precios)
        if (1>op>5):
            print("La opcion no es valida, intente de nuevo.")
        if (op==5):
            print("\nHasta pronto! ")
            break
            
def registrarND(nombre,documento):
    name=str(input("Ingrese nombre usuario: "))
    id=str(input("Ingrese documento usuario: "))
    nombre.append(name)
    documento.append(id)

def registrarP(producto,precio):
    articulo=str(input("Ingrese producto: "))
    valor=int(input("Ingrese precio del producto: "))
    producto.append(articulo)
    precio.append(valor)
    
def listaP(producto,precio):
    print("\nSu lista de productos hasta el momento es: ")
    for x in range(len(producto)):
        print(f"{producto[x]} : {precio[x]}")

def factura(nombre,documento,producto,precio):
    for x in precio:
        x+=x
    total=x
    totalIVA=total*1.19 
    items=len(precio) # contar productos
    if (items>=3 and items<5):
       descuento=str(totalIVA*1.05)
       mensaje="Su descuento es de: "
    if (items>=5 and items<7):
       descuento=str(totalIVA*1.10)
       mensaje="Su descuento es de: "
    if (items>7):
       descuento="No hay"
       mensaje="Tienes un bono por 100000"
    if (items==1 and total>500000):
       descuento="No hay"
       mensaje="Felicidades no pagas IVA"
       totalIVA=total
    
    name=input("Ingrese el nombre del usuario:") 
    indice=nombre.index(name)
    print(f"""  Nombre:{name[indice]}
                C.C:{documento[indice]}                  
          """)
    print(" Producto : Valor" )
    for x in range(len(producto)):
        print(f"{producto[x]}:{precio[x]}")
    print(f"TOTAL SIN IVA: {total}")
    print(f"TOTAL CON IVA: {totalIVA}")
    print(f"{mensaje}{descuento}")

    
menu()




