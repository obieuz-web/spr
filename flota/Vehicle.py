from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, registration_number, capacity, current_location=(0, 0)):
        self.registration_number = registration_number
        self.capacity = capacity
        self.current_location = current_location

    @abstractmethod
    def move(self, destination):
        pass

    def get_info(self):
        pass

    def calculate_fuel_cost(self, distance):
        pass
