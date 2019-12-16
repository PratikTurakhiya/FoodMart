from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class dpersonWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class dpersonApp(App):
    def build(self):
        return dpersonWindow()

if __name__=='__main__':
    dpersonApp().run()