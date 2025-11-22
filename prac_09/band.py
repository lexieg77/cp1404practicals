class Band:
    """Band class."""

    def __init__(self, band_name=""):
        """Construct a Band with a band name and empty musician's collection."""
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.band_name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))


