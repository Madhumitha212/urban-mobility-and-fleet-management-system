import json
from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_hubs = {
            "Downtown" : [ElectricCar("EV1401", "Tesla Model X", 85, 7)],
            "Airport" : [ElectricScooter("EV1402", "Ola S1", 65, 90)]
        }

        json_data = {}
        
        for hub, vehicles in fleet_hubs.items():
            json_data[hub] = []
            for v in vehicles:
                json_data[hub].append({"vehicle_id" : v.vehicle_id,
                                       "model" : v.model,
                                       "battery" : v._Vehicle__battery_percentage,
                                       "type" : v.__class__.__name__})
        with open("fleet.json", "w") as file:
            json.dump(json_data, file, indent=4)
        print("Fleet data writtern to fleet.json")
        print("\nReading data from JSON:")
        with open("fleet.json", "r") as file:
            data = json.load(file)
            for hub, vehicles in data.items():
                print(f"\nHub: {hub}")
                for v in vehicles:
                    print(v)

if __name__ == "__main__":
    EcoRideMain.main()
