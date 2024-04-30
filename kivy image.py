from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):

        return AsyncImage(source='https://i.pinimg.com/564x/3b/da/79/3bda79dc0b884dffeab2879187793da5.jpg')
    
if __name__=="__main__":
    MinhaApp().run()