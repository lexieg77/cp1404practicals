from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for converting miles to km."""

    output = StringProperty()

    def build(self):
        """Bild the Kivy app from the kv file."""
        Window.size = (400, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Handle changes to the text input by updating the model from the view."""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.output = str(result)

    def handle_increment(self, change):
        """Handle incrementing up and down using the buttons."""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)

    def get_valid_miles(self):
        """Get a valid miles number."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


ConvertMilesKmApp().run()
