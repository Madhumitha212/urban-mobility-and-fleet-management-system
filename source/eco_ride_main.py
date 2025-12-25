from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        car1 = ElectricCar("EV901", "Tesla Model 3", 90, 5)
        car2 = ElectricCar("EV902", "Tesla Model Y", 85, 7)
        scooter1 = ElectricScooter("EV903", "Ather 450X", 80, 85)
        scooter2 = ElectricScooter("EV904", "Ola 51", 75, 90)

        vehicles = [car1, car2, scooter1, scooter2]

        electric_cars = []
        electric_scooters = []

        for vehicle in vehicles:
            if isinstance(vehicle, ElectricCar):
                electric_cars.append(vehicle)
            elif isinstance(vehicle, ElectricScooter):
                electric_scooters.append(vehicle)
        
        print("\nELectric Cars:")
        for car in electric_cars:
            car.display_details()

        print("\nElectric Scooters:")
        for scooter in electric_scooters:
            scooter.display_details()

if __name__ == "__main__":
    EcoRideMain.main()