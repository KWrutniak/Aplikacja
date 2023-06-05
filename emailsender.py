from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import smtplib as smtp

from_email = 'aplikacjatestowa2@gmail.com'
passwd = 'fgdfjshigfcfqtyj'

class Email(BoxLayout):

    def sendemail(self, to, content):
        content = content.encode("UTF-8")
        print(to, content)

        self.status.text = 'W trakcie wysyłania ...'
        server = smtp.SMTP(
            'smtp.gmail.com',
            587
        )
        server.starttls()
        server.ehlo()
        server.login(
            from_email,
            passwd
        )
        server.sendmail(
            from_email,
            to,
            content
        )
        server.quit()
        self.status.text = 'Email został wysłany.'

class EmailSenderApp(App):
    def build(self):
        return Email()

if __name__ == '__main__':
    EmailSenderApp().run()

