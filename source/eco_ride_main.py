from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")
        car = ElectricCar("EC301","Tesla Model S",90, 5)
        scooter = ElectricScooter("ES302","Ola s1", 80, 90)
        print("\nElectric Car Details:")
        car.display_details()
        print("\nElectric Scooter Details:")
        scooter.display_details()

if __name__ == "__main__":
    EcoRideMain.main()