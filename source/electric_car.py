from vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity
    def display_details(self):
        super().display_details()
        print("Seating Capacity: ",self.seating_capacity)