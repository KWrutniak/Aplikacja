from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout



class Contact(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.description = Label(
            text="OPISZ PROBLEM",
            font_size=14,
            color='#76b5c5',
            bold=True
        )


        root = StackLayout()
        for i in range(25):
            btn = Button(text=str(i), width=100 +i * 7, size_hint=(None, 0.15))
            root.add_widget(btn)
        return root

        self.window.add_widget(self.description)








        return self.window

    def callback(self, instance):
        self.logowanie.text = " "


if __name__ == "__main__":
    Contact().run()