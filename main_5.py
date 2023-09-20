# List Box, for making forms
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
	"""main window class"""
	def __init__(self):
		Gtk.Window.__init__(self,  title="My Window")
		self.set_border_width(10)
		
		listbox = Gtk.ListBox()

		listbox.set_selection_mode(Gtk.SelectionMode.NONE) # PREVENT CTRL A TYPE SELECTION

		self.add(listbox)

		#checkbox

		row_1 = Gtk.ListBoxRow()
		box_1 = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL, spacing=100)
		row_1.add(box_1)
		label_1 = Gtk.Label(label="Remember me")
		label_1.set_halign(Gtk.Align.START)
		checkbtn_1 = Gtk.CheckButton()
		box_1.pack_start(label_1, True, True, 0)
		box_1.pack_start(checkbtn_1, True, True, 0)
		listbox.add(row_1)
		
		#Toglle

		row_2 = Gtk.ListBoxRow()
		box_2 = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL, spacing=100)
		row_2.add(box_2)
		label_2 = Gtk.Label(label="Switch me")
		label_2.set_halign(Gtk.Align.START)
		switch_2 = Gtk.Switch()
		box_2.pack_start(label_2, True, True, 0)
		box_2.pack_start(switch_2, True, True, 0)
		listbox.add(row_2)

	

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
