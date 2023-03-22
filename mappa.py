import pygame
from dati import *
from piastrella import Piastrella

class Mappa:
	def __init__(self, mappa_dati, schermo):
		self.schermo = schermo
		self.setupMappa(mappa_dati)

	def setupMappa(self, mappa_dati):
		self.piastrelle = pygame.sprite.Group()

		for i, riga in enumerate(mappa_dati):
			for j, carattere in enumerate(riga):
				if carattere == '1':
					piastrella = Piastrella((j * piastrella_size, i * piastrella_size), piastrella_size)
					self.piastrelle.add(piastrella)

	def run(self):
		self.piastrelle.draw(self.schermo)