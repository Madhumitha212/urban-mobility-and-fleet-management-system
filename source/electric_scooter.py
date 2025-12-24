from vehicle import Vehicle

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit
    def display_details(self):
        super().display_details()
        print("Max Speed Limit:",self.max_speed_limit," km/hr")