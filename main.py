from kivads import (
    BannerAd,
    InterstitialAd,
    KivAds,
    RewardedAd,
    RewardedInterstitial,
    TestID,
)

from kivymd.app import MDApp 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.label import Label
from time import sleep
import requests
    

class Mensaje_Popup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        
    def on_open(self):
        if not self.app.interstitial.is_loaded() or self.app.interstitial.is_dismissed() is True:
            self.app.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")

    def salir_popup(self):
        self.app.banner_ppal.show()
        self.app.interstitial.show()
        self.app.interstitial.load("ca-app-pub-3378097856628013/5566502540")
        self.dismiss()

class Pantalla(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.cont = 0

    def mostrar(self):
        try:
            self.ids.label.text = "Banner"
            self.app.banner_ppal.show()
        except:
            self.ids.label.text = "Sin Conexion a Internet"

    def cargar_anuncios(self):
        try:
            self.ids.label.text = "Cargando anuncios"
            self.app.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")
            #self.app.interstitial = InterstitialAd(TestID.INTERSTITIAL)
            self.reward = RewardedAd("ca-app-pub-3378097856628013/7371636283")
            #self.reward = RewardedAd(TestID.REWARD)
            self.reward_interstitial = RewardedInterstitial("ca-app-pub-3378097856628013/4574954697")
            self.app.banner_ppal.hide()
        except:
            self.ids.label.text = "Sin Conexion a Internet"

    def mostrar_intersticial(self):
        try:
            self.ids.label.text = "Intersticial"
            self.app.interstitial.show()
        except:
            self.ids.label.text = "Sin Conexion a Internet"
    
    def mostrar_video(self):
        try:
            self.ids.label.text = "Bonificado"
            self.app.reward.show()
        except:
            self.ids.label.text = "Sin Conexion a Internet"
        
    def mostrar_intersticia_bonificado(self):
        try:
            self.ids.label.text = "Intersticial Bonificado"
            self.app.reward_interstitial.show()
        except:
            self.ids.label.text = "Sin Conexion a Internet"
    
    def mostrar_popup(self):
        try:
            self.app.banner_ppal.hide()
            popup = Mensaje_Popup()
            popup.open()
        except:
            self.ids.label.text = "Sin Conexion a Internet"
    
    def load_banner(self, dt):
        self.ids.label.text = "Cargando Banner"
        #si no se ha cargado el banner  esperamos a que se carge en el proximo clock_shedule
        #cuando se ha cargado lo muestra y cancela el interval.
        if not self.app.banner_ppal.is_loaded():
            print(f"Cargando Banner: {self.app.banner_ppal.is_loaded()}")
        else:
            print(f"Banner Cargado: {self.app.banner_ppal.is_loaded()}")
            self.app.banner_ppal.show()
            self.app.event.cancel()
            self.ids.label.text = "Banner Cargado"
        

class MainApp(MDApp):

    def build(self):
        self.root = Builder.load_file("main.kv")
        self.title = "PruebaAnuncios"
        #self.ads = KivAds()
        self.ads = None
        #self.banner_ppal = BannerAd("ca-app-pub-3378097856628013/7930099553", int(Window.width), True)
        self.banner_ppal = None
        #self.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")
        self.interstitial = None
        #self.interstitial = InterstitialAd(TestID.INTERSTITIAL)
        #self.reward = RewardedAd("ca-app-pub-3378097856628013/7371636283")
        self.reward = None
        #self.reward = RewardedAd(TestID.REWARD)
        #self.reward_interstitial = RewardedInterstitial("ca-app-pub-3378097856628013/4574954697")
        self.reward_interstitial = None

         # Lanzamos la carga del banner en una corrutina
        self.event = None
        self.conexion = Clock.schedule_interval(self.conexion_admob, 1)
        #self.event = Clock.schedule_interval(Pantalla().load_banner, 1)
        
        return self.root
    
    def conexion_admob(self, dt):
        if self.comprobar_conexion():
            #iniciamos variables de kivAds
            self.ads = KivAds()
            self.banner_ppal = BannerAd("ca-app-pub-3378097856628013/7930099553", int(Window.width), True)
            self.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")
            self.reward = RewardedAd("ca-app-pub-3378097856628013/7371636283")
            self.reward_interstitial = RewardedInterstitial("ca-app-pub-3378097856628013/4574954697")
            #Cargamos el banner y cancelamos el interval al existir conexion
            self.event = Clock.schedule_interval(Pantalla().load_banner, 1)
            self.conexion.cancel()
        
        

    def comprobar_conexion(self):
        conexion = True
        try:
            request = requests.get("https://www.google.com", timeout=3)
        except (requests.ConnectionError, requests.Timeout):
            conexion = False
            print("Sin conexión a internet.")
        else:
            print("Con conexión a internet.")
        return conexion

if __name__ == '__main__':
    MainApp().run()