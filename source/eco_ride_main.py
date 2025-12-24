from vehicle import Vehicle

class EcoRideMain:
    @staticmethod
    def main(): 
        print("Welcome to Eco-Ride Urban Mobility System")
        vehicle1 = Vehicle("EV101","Tesla Model 3",85)
        vehicle1.display_details()


if __name__ == "__main__":
    EcoRideMain.main()