'''
Created on 01.11.2021

@author: Paul Buda
'''

#read parking spot
parkingSpot = open('parkplatz.txt')
#get number of normal parking cars
numberCars = ord(parkingSpot.readline()[2]) - 64

#get all across parking cars, the left wall is the car at the spot -2 and the right wall the car at spot <numberCars>
acrossCars = [-2]
for r in range(int(parkingSpot.readline())):
    acrossCars.append(int(parkingSpot.readline()[2:]))
parkingSpot.close
acrossCars.append(numberCars)

#check for each normal parking car, if a across parking car is in front of it, how far that car must drive right respectively left
#and get the number of that car
for carNumber in range(numberCars):
    if(carNumber in acrossCars):
        toRight = 1
        toLeft = 2
        acrossNumber = acrossCars.index(carNumber)
    elif(carNumber - 1 in acrossCars): 
        toRight = 2
        toLeft = 1
        acrossNumber = acrossCars.index(carNumber - 1)
    #if no car is in front print the output for that car and continue
    else:
        print(chr(carNumber + 65) + ":")
        continue
    
    #true if the car(s) can make space to the specific direction
    canRight = True
    canLeft = True
    
    #count the number of cars needed to move
    rightNeeded = 0
    leftNeeded = 0
    
    #count how far all cars need to move together
    rightSteps = 0
    leftSteps = 0
    
    #save the cars and their direction and length to move
    movedCarsRight = []
    movedCarsLeft = []
    
    #check if the cars can make space to the right
    while(toRight > 0):
        if(acrossNumber > len(acrossCars) - 2):
            canRight = False
            break
        rightSteps += toRight
        rightNeeded += 1
        movedCarsRight.append([acrossNumber, toRight])
        toRight -= acrossCars[acrossNumber + 1] - acrossCars[acrossNumber] - 2
        acrossNumber += 1
    
    #reset the acrossNumber
    acrossNumber -= rightNeeded
    
    #check if the cars can make space to the left
    while(toLeft > 0):
        if(acrossNumber < 0):
            canLeft = False
            break
        leftSteps += toLeft
        leftNeeded += 1
        movedCarsLeft.append([acrossNumber, toLeft])
        toLeft -= acrossCars[acrossNumber] - acrossCars[acrossNumber - 1] - 2
        acrossNumber -= 1
    
    #check witch way is faster, left or right
    driveRight = False
    #if the cars can't move right or left, print that the car can't drive out
    if(not(canRight or canLeft)):
        print(chr(carNumber + 65) + ": can't drive out")
        continue
    elif(canRight and not canLeft):
        driveRight = True
    elif(not canRight and canLeft):
        pass
    else:
        if(rightNeeded < leftNeeded):
            driveRight = True
        elif(rightNeeded > leftNeeded):
            pass
        elif(rightSteps <= leftSteps):
            driveRight = True
    
    #print the fastest way
    if(driveRight):
        print(chr(carNumber + 65) + ": ", end = "")
        for car in movedCarsRight[:-1]:
            print(chr(car[0] + 64 + numberCars) + " " + str(car[1]) + " right, ", end = "")
        print(chr(movedCarsRight[-1][0] + 64 + numberCars) + " " + str(movedCarsRight[-1][1]) + " right")
    else:
        print(chr(carNumber + 65) + ": ", end = "")
        for car in movedCarsLeft[:-1]:
            print(chr(car[0] + 64 + numberCars) + " " + str(car[1]) + " left ", end = "")
        print(chr(movedCarsLeft[-1][0] + 64 + numberCars) + " " + str(movedCarsLeft[-1][1]) + " left ", end = "")
