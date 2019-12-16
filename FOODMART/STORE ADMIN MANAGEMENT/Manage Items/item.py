from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class ItemWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class ItemApp(App):
    def build(self):
        return ItemWindow()

if __name__=='__main__':
    ItemApp().run()