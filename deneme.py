from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
    def build(self):
        b = BoxLayout()
        t = TextInput(font_size=10)
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Merhaba\nEfendim",
                  font_size=50)
        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(f)
        s.add_widget(t)
        return b

if __name__=="__main__":
    TutorialApp().run()