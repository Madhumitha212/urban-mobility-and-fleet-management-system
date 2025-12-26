import csv
from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicles = [
            ElectricCar("EV1301", "Tesla Model 3", 80, 5),
            ElectricScooter("EV1302", "Ather 450X", 70, 85)
        ]

        with open("fleet.csv",mode = "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(["vehicle_id", "model","battery", "type"])

            for vehicle in vehicles:
                vehicle_type = "Car" if isinstance(vehicle,ElectricCar) else "Scooter"
                writer.writerow([
                    vehicle.vehicle_id,
                    vehicle.model,
                    vehicle._Vehicle__battery_percentage,
                    vehicle_type
                ])

        print("\nFleet data written to fleet.csv")

        print("\nReading data from CSV:")
        with open("fleet.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                print(row)

if __name__ == "__main__":
    EcoRideMain.main()