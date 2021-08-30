from kivy.app import App
from kivy import Config
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        return Button(text = 'Hello World')
MainApp().run()
Config.set('graphics', 'multisamples', '0')