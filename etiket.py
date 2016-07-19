from kivy.app import App
from kivy.uix.label import Label

class Uygulama(App):
    def build(self):
        self.title="Etiket deneme uygulamasi"
        etiket=Label(text="Merhaba kivy")
        return etiket
Uygulama().run()