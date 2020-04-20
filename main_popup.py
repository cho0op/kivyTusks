from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.app import App
import kivy

class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass

class PopupApp(App):
    def build(self):
        return Widgets()

def show_popup():
    show=P()
    popupWindow=Popup(title="Pupop window", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

if __name__=="__main__":
    PopupApp().run()