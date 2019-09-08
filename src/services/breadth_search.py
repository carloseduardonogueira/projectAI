from src.structs.queue import Queue

class Breadth:
    def __init__(self, origin, destiny):
        self.origin = origin
        self.origin.visited = True
        self.destiny = destiny
        self.border = Queue(20)
        self.border.toQueue(origin)
        self.found = False

    def search(self):
        start = self.border.getStart() #pega o primeiro elemento da fila
        print('Primeiro: {}'.format(start.name))

        if start == self.destiny:
            self.found = True
        else:
            temp = self.border.dequeue() #tira da fila
            print('Desenfileirou: {}'.format(temp.name))
            for a in start.neighbors:
                if not a.city.visited:
                    a.city.visited = True
                    self.border.toQueue(a.city)
            if self.border.numElements > 0:
                Breadth.search(self) #chamada recursiva
