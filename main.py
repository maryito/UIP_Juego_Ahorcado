#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import  string as cadena
from kivy.app import  App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import  Button
from kivy.uix.screenmanager import ScreenManager


# #print( cadena.ascii_uppercase)
# #print(cadena.ascii_letters)
# #print(cadena.ascii_lowercase)
class Ventana(ScreenManager):
    """
    clase ventana se encargara de administrar todos las funciones y herramientas del juego
    """
    acento={"A":"Á","E":"É","I":"Í","O":"Ó","U":"Ú"}
    animales = ["Armadillo", "Avestruz", "Ballena","Camaleon", "hormiga","Chimpance","Cocodrilo","Elefante","Escarabajo",
                "Escorpion","Guepardo","Hipopotamo","Flamenco","Gallina","Iguana","Jabali","Koala","Langostino","Leopardo",
                "Mariposa","Mosquito","Nutria","Paloma","Puma","Rinoceronte","Salamandra","Sanguijuela","Serpiente",
                "Tiburon","Tortuga","Venado","Zorro"]
    lincen=["electronica","sistemas","industrial","maritima","redes"]
    lista=[""]
    temp=[""]
    temp_acent=[""]
    contador = 0

    palabra = ""
    texto = ""
    categoria=""

    def generar_palabra(self, cat): # Palabra del ahorcado
        """
        funcion encargada de generar la palabra dependiendo de la categoria que fue elegidad
        :param cat: cd ?'
        :return palabra para el  juego: 
        """
        try:
            self.categoria = cat
            if self.ids.sec:
                self.ids.sec.clear_widgets()    

            if cat=="Carreras":
                self.ids.pista.text = "Pista es una de la muchas " + cat + " . Que se imparten en la UIP."
                self.palabra = random.choice(self.lincen).upper()
            else:
                self.ids.pista.text = "Pista es un " + cat + "."
                self.palabra = random.choice(self.animales).upper()
            # Limpiamos las lista
            self.limpiar()

            # llenamos la lista con la palabra
            self.lista=[x for x in self.palabra]


            # Creacion de objetos
            self.ids.cont.disabled = False
            self.crear_secreta(self.palabra)
            self.crear_contenido()
            #print(self.lista, self.temp)
        except Exception as e:
            pass
            #print( e)
    def crear_secreta(self, palabra): # barra de la palabra secreta
       # #print(palabra)
        try:    
            if self.ids.sec:
                self.ids.sec.clear_widgets()
            tam= len(self.lista)
            if tam>8:
                ale = random.sample(self.lista, 3)
            elif tam>6:
                ale= random.sample(self.lista,  2)
            else:
                ale=random.sample(self.lista,  1)
            for x, c in enumerate(palabra.upper()):
                if c in ale:
                    bt = Button(id="bt_" + str(x), text=c,background_color=(0, 1, 255, 1) ,color=(0, 0, 0/255, 1))
                    self.temp.append(c)
                else:
                    bt = Button(text="_" ,background_color= (0, 1, 255, .5),color=(0, 0, 0/255, 1))
                    self.temp.append("_")
                self.ids.sec.add_widget(bt)
        except Exception as e:
            raise e

    def upate_secreta(self, arreglo):# actualizamos la pabla secreta
        try:    
            if self.ids.sec:
                self.ids.sec.clear_widgets()
            for let in arreglo:
                if let == "_":
                    bt = Button(text=let, background_color=(0, 1, 255, .5), color=(0, 0, 0 / 255, .5))
                else:
                    bt = Button(text=let,background_color=(0, 1, 255, 1) ,color=(0, 0, 0/255, 1))
                self.ids.sec.add_widget(bt)
        except Exception as e:
            raise e

    def crear_contenido(self):# abcdario de letra
        try:    
            if self.ids.cont:
                self.ids.cont.clear_widgets()
            for x in cadena.ascii_uppercase:
                if x in self.temp:
                    bt = Button(text=x,color=(0, 0, 0 / 255, 1), background_color=(100, 1, 1 / 255, 1))
                else:
                    bt = ToggleButton(text=x, color=(1, 1, 1, 1), background_color=(0, 0, 0 / 255, 1))
                    bt.bind(on_press=self.ev_buscar_letra)
                self.ids.cont.add_widget(bt)
        except Exception as e:
            raise e

    def ev_buscar_letra(self, evet):# evento de la letras
        try:    
            letra= evet.text
            #logica de puntos
            #print(self.contador)

            # # Busquedad de acentos tildes
            # if letra in self.acento:
            #     let=self.acento[letra]
            #     if let in self.lista:
            #         letra =let

            if letra in self.lista   :
                if letra in self.temp:
                    # ya esta generado por random
                    pass
                else:
                    for x in range(len(self.lista)):
                        if self.lista[x] ==letra:
                            self.temp[x]=letra
                            self.upate_secreta(self.temp)
                    if self.temp == self.lista:
                        #print("Ganaste")
                        self.terminar(True)
                    else:
                        pass
                        #print("Muy bien ")
            else:
                #print("Ops mala seleccion")
                self.contador += 1
                self.crear_Componentes()
                if self.contador == 7:
                    #print("Perdiste")
                    self.ids.cont.disabled = True  # desabilitamos la letras
                    self.terminar(False)


            #desabilitamos la letra

            evet.disabled = True
        except Exception as e:
            raise e
    def crear_Componentes(self):
        try:    
            if self.ids.compo:
                self.ids.compo.clear_widgets()
            lista_comp = ["data/1.png", "data/2.png","data/3.png",
                          "data/4.png","data/5.png","data/6.png",
                          "data/7.png"]
            tam= len(lista_comp)
            ind= self.contador-1
            ##print(ind, "  contador", self.contador, tam, "source ",lista_comp[ind])
            ima= Image( source=lista_comp[ind] )
            self.ids.compo.add_widget(ima)
            # for x in range(self.contador):
            #     bt = Image(source=lista_comp[x])
            #     self.ids.compo.add_widget(bt)
            #
            #     #print(x, tam)
        except Exception as e:
            raise e
    def terminar(self, opc):
        texto=""
        mensaje=""
        if opc==True:
            texto="".join(self.lista)
            texto= 'La Palabra fue '+texto
            bt= Image(source= "data/ganaste.png")
        else:
            texto="Ahorcado"
            pal = "".join(self.lista)
            texto="La palabra era  "+pal
            bt = Image(source="data/perdiste.jpg")

            #bt =Label(font_size= 40 ,text= mensaje)

        atras= Button(text="Intentarlo Nuevamente ")
        prin = Button(text="Menu Principal")
        prin.bind(on_press= self.ev_home)

        contenido= BoxLayout(orientation="vertical",spacing=25, padding=10, )
        contAtras = BoxLayout(spacing=25, padding=10)

        contAtras.add_widget(atras)
        contAtras.add_widget(prin)

        contenido.add_widget(bt)
        contenido.add_widget(contAtras)


        self.upate_secreta(x for x in texto.upper())
        #self.ids.compo.clear_widgets()

        #self.ids.compo.add_widget(contenido)
        self.popup = Popup(background_color= (0, 0, 181/255, 0.4),title=texto, content=contenido, auto_dismiss=False, size_hint=(0.6, 0.5),
        pos_hint={'center_x': .35, 'center_y': .4})

        atras.bind(on_press=self.ev_home)
        self.popup.open()

    def ev_home(self, home):
        self.generar_palabra(self.categoria)
        if home.text=="Menu Principal":
            self.current ="home"
        self.popup.dismiss()

    def limpiar(self):
        try:
            self.ids.compo.clear_widgets()
            self.lista=[]
            self.temp=[]

            self.contador=0
        except Exception as e:
            pass
            #print("error 01 - clear data "+str(e))
    


class AhorcadoApp(App):
    def build(self):
        return  Ventana()

    def on_pause(self):
        return True

if __name__ == "__main__":
    AhorcadoApp().run()
