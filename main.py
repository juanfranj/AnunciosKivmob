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
from time import sleep
    

class Mensaje_Popup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.app.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")
        self.app.banner = BannerAd("ca-app-pub-3378097856628013/7930099553", int(int(Window.width)), True)
        
    
    def on_open(self):
        self.cargar_banner()

    def salir_popup(self):
        self.dismiss()
        self.app.interstitial.show()
    
    def cargar_banner(self):
        # while not self.app.banner.is_loaded():
        #     sleep(.5)
        sleep(3)
        self.app.banner.show()


class Pantalla(BoxLayout):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def mostrar(self):
        self.ids.label.text = "Banner"
        self.app.banner.show()

    def cargar_anuncios(self):
        self.ids.label.text = "Cargando anuncios"
        self.app.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")
        #self.app.interstitial = InterstitialAd(TestID.INTERSTITIAL)
        self.reward = RewardedAd("ca-app-pub-3378097856628013/7371636283")
        #self.reward = RewardedAd(TestID.REWARD)
        self.reward_interstitial = RewardedInterstitial("ca-app-pub-3378097856628013/4574954697")
        self.app.banner.hide()

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
        popup = Mensaje_Popup()
        popup.open()

class MainApp(MDApp):

    def build(self):
        self.root = Builder.load_file("main.kv")
        self.title = "PruebaAnuncios"
        self.ads = KivAds()
        
        self.banner = BannerAd("ca-app-pub-3378097856628013/7930099553", int(Window.width), True)
        #self.banner = BannerAd(TestID.BANNER, int(Window.width), True)
        self.interstitial = InterstitialAd("ca-app-pub-3378097856628013/5566502540")
        #self.interstitial = InterstitialAd(TestID.INTERSTITIAL)
        self.reward = RewardedAd("ca-app-pub-3378097856628013/7371636283")
        #self.reward = RewardedAd(TestID.REWARD)
        self.reward_interstitial = RewardedInterstitial("ca-app-pub-3378097856628013/4574954697")


        return self.root
    
    def on_start(self):
        while not self.banner.is_loaded():
            sleep(.5)
        self.banner.show()
    

if __name__ == '__main__':
    MainApp().run()