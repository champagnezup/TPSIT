piastrella_size = 150

listaMappa = []

with open("mappa.csv") as f:
	[listaMappa.append(line) for line in f.readlines()]

f.close()

screen_width = (len(listaMappa[1]) - 1) * piastrella_size
screen_height = len(listaMappa) * piastrella_size

print(screen_width)
print(screen_height)