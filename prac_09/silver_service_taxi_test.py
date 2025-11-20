from silver_service_taxi import SilverServiceTaxi

def main():
    """Testing the silver service taxi class."""
    my_silver_service_taxi = SilverServiceTaxi("Prius 1", 200, 2)
    my_silver_service_taxi.drive(18)
    print(my_silver_service_taxi)
    print(f"Current fare: ${my_silver_service_taxi.get_fare():.2f}")

main()