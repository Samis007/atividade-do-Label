from kivy.app import App 
from kivy.uix.slider import Slider

class MinhaApp(App):
    def build(self):
        return Slider(min=0, max=100, value=50)
    
if __name__=="__main__":
    MinhaApp().run()
    #serve para ajustar configurações ou paramentros com valores contínuos, como volume ou brilho.