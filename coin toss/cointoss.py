from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.app import App
from kivy.config import Config
from random import randint
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CornerRectangleWidget(Widget):
    def __init__(self, **kwargs):
        super(CornerRectangleWidget, self).__init__(**kwargs)
        with self.canvas:
                Rectangle(source='back.png', size=(450,415))

        with self.canvas:
                Rectangle(source='title.png', pos=(25,315), size=(400,100))
        
        with self.canvas:
                Rectangle(source='button_area.png', pos=(25,5), size=(400,200))

            
class cointossApp(App):
        #homeee=homepage()
        def build(self):
                App.get_running_app().stop()
                Config.set('graphics', 'width', '450')
                Config.set('graphics', 'height', '415')
                Config.set('graphics','resizable', True)
                self.layout = GridLayout()
                
                bt = Button(pos=(120,95),text='', color=(0,1,0,1),font_size=15, width=200, height=75, id=str('hjh'), background_normal='flip.png',background_down='flip_hover.png')
                t=CornerRectangleWidget()
                self.layout.add_widget(t)

                res=Button(pos=(25,210),text='', color=(0,1,0,1),font_size=15, width=400, height=100, id=str('res'), background_normal='null.png',background_down='null.png')
                reset_btn=Button(pos=(119,50),text='', color=(0,1,0,1),font_size=15, width=98, height=40, id=str('resett'), background_normal='reset.png',background_down='reset_hover.png')
                reset_btn.bind(on_release=self.press_reset)
                self.layout.add_widget(bt)
                self.layout.add_widget(reset_btn)
                quit_btn=Button(pos=(223,50),text='', color=(0,1,0,1),font_size=15, width=98, height=40, id=str('quit'), background_normal='quit.png',background_down='quit _hover.png')
                quit_btn.bind(on_release=self.press_quit)
                self.layout.add_widget(quit_btn)
                self.layout.add_widget(res)
                bt.bind(on_release=self.press_flip)
                
                
                
                return self.layout


        def press_flip(self,res):
               
                if (randint(0,1)==0):
                        res=Button(pos=(25,210),text='', color=(0,1,0,1),font_size=15, width=400, height=100, id=str('res1'), background_normal='head.png',background_down='head.png')
                        self.layout.add_widget(res)
                else:
                        res=Button(pos=(25,210),text='', color=(0,1,0,1),font_size=15, width=400, height=100, id=str('res1'), background_normal='tail.png',background_down='tail.png')
                        self.layout.add_widget(res)
                #return self.layout
        def press_quit(self,quit_btn):
                hom.run()
                
        def press_reset(self,res):
                res=Button(pos=(25,210),text='', color=(0,1,0,1),font_size=15, width=400, height=100, id=str('res1'), background_normal='null.png',background_down='null.png')
                self.layout.add_widget(res)
cointoss=cointossApp()
class homewidget(Widget):
    def __init__(self, **kwargs):
        super(homewidget, self).__init__(**kwargs)
        with self.canvas:
                Rectangle(source='back.png', size=(450,415))
        with self.canvas:
                Rectangle(source='title.png', pos=(25,315), size=(400,100))
cointoss=cointossApp()
class homepage(App):
    coin=cointossApp()
    def build(self):
        App.get_running_app().stop()
        Config.set('graphics', 'width', '450')
        Config.set('graphics', 'height', '415')
        Config.set('graphics','resizable', True)
        self.layout = GridLayout()
        ar=homewidget()
        self.layout.add_widget(ar)
        bt_play=Button(pos=(25,210),text='', color=(0,1,0,1),font_size=15, width=400, height=100, id=str('play'), background_normal='Play.png',background_down='Play_hover.png')
        self.layout.add_widget(bt_play)
        bt_play.bind(on_release=self.press_play)
        
        
        return self.layout

    def press_play(self,bt_play):
        
        self.coin.run()
            
        
        

#hom=homepage()
cointoss=cointossApp()
if __name__ == '__main__':
    hom=homepage()
    homepage().run()
