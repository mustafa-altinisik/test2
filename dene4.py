# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button


class Butonumuz(Button):
    def __init__(self):
        Button.__init__(self)
        self.sayi = 1
        self.text = "Basiniz, sayi = %d" %self.sayi
        self.on_press = self.arttir
    def arttir(self,*k):
        self.sayi +=1
        self.sayi = "Basiniz, sayi = %d" %self.sayi


class program(App):
    def build(self):
        buton = Butonumuz()
        return buton

if __name__ == "*__main__*":
    program().run()