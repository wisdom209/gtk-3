import requests
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class MainWindow(Gtk.Window):
    """main window class"""
    def __init__(self):
        Gtk.Window.__init__(self)

        self.icon = Gtk.StatusIcon() 
        self.icon.set_from_file('logo.png')
        self.menu = Gtk.Menu()

        item1 = Gtk.MenuItem(label="Weather Report")
        item1.connect("activate", self.show_weather_report, "Weather Report")
        self.menu.append(item1)
        
        item2 = Gtk.MenuItem(label="Convert Currency")
        item2.connect("activate", self.convert_dollar_to_naira, "Currency Converter")
        self.menu.append(item2)
        
        item2 = Gtk.MenuItem(label="Trending movies")
        item2.connect("activate", self.show_latest_trending_movies, "Trending Movies")
        self.menu.append(item2)
        
        item3 = Gtk.MenuItem(label="Exit")
        item3.connect("activate", self.on_menu_item_activate, "Exit")
        self.menu.append(item3)

        self.menu.show_all()

        self.icon.connect('button-press-event', self.double_click_event_statusicon)

    def double_click_event_statusicon(self, icon, event_button):
        if event_button.type == Gdk.EventType.DOUBLE_BUTTON_PRESS and event_button.button == 1:
            self.menu.popup(None, None, None, None, event_button.button, event_button.time)

    def show_weather_report(self, widget, item_text):
        self.on_popup_menu_item_clicked(item_text)
        pass

    def show_latest_trending_movies(self, widget, item_text):
        self.on_popup_menu_item_clicked(item_text)
        pass

    def convert_dollar_to_naira(self, widget, item_text):
        self.on_popup_menu_item_clicked(item_text)
        pass

    def on_menu_item_activate(self, widget, item_text):
        print(f"Menu item activated: {item_text}")
        Gtk.main_quit()

    def on_popup_menu_item_clicked(self, item_text):
        dialog = Popup(self, item_text)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print('ok boss')
        elif response == Gtk.ResponseType.CANCEL:
            print('cancelled boxx')

        dialog.destroy()


class Popup(Gtk.Dialog):
    def __init__(self, parent, item_text):
        Gtk.Dialog.__init__(self, item_text, parent, Gtk.DialogFlags.MODAL, (
            "cancel popup", Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        ))

        self.set_default_size(100, 200)
        self.set_border_width(30)
        area = self.get_content_area()

        grid = Gtk.Grid()
        area.add(grid)
        
        if item_text == 'Weather Report':
            print('hello world')
            greeting_box = Gtk.Box()
            greeting_box.pack_start(Gtk.Label(label="Will it rain today?"), True, True, 0)
            grid.add(greeting_box)
            
            self.show_all()
            response = self.retrieve_weather_data()
            if response:
                weather_box = Gtk.Box()
                label = Gtk.Label(label="label")
                label.set_halign(Gtk.Align.START)
                weather_box.pack_start(label, True, True, 0)

                grid.attach_next_to(weather_box, greeting_box, Gtk.PositionType.BOTTOM, 80, 3)
                self.show_all()
            pass
        elif item_text == 'Currency Converter':
            pass
        elif item_text == 'Trending Movies':
            pass

        
        self.show_all()
    
    def retrieve_weather_data(self):
        import json

        data = requests.get('https://ipinfo.io')
        city = data.json().get('city')

        url = "https://api.weatherapi.com/v1/forecast.json"

        querystring = {"key":"d0e9895575b34ce58f913230232009", "q": city, "days": 2, "aqi": "no", "alerts":"yes"}

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers, params=querystring)
        
        try:
            if response.json():
                data = response.json()
                return data.get('forecast')['forecastday'][0]['day']
        except Exception:
            return None

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
Gtk.main()
