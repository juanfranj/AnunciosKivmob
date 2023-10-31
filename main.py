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

    def mostrar(self):
        self.ids.label.text = "Banner"
        self.app.banner_ppal.show()

    def cargar_anuncios(self):
        self.ids.label.text = "Cargando anuncios"
        self.app.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")
        #self.app.interstitial = InterstitialAd(TestID.INTERSTITIAL)
        self.reward = RewardedAd("ca-app-pub-3378097856628013/7371636283")
        #self.reward = RewardedAd(TestID.REWARD)
        self.reward_interstitial = RewardedInterstitial("ca-app-pub-3378097856628013/4574954697")
        self.app.banner_ppal.hide()

    def mostrar_intersticial(self):
        self.ids.label.text = "Intersticial"
        self.app.interstitial.show()
    
    def mostrar_video(self):
        self.ids.label.text = "Bonificado"
        self.app.reward.show()
    
    def mostrar_intersticia_bonificado(self):
        self.ids.label.text = "Intersticial Bonificado"
        self.app.reward_interstitial.show()
    
    def mostrar_popup(self):
        self.app.banner_ppal.hide()
        popup = Mensaje_Popup()
        popup.open()
        

class MainApp(MDApp):

    def build(self):
        self.root = Builder.load_file("main.kv")
        self.title = "PruebaAnuncios"
        self.ads = KivAds()
        
        self.banner_ppal = BannerAd("ca-app-pub-3378097856628013/7930099553", int(Window.width), True)
        #self.banner_popup = BannerAd("ca-app-pub-3378097856628013/7930099553", int(Window.width), True)#
        self.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")
        #self.interstitial = InterstitialAd(TestID.INTERSTITIAL)
        self.reward = RewardedAd("ca-app-pub-3378097856628013/7371636283")
        #self.reward = RewardedAd(TestID.REWARD)
        self.reward_interstitial = RewardedInterstitial("ca-app-pub-3378097856628013/4574954697")
        
        #self.root.add_widget(Label(text="Esperando a que se cargue el banner...", color = (0,0,0,1)))

         # Lanzamos la carga del banner en una corrutina
        Clock.schedule_once(self.load_banner, 5)
        
        
        return self.root
    
    
    def load_banner(self, dt):
        print(f"banner cargando: {self.banner_ppal.is_loaded()}")
        self.banner_ppal.show()
    
    # def on_start(self):
    #     print(f"on_start: {self.banner_ppal.is_loaded()}")
    
if __name__ == '__main__':
    MainApp().run()