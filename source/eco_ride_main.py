from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicles = [
            ElectricCar("EV1201", "Tesla Model 3", 60, 5),
            ElectricCar("EV1202", "Tesla Model Y", 90, 7),
            ElectricScooter("EV1203", "Ather 450X", 40, 85),
            ElectricScooter("EV1204", "Ola S1", 75, 90)
        ]

        vehicles.sort(
            key=lambda v: v._Vehicle__battery_percentage,
            reverse=True
        )

        print("\nVehicles sorted by Battery Percentage(Descending):")
        for v in vehicles:
            v.display_details()

if __name__ == "__main__":
    EcoRideMain.main()