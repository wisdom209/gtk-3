import json
import requests
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

def random_quote():
    print('hello')
    url = "https://zenquotes.io/api/random/"

    data = requests.get(url)

    print(data.json())
    
    return data.json()


def retrieve_data():
    url = "https://zenquotes.io/api/random/"

    quote_data = requests.get(url)

    quote_data = quote_data.json()


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
            return ([data.get('forecast')['forecastday'][0]['day'], data['location']['name']], quote_data)
    except Exception:
        return None

weather_response = None
random_quote = None

try:
    weather_response = retrieve_data()[0]
    random_quote = retrieve_data()[1]
except Exception:
    pass

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
        
        item2 = Gtk.MenuItem(label="Random Quote")
        item2.connect("activate", self.get_random_quote, "Random Quote")
        self.menu.append(item2)
        
        item3 = Gtk.MenuItem(label="Exit")
        item3.connect("activate", self.on_menu_item_exit, "Exit")
        self.menu.append(item3)

        self.menu.show_all()

        self.icon.connect('button-press-event', self.double_click_event_statusicon)

    def double_click_event_statusicon(self, icon, event_button):
        if event_button.type == Gdk.EventType.DOUBLE_BUTTON_PRESS and event_button.button == 1:
            self.menu.popup(None, None, None, None, event_button.button, event_button.time)

    def show_weather_report(self, widget, item_text):
        self.on_popup_menu_item_clicked(item_text)
        pass

    def get_random_quote(self, widget, item_text):
        self.on_popup_menu_item_clicked(item_text)
        pass

    def on_menu_item_exit(self, widget, item_text):
        Gtk.main_quit()

    def on_popup_menu_item_clicked(self, item_text):
        dialog = Popup(self, item_text)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            pass
        # elif response == Gtk.ResponseType.CANCEL:
        #     pass

        dialog.destroy()


class Popup(Gtk.Dialog):
    def __init__(self, parent, item_text):
        Gtk.Dialog.__init__(self, item_text, parent, Gtk.DialogFlags.MODAL, (
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        ))

        self.set_default_size(100, 200)
        self.set_border_width(10)

        area = self.get_content_area()

        grid = Gtk.Grid()
        area.add(grid)
        
        if item_text == 'Weather Report':
            greeting_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

            label_greeting = Gtk.Label()
            label_greeting.set_markup("<big>Will it rain today?</big>")
            label_greeting.set_halign(Gtk.Align.START)
            
            greeting_box.pack_start(label_greeting, True, True, 10)
            
            grid.add(greeting_box)
            
            global weather_response
            
            if weather_response:
                location= f"- Location: {weather_response[1]}"
                likely = "- Report: Likely" if weather_response[0]["daily_will_it_rain"] > 0 else "- Unlikely"
                expectation = f"- Detail: Expect {weather_response[0]['condition']['text'].lower()} today"
                
                weather_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
                
                label_location = Gtk.Label(label=location)
                label_location.set_halign(Gtk.Align.START)
                
                label_likely = Gtk.Label(label=likely)
                label_likely.set_halign(Gtk.Align.START)
                
                label_expectation = Gtk.Label(label=expectation)
                label_expectation.set_halign(Gtk.Align.START)

                weather_box.pack_start(label_location, True, True, 0)
                weather_box.pack_start(label_likely, True, True, 0)
                weather_box.pack_start(label_expectation, True, True, 0)

                grid.attach_next_to(weather_box, greeting_box, Gtk.PositionType.BOTTOM, 80, 3)
            else:
                weather_box = Gtk.Box()
                label_network = Gtk.Label(label="Unable to fetch data.\nMake sure you have internet connection.")
                label_network.set_halign(Gtk.Align.START)
                weather_box.pack_start(label_network, True, True, 0)
                grid.attach_next_to(weather_box, greeting_box, Gtk.PositionType.BOTTOM, 20, 3)

        elif item_text == 'Random Quote':
            global random_quote
            
            if random_quote:
                quote= f"{random_quote[0]['q']}"
                author= f"- {random_quote[0]['a']}"

                title_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
                title_box.set_size_request(80, 150)

                label_title = Gtk.Label()
                label_title.set_markup("<big>Your daily dose of inspiration</big>")
                label_title.set_halign(Gtk.Align.START)
                
                label_quote = Gtk.Label(label=f"{quote}")
                label_quote.set_width_chars(60)
                label_quote.set_halign(Gtk.Align.START)
                
                label_author = Gtk.Label()
                label_author.set_markup(f"<small>{author}</small>")
                label_author.set_halign(Gtk.Align.START)

                title_box.pack_start(label_title, True, True, 0)
                title_box.pack_start(label_quote, False, False, 0)
                title_box.pack_start(label_author, True, True, 0)

                grid.add(title_box)
            else:
                title_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
                
                label_title = Gtk.Label()
                label_title.set_markup("<big>Your daily dose of inspiration</big>")
                label_title.set_halign(Gtk.Align.START)
                
                label_network = Gtk.Label(label="Unable to fetch data.\nMake sure you have internet connection.")
                label_network.set_halign(Gtk.Align.START)

                title_box.pack_start(label_title, True, True, 5)
                title_box.pack_start(label_network, True, True, 0)
                grid.add(title_box)
            
        self.show_all()


window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
Gtk.main()
