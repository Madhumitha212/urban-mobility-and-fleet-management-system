from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = None
        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):
        return self.__bettery_percenatge
    def set_battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Invalid battery percentage! Must be between 0 and 100.")
    def display_details(self):
        print("Vehicle ID:",self.vehicle_id)
        print("Model:",self.model)
        print("Battery Percentage:",self.__battery_percentage, "%")

    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vehicle_id == other.vehicle_id
        return False