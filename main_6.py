import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    """main window class"""
    def __init__(self):
        Gtk.Window.__init__(self, title="My Window")
        self.set_border_width(10)
        
        box = Gtk.VBox(orientation=Gtk.Orientation.VERTICAL, spacing=10) 

        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(2000)

        check_btn = Gtk.CheckButton("Check me")
        main_area.add_named(check_btn, "check_name")
        
        # Create a label widget
        label = Gtk.Label()
        label.set_markup("<big>big text</big>")

        main_area.add_named(label, "label_name")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)
        box.pack_start(stack_switcher, False, False, 0)
        box.pack_start(main_area, True, True, 0)

        self.add(box)  # Add the 'box' to the window

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
