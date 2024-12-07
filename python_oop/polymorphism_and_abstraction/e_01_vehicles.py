from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    EXTRA_FUEL_CONSUMPTION = 0.9

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + Car.EXTRA_FUEL_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    EXTRA_FUEL_CONSUMPTION = 1.6
    TOTAL_FUEL = 0.95

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + Truck.EXTRA_FUEL_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.TOTAL_FUEL


