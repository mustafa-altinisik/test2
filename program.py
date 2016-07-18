# -*- coding: utf-8 -*-

import kivy
kivy.require('1.0.6') # replace with your current kivy version !
#Mevcut kivy versiyonu ile degistirilmeli.

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

import RPi.GPIO as GPIO
#Birkac modul cektik.

def deneme(obj):
    if obj.text == "Dene":
        print(u"Deneme başarılı")


class Deneme_Uygulamasi(App)
    def yapı(self):
        with layout.canvas.before:
            Color(.2, .2, .2, 1)
            self.rect =Rectangle(size=(800,600), pos=layout.pos)

        buton = Button(text="Dene")
        buton.bind()

        return layout