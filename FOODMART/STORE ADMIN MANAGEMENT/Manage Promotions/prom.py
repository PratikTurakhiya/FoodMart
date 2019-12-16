from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class promWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class promApp(App):
    def build(self):
        return promWindow()

if __name__=='__main__':
    promApp().run()