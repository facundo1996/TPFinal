#! /usr/bin/env python3
import sys
from listaClientes import ListaClientes
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
class Menu:
    def __init__(self):
        self.rc = RepositorioClientes()
        self.rt = RepositorioTrabajos()
        self.lista_clientes = ListaClientes()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.modificar_particular,
            "4": self.modificar_corporativo,
            "5": self.borrar_cliente,
            "6": self.nuevo_trabajo,
            "0": self.salir
        }

    def mostrar_menu(self):
        print("""
Menu del sistema:
1. Mostrar todos los clientes
2. Agregar Nuevo Cliente
3. Modificar Cliente PARTICULAR
4. Modificar Cliente CORPORATIVO
5. Borrar cliente
6. Nuevo Trabajo
0. Salir
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
        for cliente in lista:
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
            print("Cliente cargado.")


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
            
        elif opcion == 2:
            nuevo_apellido = input("Ingrese el nuevo APELLIDO: ")
            obj_cliente.apellido = nuevo_apellido
            
        elif opcion == 3:
            nuevo_telefono = input("Ingrese el nuevo TELEFONO: ")
            obj_cliente.telefono = nuevo_telefono
            
        elif opcion == 4:
            nuevo_mail = input("Ingrese un nuevo MAIL: ")
            obj_cliente.mail = nuevo_mail
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
 
        elif opcion == 2:
            nuevo_nombre_contacto = input("Ingrese el nuevo NOMBRE DE CONTACTO:")
            obj_cliente.nombre_contacto = nuevo_nombre_contacto

        elif opcion == 3:
            nuevo_telefono_contacto = input("Ingrese el nuevo TELEFONO DE CONTACTO: ")
            obj_cliente.telefono_contacto = nuevo_telefono_contacto
            
        elif opcion == 4:
            nuevo_telefono = input("Ingrese el nuevo TELEFONO: ")
            obj_cliente.telefono = nuevo_telefono
            
        elif opcion == 5:
            nuevo_mail = input("Ingrese un nuevo MAIL: ")
            obj_cliente.mail = nuevo_mail

        elif opcion == 0:
            return
          
        self.rc.update(obj_cliente)
        self.lista_clientes = ListaClientes()       
        print("Cambio Exitoso:")
        print(obj_cliente)  


    def borrar_cliente(self):
        lista = self.lista_clientes.lista
        for id_lista in lista:
            print(id_lista)
            print("===========================================")
        id_elegido = int(input("Ingrese el ID del cliente que quiere eliminar: "))
        for id_lista in lista:
            if id_lista.id_cliente == id_elegido:
                cli = self.lista_clientes.rc.delete(id_lista)
                lista.remove(id_lista)
                print("Se elimino correctamente.")
                break;


    def nuevo_trabajo(self):
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
            print("Cliente cargado.")




    def salir(self):
        print("Saliste del programa. Gracias por todo.")
        sys.exit(0)


if __name__ == "__main__":
    m = Menu()
    m.ejecutar()
