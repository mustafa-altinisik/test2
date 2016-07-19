# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

import os

class Uygulama(App):
    def resmi_guncelle(self):
        self.resim.source = "/home/mustafa/Resimler/"+self.resimler[self.sayac%len(self.resimler)]
        self.etiket.text = self.resim.source

    def tik(self,nesne):
        self.sayac += 1
        self.resmi_guncelle()

    def basla(self,nesne):
        if self.slayt_basladi:
            self.slayt_basladi = False
            Clock.schedule_interval(self.tik,1)
            self.basla_dugme.text = "DUR"
        else:
            self.slayt_basladi = True
            Clock.unschedule(self.tik,1)
            self.basla_dugme.text = u"BAŞLAT"

    def build(self):
        self.slayt_basladi = True
        self.resimler = os.listdir("/home/mustafa/Resimler/")
        self.sayac=0
        duzen = BoxLayout(orientation="vertical")
        self.resim = Image()
        self.resim.allow_stretch = True
        self.resim.keep_ratio = False
        self.basla_dugme = Button(text="Başlat",size_hint=(1,0.1))
        self.basla_dugme.bind(on_press=self.basla)
        self.etiket = Label(text="Etiket",size_hint=(1,0.1))
        duzen.add_widget(self.resim)
        duzen.add_widget(self.etiket)
        duzen.add_widget(self.basla_dugme)
        self.resmi_guncelle()
        return duzen
Uygulama().run()