import random
import time

n = 1000000
l = [random.uniform(0., 1.) for _ in range(n)]
print(l)

startTime = time.time() #START

maximum = l[0]
for element in l:
    if element > maximum:
        maximum = element

print(f"il valore massimo è: {maximum}")
endTime = time.time() #END
print(f"durata algoritmo: {endTime - startTime}") #cronometro quanto ci mette ad eseguire l'algoritmo