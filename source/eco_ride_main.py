from vehicle import Vehicle

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicle1 = Vehicle("EV201", "Tesla Model Y",90)
        vehicle1.display_details()
        print("Updating battery to 110(Invalid)")
        vehicle1.set_battery_percentage(110)
        print("updating battery to 75 (valid)")
        vehicle1.set_battery_percentage(75)
        vehicle1.display_details()


if __name__ == "__main__":
    EcoRideMain.main()