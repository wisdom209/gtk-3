# Grid layout
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
	"""main window class"""
	def __init__(self):
		Gtk.Window.__init__(self,  title="My Window")
		
		grid = Gtk.Grid()
		self.add(grid)


		btn1 = Gtk.Button(label="btn 1")
		btn2 = Gtk.Button(label="btn 2")
		btn3 = Gtk.Button(label="btn 3")
		btn4 = Gtk.Button(label="btn 4")
		btn5 = Gtk.Button(label="btn 5")
		btn6 = Gtk.Button(label="btn 6")

		grid.add(btn1)

		#params column, row, width, height
		grid.attach(btn2, 1, 0, 4, 1 )
		
		# parmas item, refers to, position, widht, height
		grid.attach_next_to(btn3, btn1, Gtk.PositionType.BOTTOM, 1, 3)

		grid.attach_next_to(btn4, btn2, Gtk.PositionType.BOTTOM, 2, 1)

		grid.attach_next_to(btn5, btn4, Gtk.PositionType.BOTTOM, 1, 1)

		grid.attach_next_to(btn6, btn5, Gtk.PositionType.RIGHT, 1, 1)

	

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
