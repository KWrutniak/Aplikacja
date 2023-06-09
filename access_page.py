from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import sqlite3


class AccessPage(App):
    def build(self, *kwargs):
        self.window = GridLayout()
        self.window.cols =1
        self.window.size_hint = (0.3, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #image widget
        self.window.add_widget(Image(source="logo2.jpg", size_hint_y=None, height=(180)))

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

        self.user = TextInput(
                    multiline=False,
                    padding_y = (20, 20),
                    halign='center',
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
                    halign = 'center',
                    background_color = '#cececc'
                    )
        self.window.add_widget(self.password)

        self.button = Button(
                      text="ZALOGUJ",
                      size_hint = (1, 0.5),
                      bold = True,
                      background_color = '#76b5c5'
                      )

        self.button.bind(on_press=self.when_press)
        self.window.add_widget(self.button)

        return self.window

    def when_press(self, instance):

        #connect to database
        conn = sqlite3.connect('users.sqlite')
        cur = conn.cursor()
        conn.commit()

        login1 = self.user.text
        password = self.password.text

        query = ('SELECT login, passwd, imie FROM users WHERE login = ? AND passwd = ?')
        cur.execute(query, (login1, password))
        result = cur.fetchone()
        conn.commit()

        #sprawdzenie poprawności danych
        if result == None or login1 != result[0] or password != result[1]:
            self.logowanie.text = "DANE NIEPOPRAWNE!"
        else:
            self.logowanie.text = "WITAJ " + result[2] + " !"
            return result

        cur.close()
        conn.close()


if __name__ == "__main__":
   AccessPage().run()
    