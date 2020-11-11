#! /usr/bin/env python3
from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes

class ListaClientes:
	def __init__(self):
		self.rc = RepositorioClientes()
		lista_clientes = self.rc.get_all()

	def mostrar_clientes(self, lista = None):
		if lista == None:
			lista = self.lista_clientes
		for cliente in lista:
			print(cliente)
			print("===========================================")

		def nuevo_cliente_corporativo(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail):
			c = ClienteCorporativo(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail)
			c.id_cliente = self.rc.store(c)
			if c.id_cliente == 0:
				return False
			else:
				self.lista_clientes.append(c)
				return c

		def nuevo_cliente_partiular(self, nombre, apellido, telefono, mail):
			c = ClienteParticular(nombre, apellido, telefono, mail)
			c.id_cliente = self.rc.store(c)
			if c.id_cliente == 0:
				return False
			else:
				self.lista_clientes.append(c)
				return c