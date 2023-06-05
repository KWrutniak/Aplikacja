from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout



class Schedule(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 6
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        def when_press(self, instance):

            # connect to database

            conn = sqlite3.connect('users.sqlite')
            cur = conn.cursor()
            conn.commit()

            login1 = self.user.text
            password = self.password.text

            query = ('SELECT login, passwd, imie FROM users WHERE login = ? AND passwd = ?')
            cur.execute(query, (login1, password))
            result = cur.fetchone()
            conn.commit()
            print(' result:', result)

            # sprawdzenie poprawności danych
            if result == None or login1 != result[0] or password != result[1]:
                self.logowanie.text = "DANE NIEPOPRAWNE!"
            else:
                self.logowanie.text = "WITAJ " + result[2] + " !"

            return result

            cur.close()
            conn.close()

        root = StackLayout()
        for i in range(31):
            btn = Button(text=str(i + 1), width=100, size_hint=(None, 0.15))
            root.add_widget(btn)
        return root















        return self.window



if __name__ == "__main__":
    Schedule().run()