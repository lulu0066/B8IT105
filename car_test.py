"""
File Description: unit test
Student ID : 10543531
Student Name: Wenjuan Zhao
Git hub: https://github.com/lulu0066/B8IT105.git
"""

import unittest

from car import Car, PetrolCar, DieselCar, ElectricCar
from carRental import CarFleet

# test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        
    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ford')
        self.assertEqual('Ford', self.car.getMake())
        
    def test_car_model(self):
        self.assertEqual('', self.car.getModel())
        self.car.setModel('Focus')
        self.assertEqual('Focus', self.car.getModel())

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

class TestPetrol(unittest.TestCase):
    
    def setUp(self):
        self.petrol = PetrolCar()
    
    def test_petrol_engineSize(self):
        self.assertEqual('', self.petrol.getEngineSize())
        self.petrol.setEngineSize('1.5')
        self.assertEqual('1.5', self.petrol.getEngineSize())
 
class TestDiesel(unittest.TestCase):
    
    def setUp(self):
        self.diesel = DieselCar()
    
    def test_diesel_engineSize(self):
        self.assertEqual('', self.diesel.getEngineSize())
        self.diesel.setEngineSize('2.5')
        self.assertEqual('2.5', self.diesel.getEngineSize())
        
class TestElectric(unittest.TestCase):
    
    def setUp(self):
        self.electric = ElectricCar()
    
    def test_electric_engineSize(self):
        self.assertEqual('1', self.electric.getNumberFuelCells())
        self.electric.setNumberFuelCells('2')
        self.assertEqual('2', self.electric.getNumberFuelCells())

class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.fleet = CarFleet()
    def test_getPetrolCars(self):
        self.assertEqual(20, len(self.fleet.getPetrolCars()))
    def test_getDieselCars(self):
        self.assertEqual(10, len(self.fleet.getDieselCars()))
    def test_getElectricCars(self):
        self.assertEqual(6, len(self.fleet.getElectricCars()))
    def test_getHybridCars(self):
        self.assertEqual(4, len(self.fleet.getHybridCars()))

        
if __name__ == '__main__':
    unittest.main()
