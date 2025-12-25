from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicles = [
            ElectricCar("EV1001", "Tesla Model 3", 90, 5),
            ElectricCar("EV1002", "Tesla Model Y", 40, 7),
            ElectricScooter("EV1003", "Ather 450X", 25, 85),
            ElectricScooter("EV1004", "Ola S1", 60, 90)
        ]

        total_vehicles = len(vehicles)
        car_count = 0
        scooter_count = 0
        low_battery_count = 0
        total_battery = 0

        for vehicle in vehicles:
            total_battery += vehicle._Vehicle__battery_percentage

            if isinstance(vehicle, ElectricCar):
                car_count += 1
            elif isinstance(vehicle, ElectricScooter):
                scooter_count += 1

            if vehicle._Vehicle__battery_percentage:
                low_battery_count += 1
        
        avg_battery = total_battery / total_vehicles

        print("\nFleet Analytics:")
        print(f"Total Vehicles: {total_vehicles}")
        print(f"Electric Cars: {car_count}")
        print(f"Electric Scooters: {scooter_count}")
        print(f"Low Battery Vehicles: {low_battery_count}")
        print(f"Average Battery Percentage: {avg_battery:.2f} %")



if __name__ == "__main__":
    EcoRideMain.main()