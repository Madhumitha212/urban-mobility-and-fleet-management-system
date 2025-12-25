from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicles = [
            ElectricCar("EV1201", "Tesla Model Y", 60, 7),
            ElectricCar("EV1202", "Tesla Model 3", 60, 5),
            ElectricScooter("EV1203", "Ather 450X", 40, 85),
            ElectricScooter("EV1204", "Ola S1", 40, 90)
        ]

        vehicles.sort(key=lambda v: (v._Vehicle__battery_percentage, v.model))

        print("\nVehicles sorted by Battery then Model:")
        for v in vehicles:
            v.display_details()

if __name__ == "__main__":
    EcoRideMain.main()