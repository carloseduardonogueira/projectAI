class City:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.neighbors = []

    def addNeighbor(self, city):
        self.neighbors.append(city)
