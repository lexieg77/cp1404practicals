from taxi import Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        flagfare = 4.50
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the silver service taxi trip."""
        return f"{super().__str__()}"


def main():
    my_silver_service = SilverServiceTaxi("Prius 1", 30, 5.5)
    print(my_silver_service.get_fare())

main()