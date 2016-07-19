# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


class Uygulama(App):
    def build(self):
        self.title = u"Etiket Uygulaması"
        etiket = Label(text = u"Merhaba\nKivy")
        etiket.markup = True
        return etiket
Uygulama().run()