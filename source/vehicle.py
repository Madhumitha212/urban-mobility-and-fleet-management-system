class Vehicle:
    def __init__(self,vehicle_id, model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
    def display_details(self):
        print("vehicle ID:", self.vehicle_id)
        print("Model:",self.model)
        print("Battery Percentage:",self.battery_percentage,"%")