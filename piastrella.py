import pygame

class Piastrella(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()

		self.image = pygame.Surface((size, size)) # la prima size = x la seconda = y, creazione di un rettangolo
		self.image.fill("grey") # coloro la mia immagine
		self.rect = self.image.get_rect(topleft = pos) # il mio rrettangolo verra posizionato nella posizione pos rispetto al suo topleft (alto a sinistra)

