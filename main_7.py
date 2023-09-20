#header bar
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    """main window class"""
    def __init__(self):
        Gtk.Window.__init__(self, title="My Window")
        self.set_border_width(10)

        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        self.set_titlebar(header)

        headerBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label(label="Welcome")
        headerBox.pack_start(label, True, True, 0)
        header.pack_start(headerBox)
        
        btn1 = Gtk.Button("btn 1")
        btn2 = Gtk.Button("btn 2")

        headerBox.pack_start(btn1, True, True, 0)
        headerBox.pack_start(btn2, True, True, 0)

        self.stack = Gtk.Stack()
        self.add(self.stack)

        page_label = Gtk.Label(label="page 1")
        self.stack.add(page_label)
        self.stack.remove(page_label)
        self.stack.show_all()        
       

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
