from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class WindowManager(ScreenManager):
    pass

class MainWondow(Screen):
    pass

class SecondWindow(Screen):
    pass

kv=Builder.load_file("mymain.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()