
"""
File Description: car rental application
Student ID : 10543531
Student Name: Wenjuan Zhao
Git hub: https://github.com/lulu0066/B8IT105.git
"""
import pandas as pd
from car import Car, PetrolCar, DieselCar, ElectricCar, HybridCar
from carRental import CarFleet

dbsCarRental = CarFleet()  
myCar = Car()

myCar.setColour('Silver')

petrol = PetrolCar()
petrol.setMake('Ford')
petrol.setModel('Focus')
petrol.setEngineSize('1.6')

diesel = DieselCar()
diesel.setMake('Renault')
diesel.setModel('Clio')
diesel.setEngineSize('1.5')

electric = ElectricCar()
electric.setMake('Nissan')
electric.setModel('Leaf')
electric.setNumberFuelCells('62KWH')

hybrid = HybridCar()
hybrid.setMake('Toyota')
hybrid.setModel('Corolla')

# the initial stock of cars
def initial_cars_stock_csv(csv_file):
    type = ['Petrol','Diesel','Electric','Hybrid']
    color = myCar.getColour()
    make = [petrol.getMake(), diesel.getMake(), electric.getMake(), hybrid.getMake()]
    model = [petrol.getModel(), diesel.getModel(), electric.getModel(), hybrid.getModel()]
    engineSize = [petrol.getEngineSize(), diesel.getEngineSize(), '', '']
    numberFueCells = ['', '', electric.getNumberFuelCells(), '']
    initialStock = ['20','10','6','4']
    currentStock = ['20','10','6','4']
    dict = {'type': type, 'color': color, 'make':make, 'model':model, 'engine size':engineSize, 'fue cells':numberFueCells, 'initial stock': initialStock, 'current stock':currentStock}
    df = pd.DataFrame(dict) 
    df.to_csv(csv_file) 

# read the car stock file
def check_cars_stock(csv_file):
    df = pd.read_csv(csv_file)
    return df

def current_cars_stock_csv(csv_file):
    type = ['Petrol','Diesel','Electric','Hybrid']
    color = myCar.getColour()
    make = [petrol.getMake(), diesel.getMake(), electric.getMake(), hybrid.getMake()]
    model = [petrol.getModel(), diesel.getModel(), electric.getModel(), hybrid.getModel()]
    engineSize = [petrol.getEngineSize(), diesel.getEngineSize(), '', '']
    numberFueCells = ['', '', electric.getNumberFuelCells(), '']
    initialStock = ['20','10','6','4']
    currentStock = [len(dbsCarRental.getPetrolCars()),len(dbsCarRental.getDieselCars()),len(dbsCarRental.getElectricCars()),len(dbsCarRental.getHybridCars())]
    dict = {'type': type, 'color': color, 'make':make, 'model':model, 'engine size':engineSize, 'fue cells':numberFueCells, 'initial stock': initialStock, 'current stock':currentStock}
    df = pd.DataFrame(dict) 
    df.to_csv(csv_file) 
    
def main ():
#     initial_cars_stock_csv('car_stock.csv')
    check_cars_stock('car_stock.csv')
    dbsCarRental.mainMenu()
    current_cars_stock_csv('car_stock.csv')
#     

if __name__ == '__main__':
    main()