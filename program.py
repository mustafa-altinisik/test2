# -*- coding: utf-8 -*-



from kivy.app import App
from kivy.uix.button import Button
#from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.image import Image
#from kivy.uix.slider import Slider
#from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

#Birkac modul cektik.


class Deneme_Uygulamasi(App):
    def build(self):
        layout = GridLayout(cols=5, rows=5, spacing=5, padding=2,col_default_width=30, row_default_height=30)
        with layout.canvas.before:
            Color(.2, .2, .2, 1)
            self.rect = Rectangle(size=(600,600), pos=layout.pos)




        buton = Button(text="Dene")
        buton.bind()

        return layout


if __name__ == "__main__":
    Deneme_Uygulamasi().run()

#exit(0) means a clean exit without any errors / problems
#exit0 hatasiz temiz bir cikis anlamina gelir.