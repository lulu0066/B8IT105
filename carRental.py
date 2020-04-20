
"""
File Description: car stock, rental records and return records
Student ID : 10543531
Student Name: Wenjuan Zhao
Git hub: https://github.com/lulu0066/B8IT105.git
"""

import pandas as pd
from car import Car, PetrolCar, DieselCar, ElectricCar, HybridCar


class CarFleet(object):
    
    def __init__(self):
        self.__petrol_cars = []
        self.__diesel_cars = []
        self.__electric_cars = []
        self.__hybrid_cars = []
        self.__csv_header = ''
        for i in range(1, 21):
            self.__petrol_cars.append(PetrolCar())
        for i in range(1, 11):
            self.__diesel_cars.append(DieselCar())
        for i in range(1, 7):
            self.__electric_cars.append(ElectricCar())
        for i in range(1, 5):
            self.__hybrid_cars.append(HybridCar())
            
    def getPetrolCars(self):
        return self.__petrol_cars

    def getDieselCars(self):
        return self.__diesel_cars
    
    def getElectricCars(self):
        return self.__electric_cars
    
    def getHybridCars(self):
        return self.__hybrid_cars
    
    def checkCarsInStock(self):
        print('Our Car Stock')
        print('Number of Petrol Cars : ' + str(len(self.getPetrolCars())))
        print('Number of Diesel Cars : ' + str(len(self.getDieselCars())))
        print('Number of Electric Cars : ' + str(len(self.getElectricCars())))
        print('Number of Hybrid Cars : ' + str(len(self.getHybridCars())))
   
    def rentCar(self, type):
        if type == 'P':
            return self.__petrol_cars.pop()
        elif type == 'D':
            return self.__diesel_cars.pop()
        elif type == 'E':
            return self.__electric_cars.pop()
        elif type == 'H':
            return self.__hybrid_cars.pop()

    def returnCar(self, type, car):
        if type == 'P':
            self.__petrol_cars.append(car)
        elif type == 'D':
            self.__diesel_cars.append(car)
        elif type == 'E':
            self.__electric_cars.append(car)
        elif type == 'H':
            self.__hybrid_cars.append(car)
    
    def mainMenu(self):
        print('Welcome to DBS Car Rental')
        self.checkCarsInStock()
        rentedCar = None
        msg = 'Would you like to rent a car R, return a car U, any key to quit? '
        answer = input(msg).upper()
        while answer == 'R' or answer == 'U':
            if answer == 'R':
                type = input('What car would you like to rent - P for petrol, D for diesel, E for electric, H for hybrid? ').upper()
                rentedCar = self.rentCar(type)
            elif answer == 'U':
                type = input('What car would you like to return - P for petrol, D for diesel, E for electric, H for hybrid? ').upper()
                self.returnCar(type, rentedCar)
#             self.checkCarsInStock()
            answer = input(msg).upper()
        print(rentedCar)