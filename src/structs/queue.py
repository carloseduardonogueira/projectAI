class Queue:
    def __init__(self, length):
        self.length = length
        self.cities = [None] * self.length
        self.start = 0
        self.end = -1
        self.numElements = 0

    def toQueue(self, city):
        if not Queue.isFull(self):
            if self.end == self.length - 1:  # reinicia o fim caso chegue na ultima posicao do vetor
                self.end = -1
            self.end += 1
            self.cities[self.end] = city
            self.numElements += 1
        else:
            print('Fila cheia!')
            return None

    def dequeue(self):
        if not Queue.isEmpty(self):
            temp = self.cities[self.start]  # guarda a primeira cidade para poder retornar
            self.start += 1
            if self.start == self.length:  # reinicia o inicio caso chegue na ultima posicao do vetor
                self.start = 0
            self.numElements -= 1
            return temp
        else:
            print('Fila vazia!')

    def getStart(self):
        return self.cities[self.start]

    def isEmpty(self):
        return self.numElements == 0

    def isFull(self):
        return self.numElements == self.length
