# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
import os

class Uygulama(App):
    def






    def degistir(self,nesne):
        self.sayac+=1
        if self.sayac==len(self.resimler):self.sayac=0
        self.resim.source="/home/mustafa/Resimler/"+self.resimler[self.sayac]
        self.dugme.text="Gösterilen resim:%s" %self.resimler[self.sayac]
    def build(self):

        self.sayac=0
        self.resimler=os.listdir("/home/mustafa/Resimler/")
        duzen=BoxLayout(orientation="vertical")
        self.title = u"Boxlayout Eplikeyşını"
        self.dugme=Button(text="Merhaba")
        self.dugme.bind(on_press=self.degistir)
        self.resim=Image()
        self.resim.source="/home/mustafa/Resimler/"+self.resimler[self.sayac]
        duzen.add_widget(self.dugme)
        duzen.add_widget(self.resim)
        return duzen

Uygulama().run()