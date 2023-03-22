from time import sleep
from threading import Thread
import random

print("------")

# classe task che ereditata da Thread
class Task(Thread):

    # iniziallizazione oggetto
    def __init__(self, id, t):
        Thread.__init__(self)
        self.id = id
        self.t = t

    # metodo per l'esecuzione
    def run(self):
        print(f"{self.id} START thread ...")
        sleep(self.t)
        print(f"{self.id} FINISH thread time({self.t})")

class TaskSleep1(Thread):
    def __init__(self, id, tempo):
        Thread.__init__(self)
        self.id = id
        self.tempo = tempo

    def start(self):
        out = 0
        for i in range(20):
            out += 1
            sleep(self.tempo)
            print(f"id: {self.id} out: {out}")

class TaskSleep10(Thread):
    def __init__(self, id, tempo):
        Thread.__init__(self)
        self.id = id
        self.tempo = tempo

    def start(self):
        out = 0
        for i in range(20):
            out += 1
            sleep(self.tempo)
            print(f"id: {self.id} out: {out}")





# creo 2 nuovi thread e passo l'ID e il tempo che voglio che rimanga in attesa
# t1 = Task()
# t2 = Task()

l = [Task(i + 1, random.randrange(5)) for i in range(10)]
print(l)

for t in l:
    t.start()

[t.join() for t in l]

print("\nHO FINITO! Task")

# inizializzo il thread
# t1.start() # avviami il thread, fa partire il run della class Task
# t2.start()

# aspetto il tempo di attesa dei thread
# t1.join() # serve a chiudere il thread -> "spegne il thread"
# t2.join()

sleep1 = 1
sleep10 = 10

uno = TaskSleep1(1, sleep1)
print("\nFINISH th1")

dieci = TaskSleep10(2, sleep10)
uno.start()
dieci.start()

uno.join()
dieci.join()

print("\nFINISH th2")

print("------")