from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class deliveryWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class deliveryApp(App):
    def build(self):
        return deliveryWindow()

if __name__=='__main__':
    deliveryApp().run()