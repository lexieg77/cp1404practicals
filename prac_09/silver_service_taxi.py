from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Silver Service Taxi."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialising silver service taxi class."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return the price for the silver service taxi trip."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the silver service taxi's current fare."""
        return self.flagfall + super().get_fare()
