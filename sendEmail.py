from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import smtplib


class sendEmail(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.senders_email = Label(
            text="PODAJ SWÓJ EMAIL",
            font_size=14,
            color='#76b5c5',
            bold=True
        )
        self.window.add_widget(self.senders_email)

        self.user_email = TextInput(
            multiline=False,
            padding_y=(20, 20),
            halign='center',
            size_hint = (1, 0.5),
            background_color='#cececc'
        )
        self.window.add_widget(self.user_email)

        self.description = Label(
            text="OPISZ PROBLEM",
            font_size=14,
            color='#76b5c5',
            bold=True
        )
        self.window.add_widget(self.description)

        self.message = TextInput(
            multiline=True,
            padding_y=(20, 20),
            size_hint=(1, 0.5),
            background_color='#cececc'
        )
        self.window.add_widget(self.message)

        # buttons widget
        self.button = Button(
            text="WYŚLIJ DO IT",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#76b5c5'
        )

        self.button.bind(on_press=self.email_check_send)

        self.window.add_widget(self.button)

        return self.window

    def email_check_send(self, **kwargs):
        email = self.user_email
        list(email)
        allowed_char = []
        for i in range(48, 58):
            allowed_char.append(chr(i))
        for i in range(97, 123):
            allowed_char.append(chr(i))
        allowed_char.append('-')
        allowed_char.append('_')
        allowed_char.append('.')
        allowed_char.append('@')

        for char in email:
            if char not in allowed_char:
                self.senders_email.text = "E-MAIL ZAWIERA NIPEPOPRAWNE ZNAKI, WPISZ PONOWNIE"



class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session


    def send_message(self, subject, body):
            #''' This must be removed '''
            headers = [
                "From: " + self.email,
                "Subject: " + subject,
                "To: " + self.email,
                "MIME-Version: 1.0",
                "Content-Type: text/html"]
            headers = "\r\n".join(headers)
            self.session.sendmail(
                self.email,
                self.email,
                headers + "\r\n\r\n" + body)

        #__version__ = 'some_version'

class send_email(App):
        gm = Gmail('aplikacjatestowa2@gmail.com', 'fgdfjshigfcfqtyj')
        gm.send_message('Subject',"message6955")


if __name__ == "__main__":
    sendEmail().run()
   # send_email().run()
