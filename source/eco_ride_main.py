from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_hubs = {
            "Downtown" : [],
            "Airport" : []
        }

        car1 = ElectricCar("EV701", "Tesla Model 3", 90, 5)
        car2 = ElectricCar("EV701", "Tesla Model Y", 85, 7)
        scooter1 = ElectricScooter("EV702", "Ather 450X", 80, 85)

        def add_vehicle(hub, vehicle):
            for vehicles in fleet_hubs.values():
                if vehicle in vehicles:
                    print(f"Duplicate vehicle ID detected: {vehicle.vehicle_id}")
                    return 
            fleet_hubs[hub].append(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} added to {hub}")

        add_vehicle("Downtown", car1)
        add_vehicle("Airport", car2)
        add_vehicle("Downtown", scooter1)

        print("\nFinal Fleet status:")
        for hub, vehicles in fleet_hubs.items():
            print(f"\nHub: {hub}")
            for v in vehicles:
                v.display_details()


if __name__ == "__main__":
    EcoRideMain.main()