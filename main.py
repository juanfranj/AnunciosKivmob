from kivmob import KivMob, TestIds

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
    
    


class Pantalla(BoxLayout):
    ads = KivMob(TestIds.APP)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ads.new_banner('ca-app-pub-3940256099942544/6300978111',True)
        self.ads.new_interstitial(TestIds.INTERSTITIAL)

    def mostrar(self):
        self.ids.label.text = "Mostrar Banner"
        self.ads.request_banner()
        self.ads.show_banner()

    def quitar(self):
        self.ids.label.text = "Quitar Banner"
        self.ads.hide_banner()

    def mostrar_intersticial(self):
        self.ids.label.text = "Mostrar Intersticial"
        self.ads.request_interstitial()
        self.ads.show_interstitial()
    
    def mostrar_video(self):
        self.ids.label.text = "Mostrar video"

class MainApp(App):

    def build(self):
        self.root = Builder.load_file("main.kv")
        self.title = "PruebaAnuncios"
        return self.root
    

if __name__ == '__main__':
    MainApp().run()