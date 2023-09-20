"""Module implements a system tray using GTK-3"""

import threading, requests, textwrap3, gi, warnings
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

warnings.filterwarnings("ignore", category=DeprecationWarning) # filter out deprecation warnings, comment out to see them if need be

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
        """Popup Window Class"""
        Gtk.Dialog.__init__(self, item_text, parent, Gtk.DialogFlags.MODAL, (
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        ))

        self.set_default_size(100, 200)
        self.set_border_width(10)

        area = self.get_content_area()

        grid = Gtk.Grid()
        area.add(grid)
        
        if item_text == 'Weather Report' or item_text == "Random Quote":
            greeting_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

            greeting = "Will it rain today?" if item_text == "Weather Report" else "Your daily dose of inspiration"

            label_greeting = Gtk.Label()
            label_greeting.set_markup(f"<b>{greeting}</b>")
            label_greeting.set_halign(Gtk.Align.START)
            
            greeting_box.pack_start(label_greeting, True, True, 10)
            
            grid.add(greeting_box)
            
            global weather_response
     
            network_thread = threading.Thread(target=self.retrieve_data, args=[item_text])
            network_thread.daemon = True
            network_thread.start()

            # show loading screen while api request is ongoing
            self.header_box = Gtk.Box()
            self.label_network = Gtk.Label(label="Loading ...")
            self.label_network.set_halign(Gtk.Align.START)
            self.header_box.pack_start(self.label_network, True, True, 0)
            grid.attach_next_to(self.header_box, greeting_box, Gtk.PositionType.BOTTOM, 20, 3)
        else:
            Gtk.main_quit()
            
        self.show_all()
    
    def retrieve_data(self, item_text):
        # retrieve quote data
        try:
            url = "https://zenquotes.io/api/random/"

            quote_data = requests.get(url)

            quote_data = quote_data.json()

            # retrieve city data
            data = requests.get('https://ipinfo.io')
            city = data.json().get('city')

            # retrieve weather data
            url = "https://api.weatherapi.com/v1/forecast.json"

            querystring = {"key":"d0e9895575b34ce58f913230232009", "q": city, "days": 2, "aqi": "no", "alerts":"yes"}

            headers = {
                "Content-Type": "application/json"
            }

            response = requests.get(url, headers=headers, params=querystring)
            
            
            if response.json():
                data = response.json()
                weather_response = [data.get('forecast')['forecastday'][0]['day'], data['location']['name']]
                random_quote = quote_data
                
                Gdk.threads_enter()
                
                # display data
                if item_text == "Weather Report":
                    isLikely = "Likely" if weather_response[0]["daily_will_it_rain"] > 0 else "Unlikely"
                    
                    self.label_network.set_text(f"- Location: {weather_response[1]}\n- Report: {isLikely}\n- Detail: Expect {weather_response[0]['condition']['text'].lower()} today")
                elif item_text == "Random Quote":
                    quote = random_quote[0]['q']
                    formatted_quote = textwrap3.fill(quote, width=60)
                
                    self.label_network.set_text(f"{formatted_quote}\n\n- {random_quote[0]['a']}")

                Gdk.threads_leave()
        except Exception as e:
            self.label_network.set_text("Unable to fetch weather details.\nCheck your internet connection.")
     
if __name__ == "__main__":    
    window = MainWindow()
    window.connect('delete-event', Gtk.main_quit)
    Gtk.main()
