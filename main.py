from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
<<<<<<< HEAD
=======
import mysql.connector
>>>>>>> 27dafba (Initial commit)
 
class mainHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols =1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #add widgets to window

<<<<<<< HEAD
=======
        #connect to database
        #mybd = mysql.connector.connect(
           # host = "localhost",
        # user = "root",
         #   passwd = "passWd123",)

>>>>>>> 27dafba (Initial commit)
        #image widget
        self.window.add_widget(Image(source="logo.jpg"))
        #Label widget
        

        self.logowanie = Label(
                         text="PODAJ LOGIN I HASŁO",
                         font_size = 18,
                         color = '#76b5c5'
                        )
        self.window.add_widget(self.logowanie)

        self.label = Label(
                        text= "[b]Login: [/b]", markup=True,  
                        font_size = 14,
                        size_hint = (1, 0.5),
                        color = '#76b5c5'
                        )
        
        self.window.add_widget(self.label)

        #text input widget
        self.user = TextInput(
                    multiline=False,
                    padding_y = (20, 20),
                    size_hint = (1, 0.5),
                    background_color = '#cececc'
                    )
        self.window.add_widget(self.user)

        self.label = Label(
                        text= "[b]Hasło: [/b]", markup=True,
                        font_size = 14,
                        size_hint = (1, 0.5),
                        color = '#76b5c5'
                        )
    
        self.window.add_widget(self.label)

        self.password = TextInput( 
                    multiline=False,
                    password=True, 
                    padding_y = (20, 20),
                    size_hint = (1, 0.5),
                    background_color = '#cececc'
                    )
        self.window.add_widget(self.password)
        #button widget
        self.button = Button(
                      text="ZALOGUJ!",
                      size_hint = (1, 0.5),
                      bold = True,
                      background_color = '#76b5c5'
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        

        

        return self.window

    def callback(self, instance):
        self.logowanie.text = "PODAJ HASŁO DLA " + self.user.text + " !"

if __name__ == "__main__":
    mainHello().run()
    