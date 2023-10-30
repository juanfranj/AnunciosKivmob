from kivads import (
    BannerAd,
    InterstitialAd,
    KivAds,
    RewardedAd,
    RewardedInterstitial,
    TestID,
)

from kivy.app import App 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
    
    


class Pantalla(BoxLayout):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def mostrar(self):
        self.ids.label.text = "Mostrar Banner"
        self.app.banner.show()

    def quitar(self):
        self.ids.label.text = "Quitar Banner"
        self.app.benner.hide()

    def mostrar_intersticial(self):
        self.ids.label.text = "Mostrar Intersticial"
    
    def mostrar_video(self):
        self.ids.label.text = "Mostrar video"

class MainApp(App):

    def build(self):
        self.root = Builder.load_file("main.kv")
        self.title = "PruebaAnuncios"
        self.ads = KivAds()
        self.banner = BannerAd(TestID.BANNER, int(Window.width))

        
        return self.root
    

if __name__ == '__main__':
    MainApp().run()