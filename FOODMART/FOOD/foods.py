from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image



class userWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class userApp(App):
    def build(self):
        return userWindow()

class FullImage(Image):
            pass

if __name__=='__main__':
    userApp().run()
