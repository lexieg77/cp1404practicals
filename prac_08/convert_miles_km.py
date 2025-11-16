from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for converting miles to km."""

    def build(self):
        """Bild the Kivy app from the kv file."""
        Window.size = (400, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKmApp().run()
