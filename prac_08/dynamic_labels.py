from kivy.app import App
from kivy.lang import Builder

NEW_COLOUR = (255, 6, 7, 1)


class DynamicLabelsApp(App):
    """Dynamically display labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

