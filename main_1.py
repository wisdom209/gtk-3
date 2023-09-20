import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
	"""main window class"""
	def __init__(self):
		Gtk.Window.__init__(self,  title="My Window")

		self.button = Gtk.Button(label="Click me")
		self.button.connect('clicked', self.button_func)
		self.add(self.button)
	
	def button_func(self, widget):
		print("Clicked!")

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
