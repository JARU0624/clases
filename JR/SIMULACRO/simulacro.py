# Crea un programa que permita a un usuario gestionar una agenda de contactos. El programa debe permitir al usuario realizar las siguientes acciones:
#     • Agregar un nuevo contacto con nombre y número de teléfono.
#     • Ver la lista de contactos existentes.
#     • Buscar un contacto por nombre y mostrar su número de teléfono.
#     • Eliminar un contacto por nombre.
# Instrucciones:
#     • Inicializar una lista vacía para almacenar los contactos.
#     • Crear un menú que ofrezca las opciones de agregar, ver, buscar y eliminar contactos, así como salir del programa.
#     • Para agregar un contacto, solicitar al usuario el nombre y el número de teléfono y agregarlos a la lista de contactos.
#     • Para ver la lista de contactos, mostrar todos los nombres y números de teléfono.
#     • Para buscar un contacto, solicitar al usuario el nombre y mostrar su número de teléfono si existe en la lista de contactos.
#     • Para eliminar un contacto, solicitar al usuario el nombre y eliminarlo de la lista de contactos.
#     • Repetir el menú hasta que el usuario elija salir del programa.



listaContactos = []
#Menu de opciones

opcion1 = str(input('seleccione la opcion "ver" Si desea visulizar sus contactos:\n'))
opcion2 = str(input('seleccione la opcion "buscar" para buscar a alguien entre sus contactos:\n'))
opcion3 = str(input('seleccione "eliminar" para borrar de su lista alguno de sus contactos:\n'))
opcion4 = str(input('seleccione "agregar" para agregar un amigo mas a tus contactos:\n'))
opcion5 = str(input('Seleccione "salir" si desea cerrar su lista de cotactor seleccione:\n'))

if opcion4 == "agregar":
    agregarContacto = int(input("Indique el nombre y numero de celular que desea agregar: \n "))
    nuevoContacto = (agregarContacto) ,  listaContactos.insert
    print("Su nuevo contacto es:" , nuevoContacto)

elif opcion1 == "ver":
    visualizar = print(listaContactos)
    
elif opcion2 == "buscar":
    print(str("Indique el nombre del contacto que desea agregar:\n") (listaContactos[1]))

elif opcion3 == "eliminar":
     borrar = str(input("Indique el nombre del contacto que desea eliminar: \n"))
     nombreaEliminar = (listaContactos.remove)
     
