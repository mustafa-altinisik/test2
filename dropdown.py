# -*- coding: utf-8 -*-

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.app import App

class Uygulama(App):
    def secim(self,nesne):
        if nesne.text=="mavi":
            self.resim.color=(0,0,1,1)
        elif nesne.text=="kirmizi":
            self.resim.color=(1,0,0,1)
        elif nesne.text=="yeşil":
            self.resim.color=(0,1,0,1)
        self.dropdown.select(nesne.text)
        self.anaDugme.text=nesne.text
    def build(self):
        self.renkler=(["mavi"],["kirmizi"],["yeşil"])
        duzen=BoxLayout()
        self.dropdown=DropDown()
        self.resim=Image()
        for renk in self.renkler:
            dugme=Button(text=renk[0],size_hint_y=None,height=50)
            dugme.bind(on_relase=self.secim)
            self.dropdown.add_widget(dugme)
        self.anaDugme=Button(text="Renkler",size_hint=(None,None))
        self.anaDugme.bind(on_relase=self.dropdown.open)
        duzen.add_widget(self.anaDugme)
        duzen.add_widget(self.resim)

        return duzen

Uygulama().run()