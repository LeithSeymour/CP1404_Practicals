"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometers(App):

    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('MilesToKilometers.kv')
        return self.root

    def increment(self, value, current_display):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = current_display + value
        self.root.ids.input_number.text = str(result)

    def convert_miles_to_kilometers(self, current_display):
        try:
            current_display = int(current_display)
            result = current_display * 1.60934
            self.root.ids.output_display.text = str(result)
        except ValueError:
            self.root.ids.output_display.text = str(0.0)
            return  # it was a string, not an int.


MilesToKilometers().run()
