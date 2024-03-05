# Prueba 1:
    
# Enunciado: Agenda de Contactos

# Descripción del problema: 
    
# Crea un programa que permita a un usuario gestionar una agenda de contactos. 
# El programa debe permitir al usuario realizar las siguientes acciones:    
# •	Agregar un nuevo contacto con nombre y número de teléfono.
# •	Ver la lista de contactos existentes.
# •	Buscar un contacto por nombre y mostrar su número de teléfono.
# •	Eliminar un contacto por nombre.

# Instrucciones:
# •	Inicializar una lista vacía para almacenar los contactos.
# •	Crear un menú que ofrezca las opciones de agregar, ver, buscar y eliminar contactos, así como 
#     salir del programa.
# •	Para agregar un contacto, solicitar al usuario el nombre y el número de teléfono y agregarlos a 
#     la lista de contactos.
# •	Para ver la lista de contactos, mostrar todos los nombres y números de teléfono.
# •	Para buscar un contacto, solicitar al usuario el nombre y mostrar su número de teléfono si existe 
#     en la lista de contactos.
# •	Para eliminar un contacto, solicitar al usuario el nombre y eliminarlo de la lista de contactos.
# •	Repetir el menú hasta que el usuario elija salir del programa. 

#------------------------------------------------------------------------------------------------------

# Se crea una lista para telefonos y otra para contactos, ambos con el mismo indice.

contacts=[]
phones=[]

# Funcion para agregar un contacto ingresado por el usuario---------------------------------------------

def apend(contact,phone):
    name=str(input('Ingrese el nombre del usuario: '))
    phone_=str(input('Ingrese el numero de Tel/Cel: '))
    contact.append(name)
    phone.append(phone_)   
    
# Funcion para ver toda la lista de contactos------------------------------------------------------------
    
def see(contact,phone):
    if len(contact)>0:
        print("\nEsta es su lista de contactos:")
        for x in range(len(contact)):
             print(f'{contact[x]}:{phone[x]}')
    else: 
        print('Aun no hay contactos')

# Funcion para encontrar un contacto dentro de la lista, y mostrarlo en pantalla-------------------------  
        
def find(contact,phone):
    if len(contact)==0:
        print("Aun no hay contactos")
    else:
        name=input(str('Ingrese el nombre del contacto: '))
        for x in range(len(contact)):
          if contact[x]==name:
             print(f"{contact[x]}:{phone[x]}")
    

# Funcion para eliminar un contacto-----------------------------------------------------------

def delete(contact,phone):    
    if len(contact)==0:
        print("Aun no hay contactos")
    else:
        name=input(str('Ingrese el nombre del contacto: '))
        for x in range(len(contact)):
          if contact[x]==name:
             contact.remove(contact[x])
             phone.remove(phone[x])
        else: print("El contacto no existe")
    
# Creacion de un menu:-------------------------------------------------------------------------

def menu(): 
 option=1
 while (option != 5):
    print("\n AGENDA DE CONTACTOS", " 1. Agregar contacto", " 2. Ver contactos"," 3. Buscar contacto"," 4. Eliminar contacto",
          " 5. Salir" ,sep = "\n")
    option=int(input("Que quieres hacer?: "))
    if option==1:
        apend(contacts,phones)
    if option ==2:
        see(contacts,phones)
    if option ==3:
        find(contacts,phones)
    if option ==4:
        delete(contacts,phones)        
    if (option!=5) and (option>5):
        print("La opcion ingresada no es valida, intentelo de nuevo")
    if option==5:
     print("El programa ha finalizado. Hasta pronto")
     break
        
# Ejecutar el programa------------------------------------------------------------

menu()