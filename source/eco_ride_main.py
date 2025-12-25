from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        car = ElectricCar("EC401", "Tesla Model X", 85, 7)
        scooter = ElectricScooter("ES402", "Ather 450X", 70, 80)

        print("\nCar Trip Cost (10km): ", car.calculate_trip_cost(10))
        print("\nScooter Trip Cost (10km): ", scooter.calculate_trip_cost(10))


if __name__ == "__main__":
    EcoRideMain.main()