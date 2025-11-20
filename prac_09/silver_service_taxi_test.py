from silver_service_taxi import SilverServiceTaxi

def main():
    """Testing the silver service taxi class."""
    my_silver_service_taxi = SilverServiceTaxi("Prius 1", 30, 5.5)
    my_silver_service_taxi.drive(50)
    print(my_silver_service_taxi)
    print(f"Current fare: ${my_silver_service_taxi.get_fare()}")

main()