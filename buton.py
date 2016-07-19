# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Button


class Uygulama(App):
    def build(self):
        self.title = u"Buton deneme uygulaması"
        dugme = Button(text = u"Merhaba Kivy")
        return dugme
Uygulama().run()