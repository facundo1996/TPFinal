#! /usr/bin/python3
from trabajo import Trabajo
from repositorioTrabajos import RepositorioTrabajos
import datetime

class Lista_Trabajo:
	def __init__(self):
		self.rt = RepositorioTrabajos()
		self.lista = self.rt.get_all()
