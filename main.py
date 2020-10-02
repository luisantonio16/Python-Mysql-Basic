from conexionMySQL import connexionDB




#Funcion de menu principal.
def menu_principal():

     opcion = 0
     while opcion != 6:
         print('\tWELCOME AGENDA TELEFONICA\n')

         print('1.AGREGAR NUEVO CONTACTO.')
         print('2.MOSTRAR TODOS LOS CONTACTOS.')
         print('3.BUSCAR CONTACTO.')
         print('4.ACTUALIZAR CONTACTO.')
         print('5.ELIMINAR UN CONTACTO.')
         print('6.SALIR.')
         opcion = int(input("ELEGIR OPCION: "))
        
         
         print("\n")


         
         database = connexionDB()
         if opcion == 1:

             agregar = ""
             while agregar != "no":

                   
                     nombre = str(input('Digite su nombre: '))
                     telefono = str(input('Diga cual es su Telefono: '))
                     compañia =  str(input('Cual es la compañia de su telefono: '))
                     direccion = str(input('Cual es su direccion: '))

                     database.registro_repetido(nombre,telefono)
                     if database.registro_repetido (nombre,telefono) == 1:
                        return 2

                     else:
                         database.Agregar(id,nombre,telefono,compañia,direccion)

                     agregar = input("DESEA AGREGAR OTRO REGISTRO(SI/NO)?: ")
                     agregar.lower()
           
                 

         #opciones del menu
         elif opcion == 2:
             database.listar_contactos()
             print("\n")


         elif opcion == 3:
            codigoid= (input('introduzca el id del Registro que desea ver: '))
            print("\n")
            database.Mostrar(codigoid)


         elif opcion == 4:
             
                          
             idcod = input('Digita id del registro a Actualizar: ')
             database.Mostrar(idcod)
             print("\n")
             nombre = input(' Actualizar nombre: ')
             telefono = input(' Actualizar Telefono: ')
             
             
             database.Actualizar(nombre,telefono,idcod)
            


         elif opcion == 5:

             codigo = str(input('INTRODUZCA EL ID DEL REGISTRO: '))
             eliminar = database.Eliminar(codigo)
           
            
             print("\n")


         elif opcion == 6:
             print("Adios!!!")

         else:
             print("OPCION NO VALIDA!!!")

def precargar():
    database = connexionDB()
    print("bienvenidos a tu Agenda Telefonica, estos son los 10 contactos\n")
    database.welcome_registro()



precargar()
menu_principal()