from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicles = [
            ElectricCar("EV1101", "Tesla Model 3",90, 5),
            ElectricCar("EV1102", "Tesla Model Y",40, 7),
            ElectricScooter("EV1103" , "Ather 450X", 25, 85),
            ElectricScooter("EV1104", "Ola S1", 60, 90)
        ]

        vehicles.sort(key = lambda v: v._Vehicle__battery_percentage)

        print("\nVehicles sorted by Battery Percentage:")
        for v in vehicles:
            v.display_details()


if __name__ == "__main__":
    EcoRideMain.main()