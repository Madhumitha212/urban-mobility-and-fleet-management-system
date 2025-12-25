from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_hubs = {
            "Downtown" : [],
            "Airport"  : []
        }

        car1 = ElectricCar("EC801", "Tesla Model 3", 90, 5)
        car2 = ElectricCar("EC802", "Tesla Model Y", 85, 7)
        scooter1 = ElectricScooter("ES803", "Ather 450X", 80, 85)

        fleet_hubs["Downtown"].append(car1)
        fleet_hubs["Airport"].append(car2)
        fleet_hubs["Downtown"].append(scooter1)

        def search_by_vehicle_id(vehicle_id):
            for hub, vehicles in fleet_hubs.items():
                for vehicle in vehicles:
                    if vehicle.vehicle_id == vehicle_id:
                        print(f"\nVehicle found in hub: {hub}")
                        vehicle.display_details()
                        return 
            print("\nVehicle not found")
        
        def search_by_model(model_name):
            found = False
            for hub, vehicles in fleet_hubs.items():
                for vehicle in vehicles:
                    if vehicle.model.lower() == model_name.lower():
                        print(f"\nVehicle found in hub: {hub}")
                        vehicle.display_details()
                        found = True
            if not found:
                print("\nNo vehicle found with this model")

        def search_by_hub(hub_name):
            if hub_name in fleet_hubs:
                print(f"\nVehicles in hub: {hub_name}")
                for vehicle in fleet_hubs[hub_name]:
                    vehicle.display_details()

            else:
                print("\nHub not found")
        
        search_by_vehicle_id("EV802")
        search_by_model("Ather 450X")
        search_by_hub("Downtown")


if __name__ == "__main__":
    EcoRideMain.main()