# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


class Uygulama(App):
    def build(self):
        self.title = u"Etiket deneme uygulaması"
        etiket=Label(text = u"Merhaba kivy")
        return etiket
Uygulama().run()