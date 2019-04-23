import numpy as np
import copy

def distance(a,b):
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 + (a[3]-b[3]))

def findNeighbors(checkCar):
    # Red=1, Black=3, Other=4, Green=6
    distances = [[0, ""], [0, ""], [0, ""], [0, ""], [0,""],[0,""],[0,""],[0,""],[0,""],[0,""]]
    civic = [130, 1, 2012, 1, 0,"Honda Civic"]
    wrangler = [110, 0, 1992, 6, 0,"Jeep Wrangler"]
    a4 = [175, 1, 2007, 3, 1,"Audi a4"]
    focus = [120, 1, 2014, 4, 0,"Ford Focus"]
    aura = [110, 1, 2009, 4, 0,"Saturn Aura"]
    eq = [100, 1, 2014, 3, 0,"Chevy Equinox"]
    infiniti = [151, 1, 2006, 6, 1,"Infiniti 635"]
    scooter = [35, 1, 2017, 1, 0,"Veloz Scooter"]
    lambo = [217, 0, 2019, 6, 1,"Lambourgini"]
    sentra = [181, 1, 2003, 3, 0,"Nissan Sentra"]
    
    cars = [civic, wrangler, a4, focus, aura, eq, infiniti, scooter, lambo, sentra]
    
    for i in range(0, 10):
        distances[i][0] = distance(checkCar, cars[i])
        distances[i][1] = cars[i][5]
    
    return distances, cars


def normalize(cars, singleCar):
    
    
    length = len(cars)
    
    normalCars = []
    for i in range(0, length):
        normalCars.append([])
    
    speedMean = mean(cars, length, 0)
    speedDev = stdDev(cars, length, 0, speedMean)
    
    yearMean = mean(cars, length, 2)
    yearDev = stdDev(cars, length, 2, yearMean)
    
    colorMean = mean(cars, length, 3)
    colorDev = stdDev(cars, length, 3, colorMean)
    
    for i in range(0, length):
        normalCars[i].append((cars[i][0]-speedMean)/speedDev)
        normalCars[i].append(cars[i][1])
        normalCars[i].append((cars[i][2]-yearMean)/yearDev)
        normalCars[i].append((cars[i][3]-colorMean)/colorDev)
        normalCars[i].append(cars[i][4])
        normalCars[i].append(cars[i][5])
    
    normalCar = []
    
    normalCar.append((singleCar[0]-speedMean)/speedDev)
    normalCar.append(singleCar[1])
    normalCar.append((singleCar[2]-yearMean)/yearDev)
    normalCar.append((singleCar[3]-colorMean)/colorDev)
        

    return normalCars, normalCar
    
    
def mean(values, length, index):
    mean = 0
    for value in values:
        mean += value[index]
    mean /= length
    return mean        

def stdDev(values, length, index, mean):
    arr = []
    
    for value in values:
        arr.append((value[index]-mean) ** 2)
    
    s = np.sum(arr)
    return(np.sqrt(s/length))
        

def printCars(cars):
    colors = ["NO_COLOR", "Red", "NO_COLOR", "Black", "Green", "NO_COLOR", "Other"]
    print("Name\t\tTop Speed\tAuto\tYear\tColor\tFast")
    for i in cars:
        if(len(i[5]) < 8):
            print(i[5], end="\t\t")
        else:
            print(i[5], end="\t")
        print("%.2f" % (i[0]), end="\t\t")
        print("%.2f" % (i[1]), end="\t")
        print("%.2f" % (i[2]), end="\t")
        print("%.2f" % (i[3]), end="\t")
        print("%.2f" % (i[4]))


def knn():
    malibu = [118, 1, 2000, 1]
    dist, cars = findNeighbors(malibu)
    """print(dist)
    print()
    print(cars)
    min = dist[0]

    for i in range(0, 10):
        if(dist[i] < min):
            min = dist[i]
    print("The malibu is closest to the " + min[1])"""
    printCars(cars)
