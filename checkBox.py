from kivy.app import App 
from kivy.uix.checkbox import CheckBox

class MinhaApp(App):
    def build(self):
        return CheckBox(active=False)
    
if __name__ == '_main_':
    MinhaApp().run()
