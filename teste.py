#from kivy.base import runTouchApp
#from kivy.uix.button import Button
#runTouchApp(Button(text = "hello world kivy"))

from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        return Button(text = "hello world kivy 2")
    
MainApp().run()