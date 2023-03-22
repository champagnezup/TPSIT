import pygame, sys
from dati import *
# SB: from piastrella import Piastrella
from mappa import Mappa

# pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
mappa = Mappa(listaMappa, screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill("black")

	mappa.run()
	
	pygame.display.update()
	clock.tick(60)