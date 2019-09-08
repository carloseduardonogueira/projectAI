from src.services.breadth_search import Breadth
from src.structs.map import Map

def readFile(file):
    file = open(file, 'r')
    fcontent = file.readlines()
    file.close()
    return fcontent


cities = readFile('input')
origin = ""
destiny = ""
if not cities:
    print("Arquivo em branco")
else:
    destiny = cities.pop(len(cities) - 1).split()
    origin = cities.pop(len(cities) - 1).split()
    destiny = destiny[0].replace(';', '')
    origin = origin[0].replace(';', '')
    indexDestiny = -1
    indexOrigin = -1

map = Map(cities)

for i in map.cities:
    if i.name == origin:
       indexOrigin = map.cities.index(i)
    elif i.name == destiny:
        indexDestiny = map.cities.index(i)

'''for x in map.cities:
    print(x.name)
    for y in x.neighbors:
        print(" -->", y.city.name)'''

breadth = Breadth(map.cities[indexOrigin], map.cities[indexDestiny])
breadth.search()
