import math

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 + (a[3]-b[3]))

def findNeighbors():
    # Red=1, Black=3, Other=4, Green=6
    distances = [[0, ""], [0, ""], [0, ""], [0, ""], [0,""],[0,""],[0,""],[0,""],[0,""],[0,""]]
    malibu = [118, 1, 2000, 1]
    civic = [130, 1, 2012, 1, 0,"honda civic"]
    wrangler = [110, 0, 1992, 6, 0,"jeep wrangler"]
    a4 = [175, 1, 2007, 3, 1,"audi a4"]
    focus = [120, 1, 2014, 4, 0,"ford focus"]
    aura = [110, 1, 2009, 4, 0,"saturn aura"]
    eq = [100, 1, 2014, 3, 0,"chevy equinox"]
    infiniti = [151, 1, 2006, 6, 1,"infiniti 635"]
    scooter = [35, 1, 2017, 1, 0,"veloz scooter"]
    lambo = [217, 0, 2019, 6, 1,"lambourgini"]
    sentra = [181, 1, 2003, 3, 0,"nissan sentra"]
    
    cars = [civic, wrangler, a4, focus, aura, eq, infiniti, scooter, lambo, sentra]
    
    for i in range(0, 10):
        distances[i][0] = distance(malibu, cars[i])
        distances[i][1] = cars[i][5]
    
    return distances, cars



dist, cars = findNeighbors()
print(dist)
print()
print(cars)
min = dist[0]

for i in range(0, 10):
    if(dist[i] < min):
        min = dist[i]
print("The malibu is closest to the " + min[1])
