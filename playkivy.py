import kivy
kivy.require('1.9.1')


from kivy.app import App
from kivy.lang import Builder
from kivy.lang import ParserException
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
 
from kivy.base import runTouchApp, async_runTouchApp, stopTouchApp

"""

#texto para inicio
BoxLayout:
   orientation:'vertical'
   Label:
      text:'texto textoi'
   Button:
      text:'botao'

"""

class PlaygroundScreen(Screen):
    content_pane = ObjectProperty(None)
    editor_pane = ObjectProperty(None)
    kivy_text = "test"

    def __init__(self,entrada):
        self.entrada = entrada
        super(PlaygroundScreen,self).__init__()

        self.creation = Builder.load_string(self.entrada)
        
        self.content_pane.add_widget(self.creation)

    
    def start(self):

        stopTouchApp()


class PGScreenManager(ScreenManager):
    pass

class PlaygroundApp(App):
    def __init__(self,entrada):
        self.entrada = entrada
        super(PlaygroundApp,self).__init__()

    def build(self):
        
        self.pgs = PlaygroundScreen(self.entrada)
        
        return self.pgs

