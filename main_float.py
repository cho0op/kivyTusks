import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name=ObjectProperty(None)
    email = ObjectProperty(None)
    def btn(self):
        print("name ", self.name.text, "email ", self.email.text)
        self.name.text=""
        self.email.name=""



class MyApp(App):
    def build(self):
        return FloatLayout()

if __name__=="__main__":
    MyApp().run()