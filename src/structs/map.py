from src.structs.city import City
from src.structs.neighbor import Neighbor


class Map:
    def __init__(self, file):
        self.cities = []
        for f in file:
            city, neighbor = f.split()
            city = city.replace(',', '')
            neighbor = neighbor.replace(';', '')
            cityPosition = -1
            neighborPosition = -1
            if len(self.cities) != 0:
                for i in self.cities:
                    if city == i.name:
                        cityPosition = self.cities.index(i)
                    elif neighbor == i.name:
                        neighborPosition = self.cities.index(i)
            if cityPosition < 0:
                self.cities.append(City(city))
                if neighborPosition < 0:
                    self.cities.append(City(neighbor))
                    self.cities[len(self.cities) - 2].addNeighbor(Neighbor(self.cities[len(self.cities) - 1]))
                else:
                    self.cities[len(self.cities) - 1].addNeighbor(Neighbor(self.cities[neighborPosition]))
            else:
                if neighborPosition < 0:
                    self.cities.append(City(neighbor))
                    self.cities[cityPosition].addNeighbor(Neighbor(self.cities[len(self.cities) - 1]))
                else:
                    self.cities[cityPosition].addNeighbor(Neighbor(self.cities[neighborPosition]))



