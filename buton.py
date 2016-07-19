from kivy.app import App
from kivy.uix.button import Button
    class Uygulama(App):
        def build(self):
            self.title="Buton deneme uygulaması"
            dugme=Button(text="Merhaba Kivy")
            return dugme
Uygulama().run()