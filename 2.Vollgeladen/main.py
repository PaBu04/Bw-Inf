'''
Created on 02.11.2021

@author: Paul Buda
'''

#read the hotel
hotels = open("hotels.txt")
#get the number of hotels
numberHotels = int(hotels.readline())
#get the total distance to drive
totalDistance = int(hotels.readline())

#read all hotels and their distance to the start and sort them by their ranting
hotelsList = [[-1, 0]]
for r in range(numberHotels):
    hotel = hotels.readline()
    hotelKm = int(hotel.split(" ")[0])
    hotelRating = float(hotel.split(" ")[1])
    #select the better rated hotel if their are two or more hotels at the same km
    if(hotelsList[-1][0] == hotelKm):
        if(hotelsList[-1][1] < hotelRating):
            del hotelsList[-1]
            hotelsList.append([hotelKm, hotelRating])
    else:
        hotelsList.append([hotelKm, hotelRating])
hotels.close()
hotelsList = sorted(hotelsList, key=lambda x: x[1], reverse=True)

checkHotels = []
allCheckHotels = [0, totalDistance]
for hotel in hotelsList:
    canUsed = True
    allCheckHotels.append(hotel[0])
    allCheckHotels.sort()
    checkHotels = allCheckHotels.copy()
    minus = 0
    for r in range(len(checkHotels) - 2):
        if(checkHotels[r + 2 - minus] - checkHotels[r - minus] <= 360):
            del checkHotels[r + 1 - minus]
            minus += 1
    for r in range(len(checkHotels) - 1):
        if(checkHotels[r + 1] - checkHotels[r] > 360):
            canUsed = False
            break
    if(canUsed and len(checkHotels) <= 6):
        del checkHotels[0]
        del checkHotels[len(checkHotels) - 1]
    
        useHotels = []
        for hotel in hotelsList:
            if(hotel[0] in checkHotels):
                useHotels.append(hotel)
        useHotels = sorted(useHotels, key=lambda x: x[0])
        ratings = []
        for hotel in useHotels:
            ratings.append(hotel[1])
            print("Hotel at km: " + str(hotel[0]) + " with the rating of " + str(hotel[1]) + " stars!")
        break
    
print("Lowest Rating: " + str(min(ratings)))
        
