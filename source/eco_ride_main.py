from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_hubs = {}

        fleet_hubs["Downtown"] = []
        fleet_hubs["Airport"] = []

        car1 = ElectricCar("EC601", "Tesla Model 3", 90, 5)
        car2 = ElectricCar("EC602", "Tesla Model Y", 85, 7)
        scooter1 = ElectricScooter("ES603", "Ather 450X", 80, 85)

        fleet_hubs["Downtown"].append(car1)
        fleet_hubs["Downtown"].append(scooter1)
        fleet_hubs["Airport"].append(car2)

        for hub_name, vehicles in fleet_hubs.items():
            print(f"\nHub: {hub_name}")
            for vehicle in vehicles:
                vehicle.display_details()


if __name__ == "__main__":
    EcoRideMain.main()