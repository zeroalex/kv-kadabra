import gi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gdk



from playkivy import *


carregar = """#texto para inicio
BoxLayout:
   orientation:'vertical'
   Label:
      text:'texto textoi'
   Button:
      text:'botao'

"""




ui = Gtk.Builder()

ui.add_from_file("main.glade")










class Handler:
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
        self.botao = ui.get_object("submit")
        self.label = ui.get_object("label")
        self.entrada = ui.get_object("entrada")
        
        self.texto = ui.get_object("texto")

        texto = self.texto.get_buffer()
        texto.insert(texto.get_start_iter(),carregar)

        self.carregar = ""



    def onDestroy(self, *args):
        Gtk.main_quit()

    def clicar(self, *args):
        window.hide()
        win = ui.get_object("ide")
        win.show_all()


    def new_project(self, *args):
        window.hide()
        win = ui.get_object("ide")
        win.show_all()

    def comandos(self, widget, event):
        entrada = Gdk.keyval_name(event.keyval)
        print(entrada)

    def recaregar(self, asd):
        pass    
    def visualizar(self,asd):
        texto = self.texto.get_buffer()

        print(texto.get_text(texto.get_start_iter(),texto.get_end_iter(),0 ))
        self.carregar = texto.get_text(texto.get_start_iter(),texto.get_end_iter(),0 )
    
    
        
        app = None
        app = PlaygroundApp(self.carregar)
        app.run()



ui.connect_signals(Handler())

window = ui.get_object("ide")

window.show_all()


Gtk.main()
