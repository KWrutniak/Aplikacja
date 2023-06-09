from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import  access_page, menu, schedule, emailsender

class MyScreens(ScreenManager):
    def screen_manager_method(self):
        pass

class Access_page(Screen):
    def screen_method(self):
        pass

class Menu(Screen):
    def screen_method(self):
        pass

class Schedule(Screen):
    def screen_method(self):
        pass

class Emailsender(Screen):
    def screen_method(self):
        pass

class ScreensSample(App):
    def app_method(self):
        pass

ScreensSample().run()