import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gdk
import os.path



ui = Gtk.Builder()

ui.add_from_file("main.glade")



asd = os.path.expanduser('~/Projetos_kadabra/')


#mudar para conseguir selecioner pasta do projeto
projeto='mais_primeiro/'


if os.path.isdir(asd) == False:
    os.mkdir(asd)

class Handler:
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
        self.botao = ui.get_object("submit")
        self.label = ui.get_object("label")
        self.entrada = ui.get_object("entrada")
        self.selecionar_projeto = ui.get_object("selecionar_projeto")
        self.lista = ui.get_object("lista_lateral")


        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["New", "document-new"])
        self.liststore.append(["Open", "document-open"])
        self.liststore.append(["Save", "document-save"])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn(" ", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_pixbuf = Gtk.CellRendererPixbuf()

        column_pixbuf = Gtk.TreeViewColumn(" ", renderer_pixbuf, icon_name=1)
        treeview.append_column(column_pixbuf)

        self.lista.add(treeview)


    def onDestroy(self, *args):
        Gtk.main_quit()

    def clicar(self, *args):
        a= os.path.expanduser('~/Projetos_kadabra/')
        self.selecionar_projeto.set_location(a)
        asd = self.selecionar_projeto.get_location()
        
        print(asd)


    def new_project(self, *args):
        window.hide()
        win = ui.get_object("ide")
        win.show_all()

    def comandos(self, widget, event):
        entrada = Gdk.keyval_name(event.keyval)
        print(entrada)
    

ui.connect_signals(Handler())


window = ui.get_object("principal")
#window = ui.get_object("controle")
window.show_all()

Gtk.main()

