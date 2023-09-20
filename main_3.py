# box and passing functions
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
	"""main window class"""
	def __init__(self):
		Gtk.Window.__init__(self,  title="My Window")
		
		self.box = Gtk.Box(spacing=10)
		self.add(self.box)

		self.bacon_btn = Gtk.Button(label="Bacon")
		self.bacon_btn.connect("clicked", self.btn_clicked, self.bacon_btn)
		self.box.pack_end(self.bacon_btn, True, True, 0 )
		
		self.tuna_btn = Gtk.Button(label="Tuna")
		self.tuna_btn.connect("clicked", self.btn_clicked, self.tuna_btn)
		self.box.pack_start(self.tuna_btn, True, True, 0 )

	def btn_clicked(self, widget, button):
		print(button.get_label())

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
