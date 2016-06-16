import random
import  string as cadena
import kivy
from kivy.app import  App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import  Button

# print( cadena.ascii_uppercase)
# print(cadena.ascii_letters)
# print(cadena.ascii_lowercase)
from kivy.uix.screenmanager import ScreenManager, Screen

nombre=""
class Ventana(ScreenManager):
    animales = ["perro", "gato", "abeja","conejo", "hormiga","oso"]
    lincen=["electronica","sistemas","industrial","maritima","redes"]
    lista=[""]
    temp=[""]
    contador = 0

    nombre = ""
    texto = ""
    def palabras(self, cat): # Palabra del ahorcado
        try:
            if self.ids.sec:
                self.ids.sec.clear_widgets()
            print(cat)
            if cat=="Carreras":
                self.nombre = random.choice(self.lincen).upper()

            else:
                #nombre="perro".upper()
                self.nombre = random.choice(self.animales).upper()
            # Limpiamos las lista
            self.limpiar()

            # llenamos la lista con la palabra
            self.lista=[x for x in self.nombre]

            # Creacion de objetos
            self.ids.cont.disabled = False
            self.crear_secreta(self.nombre)
            self.crear_contenido()
            print(self.lista, self.temp)
        except Exception as e:
            print( e)
    def crear_secreta(self, nombre): # barra de la palabra secreta
        print(nombre)
        try:    
            if self.ids.sec:
                self.ids.sec.clear_widgets()
            tam= len(self.lista)
            print(tam)
            if tam>8:
                ale = random.sample(self.lista, 3)
            elif tam>6:
                ale= random.sample(self.lista,  2)
            else:
                ale=random.sample(self.lista,  1)
            for x, c in enumerate(nombre.upper()):
                if c in ale:
                    bt = Button(id="bt_" + str(x), text=c)
                    self.temp.append(c)
                else:
                    bt = Button(text="_")
                    self.temp.append("_")
                self.ids.sec.add_widget(bt)
        except Exception as e:
            raise e

    def upate_secreta(self, arreglo):# actualizamos la pabla secreta
        try:    
            if self.ids.sec:
                self.ids.sec.clear_widgets()
            for let in arreglo:
                bt = Button(text=let)
                self.ids.sec.add_widget(bt)
        except Exception as e:
            raise e

    def crear_contenido(self):# abcdario de letra
        try:    
            if self.ids.cont:
                self.ids.cont.clear_widgets()
            for x in cadena.ascii_uppercase:
                bt = ToggleButton(text=x)
                bt.bind(on_press=self.ev_buscar_letra)
                self.ids.cont.add_widget(bt)
        except Exception as e:
            raise e

    def ev_buscar_letra(self, evet):# evento de la letras
        try:    
            letra= evet.text
            #logica de puntos
            if letra in self.lista:
                if letra in self.temp:
                    # ya esta 
                    print("generado por random ")
                    pass
                else:
                    for x in range(len(self.lista)):
                        if self.lista[x] ==letra:
                            self.temp[x]=letra
                            self.upate_secreta(self.temp)
                    if self.temp == self.lista:
                        print("Ganaste")
                        self.terminar(True)
                    else:
                        print("Muy bien ")
            elif self.contador==6:
                print("Perdiste")
                self.terminar(False)
            else:
                print("Ops mala seleccion")
                self.contador+=1
                self.crear_Componentes()

            #desabilitamos la letra
            evet.disabled = True
            print(self.contador)
        except Exception as e:
            raise e
    def crear_Componentes(self):
        try:    
            if self.ids.compo:
                self.ids.compo.clear_widgets()
            lista_comp = ["Base", "Base arriba", "Cabeza", "Cuerpo", "Brazos", "Pies"]
            tam= len(lista_comp)

            for x in range(self.contador):
                bt = Button(text=lista_comp[x])
                self.ids.compo.add_widget(bt)
                print(x, tam)
        except Exception as e:
            raise e
    def terminar(self, opc):
        texto=""
        mensaje=""
        try:    
            if opc==True:
                texto="Ganaste"
                mensaje=texto
            else:
                texto="Perdiste"
                pal = "".join(self.lista)
                mensaje="La palabra era: "+pal
            bt = Button(text= mensaje)

            self.upate_secreta(x for x in texto.upper())
            self.ids.cont.disabled = True  # desabilitamos la letras
            self.ids.compo.clear_widgets()
            self.ids.compo.add_widget(bt)
        except Exception as e:
            raise e

    def limpiar(self):
        try:    
            self.ids.compo.clear_widgets()
            self.lista.clear()
            self.temp.clear()
            self.contador=0
        except Exception as e:
            print("error 01 - clear data "+str(e))
        
class AhorcadoApp(App):
    def build(self):
        return  Ventana()

if __name__ == "__main__":
    AhorcadoApp().run()
