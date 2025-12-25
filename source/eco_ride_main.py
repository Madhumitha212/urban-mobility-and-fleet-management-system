from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        car = ElectricCar("EC401", "Tesla Model 3", 85, 7)
        scooter = ElectricScooter("ES402", "Ather 450X", 70, 80)

        vehicles = [car, scooter]

        print("\nTrip Cost Calculation (Polymorphism):")

        for vehicle in vehicles:
            cost = vehicle.calculate_trip_cost(10)
            print(f"{vehicle.model} -> Trip Cost for 10 km: {cost}")


if __name__ == "__main__":
    EcoRideMain.main()