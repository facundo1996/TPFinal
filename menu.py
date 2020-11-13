#! /usr/bin/env python3
import sys
from listaClientes import ListaClientes
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
from lista_trabajo import Lista_Trabajo
import datetime

class Menu:
    def __init__(self):
        self.rc = RepositorioClientes()
        self.rt = RepositorioTrabajos()
        self.lista_trabajo = Lista_Trabajo()
        self.lista_clientes = ListaClientes()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.modificar_particular,
            "4": self.modificar_corporativo,
            "5": self.borrar_cliente,
            "6": self.mostrar_trabajos,
            "7": self.nuevo_trabajo,
            "8": self.trabajo_finalizado,
            "9": self.trabajo_retirado,
            "10": self.modificar_trabajo,
            "11": self.mostrar_no_retirados,
            "12": self.eliminar_trabajo,
            "0": self.salir
        }

    def mostrar_menu(self):
        print("""
_________________________________________________
|Menu del sistema:                               |
|1. Mostrar todos los clientes                   |
|2. Agregar Nuevo Cliente                        |
|3. Modificar Cliente PARTICULAR                 |
|4. Modificar Cliente CORPORATIVO                |
|5. Borrar cliente                               |
|6. Mostrar Trabajos                             |
|7. Nuevo Trabajo                                |
|8. Finalizar Trabajo                            |
|9. Marcar trabajo como retirado                 |
|10. Modificar Trabajo                           |
|11. Mostrar trabajos finalizados no retirados   |
|12. Eliminar Trabajo                            |
|0. Salir                                        |
|________________________________________________|
""")

    def ejecutar(self):
        '''Mostrar el menu y responder las opciones'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese una opcion: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opcion valida".format(opcion))


    def mostrar_clientes(self, lista = None):
        if lista == None:
            lista = self.lista_clientes.lista
        print("Clientes: ")
        for cliente in lista:
            print("===========================================")
            print(cliente)
            print("===========================================")


    def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C:corporativo / P:Particular:  ")
        nombre = input("Ingrese el nombre: ")
        if tipo in ("C", "c"):
            contacto = input("ingrese el nombre del contacto: ")
            tc = input("ingrese el telefono del contacto: ")
        else:
            apellido = input("Ingrese el apellido: ")
        tel = input("Ingrese el Telefono: ")
        mail = input("Ingrese el Mail: ")

        if tipo in ("c", "C"):
            c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto, tc, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)
        if c is None:
            print("Error al cargar el cliente.")
        else:
            print("Cliente cargado con exito.")


    def modificar_particular(self):
        print("Modificar cliente Particular: ")
        id_cliente = int(input("Ingresa id de un Particular: "))
        obj_cliente = self.rc.get_one_particular(id_cliente)
        print(obj_cliente)
        opcion = int(input(""""Elige una opcion para modificar: 
                            1. Nombre
                            2. Apellido
                            3. Teléfono
                            4. Mail
                            0. Salir
                            : """))
        if opcion == 1:
            nuevo_nombre = input("Ingrese el nuevo NOMBRE:")
            obj_cliente.nombre = nuevo_nombre
            print("Nombre cambiado con exito.")
            
        elif opcion == 2:
            nuevo_apellido = input("Ingrese el nuevo APELLIDO: ")
            obj_cliente.apellido = nuevo_apellido
            print("Apellido cambiado con exito.")
            
        elif opcion == 3:
            nuevo_telefono = input("Ingrese el nuevo TELEFONO: ")
            obj_cliente.telefono = nuevo_telefono
            print("Telefono cambiado con exito.")
            
        elif opcion == 4:
            nuevo_mail = input("Ingrese un nuevo MAIL: ")
            obj_cliente.mail = nuevo_mail
            print("Mail cambiado con exito.")
        elif opcion == 0:
            return
        self.rc.update(obj_cliente)
        self.lista_clientes = ListaClientes()

    def modificar_corporativo(self):
        print("Modificar cliente Corporativo: ")
        id_cliente = int(input("Ingresa id de un Corporativo: "))
        obj_cliente = self.rc.get_one_corporativo(id_cliente)
        print(obj_cliente)
        opcion = int(input(""""Elige una opcion para modificar: 
                            1. Nombre empresa
                            2. Nombre contacto
                            3. Teléfono de contacto
                            4. Telefono
                            5. Mail
                            0. Salir
                            : """))
        if opcion == 1:
            nuevo_nombre_empresa = input("Ingrese el nuevo NOMBRE DE LA EMPRESA:")
            obj_cliente.nombre_empresa = nuevo_nombre_empresa
            print("Nombre de empresa cambiado con exito.")
 
        elif opcion == 2:
            nuevo_nombre_contacto = input("Ingrese el nuevo NOMBRE DE CONTACTO:")
            obj_cliente.nombre_contacto = nuevo_nombre_contacto
            print("Nombre de contacto cambiado con exito.")

        elif opcion == 3:
            nuevo_telefono_contacto = input("Ingrese el nuevo TELEFONO DE CONTACTO: ")
            obj_cliente.telefono_contacto = nuevo_telefono_contacto
            print("Telefono de contacto cambiado con exito.")
            
        elif opcion == 4:
            nuevo_telefono = input("Ingrese el nuevo TELEFONO: ")
            obj_cliente.telefono = nuevo_telefono
            print("Telefono cambiado con exito.")
            
        elif opcion == 5:
            nuevo_mail = input("Ingrese un nuevo MAIL: ")
            obj_cliente.mail = nuevo_mail
            print("Mail cambiado con exito.")

        elif opcion == 0:
            return
          
        self.rc.update(obj_cliente)
        self.lista_clientes = ListaClientes()       
        print("Cambio Exitoso:")
        print(obj_cliente)  


    def borrar_cliente(self):
        lista = self.lista_clientes.lista
        for id_lista in lista:
            print("==================================================================")
            print(id_lista)
            print("==================================================================")
        id_elegido = int(input("Ingrese el ID del cliente que quiere eliminar: "))
        for id_lista in lista:
            if id_lista.id_cliente == id_elegido:
                cli = self.lista_clientes.rc.delete(id_lista)
                lista.remove(id_lista)
                print("Se elimino correctamente.")
                break;


    def mostrar_trabajos(self, lista = None):
        if lista == None:
            lista = self.lista_trabajo.lista
        for trabajo in lista:
            print("====================================================")
            print("Cliente: ")
            print(trabajo.cliente)
            print("Trabajo: ")
            print("ID: ", trabajo.id_trabajo)
            print("Fecha de entrega: ", trabajo.fecha_entrega_propuesta)
            print("Fecha de entrega real: ", trabajo.fecha_entrega_real)
            print("Descripcion: ", trabajo.descripcion)
            print("Retirado: ", trabajo.retirado)
            print("====================================================")


    def nuevo_trabajo(self):
        obj_cliente = None
        while True:
            cliente = input("Ingrese el id del cliente: ")
            obj_cliente = self.rc.get_one(cliente)
            if obj_cliente != None:
                print(obj_cliente)
                break;

        fecha_ingreso = datetime.date.today()
        while True:
            try:
                f = input("Ingrese la fecha propuesta (aaaa,mm,dd): ")
                fecha_propuesta = datetime.datetime.strptime(f, "%Y,%m,%d")
            except ValueError:
                print("Fecha no valida")
                continue
            break
        fecha_entrega_real = None
        descripcion = input("Ingrese la descripcion del trabajo: ")
        retirado = False


        nt = Trabajo(obj_cliente, fecha_ingreso, fecha_propuesta, fecha_entrega_real, descripcion, retirado, None)
        resultado = self.rt.store(nt)
        self.lista_Trabajo = self.rt.get_all()

        print("Trabajo guardado exitosamente. Con el id ", resultado)

    def trabajo_finalizado(self):
        print("Finalizar trabajo: ")
        id_trabajo = int(input("Ingresa id del trabajo: "))
        obj_trabajo = self.rt.get_one(id_trabajo)
        
        obj_trabajo.fecha_entrega_real = datetime.date.today()
        print("")
        print("Trabajo finalizado con exito: ")
        print("")
        print("==============================================")
        print("ID: ", obj_trabajo.id_trabajo)
        print("Fecha de entrega: ", obj_trabajo.fecha_entrega_propuesta)
        print("Fecha de entrega real: ", obj_trabajo.fecha_entrega_real)
        print("Descripcion: ", obj_trabajo.descripcion)
        print("Retirado: ", obj_trabajo.retirado)
        print("==============================================")

        self.rt.update(obj_trabajo)
        self.lista_trabajo = Lista_Trabajo()     

    def trabajo_retirado(self):
        print("Marcar trabajo retirado : ")
        id_trabajo = int(input("Ingresa id del trabajo: "))
        obj_trabajo = self.rt.get_one(id_trabajo)
        
        obj_trabajo.retirado = True
        print("")
        print("Trabajo retirado con exito: ")
        print("")
        print("==============================================")
        print("ID: ", obj_trabajo.id_trabajo)
        print("Fecha de entrega: ", obj_trabajo.fecha_entrega_propuesta)
        print("Fecha de entrega real: ", obj_trabajo.fecha_entrega_real)
        print("Descripcion: ", obj_trabajo.descripcion)
        print("Retirado: ", obj_trabajo.retirado)
        print("==============================================")           

        self.rt.update(obj_trabajo)
        self.lista_trabajo = Lista_Trabajo()     


    def modificar_trabajo(self):
        print("Modificar trabajo : ")
        id_trabajo = int(input("Ingresa id del trabajo: "))
        obj_trabajo = self.rt.get_one(id_trabajo)

        while True:
            try:
                f = input("Ingrese la nueva fecha propuesta (aaaa,mm,dd): ")
                fecha_propuesta = datetime.datetime.strptime(f, "%Y,%m,%d")
            except ValueError:
                print("Fecha no valida")
                continue
            break
        descripcion = input("Ingrese la nueva descripcion del trabajo: ")

        obj_trabajo.fecha_entrega_propuesta = fecha_propuesta
        obj_trabajo.descripcion = descripcion

        print("")
        print("Trabajo modificado con exito: ")
        print("")
        print("==============================================")
        print("ID: ", obj_trabajo.id_trabajo)
        print("Fecha de entrega: ", obj_trabajo.fecha_entrega_propuesta)
        print("Fecha de entrega real: ", obj_trabajo.fecha_entrega_real)
        print("Descripcion: ", obj_trabajo.descripcion)
        print("Retirado: ", obj_trabajo.retirado)
        print("==============================================")           

        self.rt.update(obj_trabajo)
        self.lista_trabajo = Lista_Trabajo()

    def mostrar_no_retirados(self, lista = None):
        if lista == None:
            lista = self.lista_trabajo.lista
        for trabajo in lista:
            if trabajo.retirado == False and trabajo.fecha_entrega_real != None:
                print("===========================================")
                print("Cliente: ")
                print(trabajo.cliente)
                print("ID: ", trabajo.id_trabajo)
                print("Fecha de entrega: ", trabajo.fecha_entrega_propuesta)
                print("Fecha de entrega real: ", trabajo.fecha_entrega_real)
                print("Descripcion: ", trabajo.descripcion)
                print("Retirado: ", trabajo.retirado)
                print("===========================================")


    def eliminar_trabajo(self):
        id_elegido = int(input("Ingrese el ID del trabajo que quiere eliminar: "))
        obj_trabajo = self.rt.get_one(id_elegido)
        resultado = self.rt.delete(obj_trabajo)
        self.lista_trabajo = Lista_Trabajo()
        print("Eliminado: ", resultado)


    def salir(self):
        print("Saliste del programa. Gracias por todo.")
        sys.exit(0)


if __name__ == "__main__":
    m = Menu()
    m.ejecutar()
