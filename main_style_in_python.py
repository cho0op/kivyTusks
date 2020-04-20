import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols=1

        self.inside=GridLayout()
        self.inside.cols=2

        self.inside.add_widget(Label(text="first name: "))
        self.FirstName = TextInput(multiline=False)
        self.inside.add_widget(self.FirstName)

        self.inside.add_widget(Label(text="last name: "))
        self.LastName = TextInput(multiline=False)
        self.inside.add_widget(self.LastName)

        self.inside.add_widget(Label(text="email"))
        self.Email = TextInput(multiline=False)
        self.inside.add_widget(self.Email)

        self.add_widget(self.inside)

        self.subbmit=Button(text="Submit", font_size=40)
        self.subbmit.bind(on_press=self.pressed)
        self.add_widget(self.subbmit)
    def pressed(self, instance):
        first = self.FirstName.text
        last = self.LastName.text
        email = self.Email.text
        print("hello {0} {1} ".format(first, last))
        self.FirstName.text=""
        self.LastName.text=""
        self.Email.text=""


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()