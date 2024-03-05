# # Se crea una lista para telefonos y otra para contactos,asi sean diferentes listas 
# # contacto y telefono estaran referenciados por el mismo indice, es decir.
# # 
# ## def salario_Mensual():
# #     salario = float(input("Indica tu salario mensual"))
# #     return salario

# # salario = salario_Mensual()

# # #Se crean las categorias
# # alimentos = float(input("Indique sus gastos en alimentacion"))
# # transporte = float(input("indique sus gastos en transporte"))
# # vivienda = float(input("indique sus gastos en vivienda"))
# # entretenimiento = float(input("indique sus gastos en entretenimiento"))

# # #lista de categorias
# # categorias = [alimentos, transporte, vivienda,entretenimiento]

# # def gastos_mensuales(categorias):
# #     totalG = sum(categorias)
# #     return totalG

# # salActual = (salario) - (gastos_mensuales(categorias))
# # print(float(input(f"El saldo que le queda luego de sus gastos fijos es {salActual}")))
#  contacts=['Camilo','Laura']    phones=['123','456']   
# #               0       1                  0     1 
# #   -------->     ( Camilo-123 ) ( Laura-456 )  

# contacts=[]
# phones=[]

# # Creacion de un menu:-------------------------------------------------------------------------

# def menu(): # Esta funcion no necesita parametros ni retornar nada. Solo debe ser invocada para ser ejecutada: menu()
#  option=1
#  while (option != 5):
#     print("\n AGENDA DE CONTACTOS", " 1. Agregar contacto", " 2. Ver contactos"," 3. Buscar contacto"," 4. Eliminar contacto",
#           " 5. Salir" ,sep = "\n")
#     option=int(input("Que quieres hacer?: "))
#     if option==1:
#         apend(contacts,phones)
#     if option ==2:
#         see(contacts,phones)
#     if option ==3:
#         find(contacts,phones)
#     if option ==4:
#         delete(contacts,phones)        
#     if (option!=5) and (option>5):
#         print("La opcion ingresada no es valida, intentelo de nuevo")
#     if option==5:
#      print("El programa ha finalizado. Hasta pronto")
#      break
        
# # Funcion para agregar un contacto ingresado por el usuario---------------------------------------------

# def apend(contact,phone):
#     name=str(input('Ingrese el nombre del contacto: '))
#     phone_=str(input('Ingrese el numero de Tel/Cel: '))
#     contact.append(name)
#     phone.append(phone_)   
    
# # Funcion para ver toda la lista de contactos------------------------------------------------------------
    
# def see(contact,phone):
#     if len(contact)>0:
#         print("\nEsta es su lista de contactos:")
#         for x in range(len(contact)):  
#              print(f'{contact[x]}:{phone[x]}')
#     else: 
#         print('Aun no hay contactos.')

# # Funcion para encontrar un contacto dentro de la lista, y mostrarlo en pantalla-------------------------  
        
# def find(contact,phone):
#     if len(contact)==0:
#         print("Aun no hay contactos.")
#     else:
#         name=input(str('Ingrese el nombre del contacto: '))
#         for x in range(len(contact)):
#           if contact[x]==name:
#              print(f"{contact[x]}:{phone[x]}")
#         if (contact.count(name))==0: 
#               print('Este contacto no existe. Intenta con otro')    

# # Funcion para eliminar un contacto-----------------------------------------------------------

# def delete(contact,phone):    
#     if len(contact)==0:
#         print("Aun no hay contactos.")
#     else: 
#         name=input(str('Ingrese el nombre del contacto: '))
#         if contact.count(name)==0:
#             print('Este contacto no existe. Intenta con otro')

#                   # Analicen bien este cambio con respecto al anterior programa es mejor por metodos.
#                   # Ademas en el anterior no ejecutaba bien. 

#         else:     
#             index=contact.index(name)    
#             contact.pop(index)
#             phone.pop(index)
#             print('El contacto ha sido eliminado con exito.')
        
    

# # Ejecutar la funcion MENU construida al principio------------------------------------------------------------

# menu() 

# #---------------------------------!!! IMPORTANTE: VALIDACION DEL CODIGO !!!---------------------------------------#
# #
# # Hagan todas las validaciones pertinentes , es decir :
# #--> Primero ingresen una opcion invalida en el menu , prueben con numeros de 6 en adelate y de 0 hacia abajo, 
# #      debe arrojar que es una opcion invalida y debe volverlo a intentar.
# #--> Ejecuten y sin ingresar ningun Nombre ni Telefono las opciones (2,3,4) , debe arrojar que aun no hay contactos. 
# #--> Si van a buscar un contacto con la opcion 3 y no encuentra el nombre, debe decirle que no existe en la lista y que lo 
#       intente de nuevo. Y si esta en la lista, imprimirlo en pantalla junto con el telefono.
# #--> Si van a eliminar un contacto con la opcion 4 y no encuentra el nombre, debe decirle que no existe, que lo 
#       intente de nuevo. Y si esta en la lista, hacerle saber que ha sido  eliminado.
# #--> Por ultimo y no menos importante que salga del ciclo while cuando selcciono la opcion 5. Si observan en el menu la opcion 
#      5 , imprime un mensaje de despedida , e inmediatamente aparece la palabra "break" ;) 
