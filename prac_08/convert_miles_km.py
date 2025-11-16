from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

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
        self.output = self.root.ids.input_number

ConvertMilesKmApp().run()
