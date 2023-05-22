from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class sendEmail(App):

    def build(self):

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        self.description = Label(
                         text="OPISZ PROBLEM",
                         font_size = 14,
                         color = '#76b5c5',
                         bold = True
                        )
        self.window.add_widget(self.description)

        self.message = TextInput(
                    multiline=True,
                    padding_y = (20, 20),
                    size_hint = (1, 0.5),
                    background_color = '#cececc'
                    )
        self.window.add_widget(self.message)

        #buttons widget
        self.button = Button(
                      text="WYŚLIJ DO IT",
                      size_hint = (1, 0.5),
                      bold = True,
                      background_color = '#76b5c5'
                      )
        
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        

        
        return self.window
        

    def callback(self, instance):
        self.logowanie.text = " "

if __name__ == "__main__":
    Contact().run()