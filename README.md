# GTK System Tray

This project demonstrates the use of GTK (GIMP Toolkit) in Python to create a system tray which on clicking shows a popup menu with different options and displays information based on user selections. In this example, we have two menu items: "Weather Report" and "Random Quote." Selecting each item shows relevant information in a GTK dialog.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Limitation](#Limitations)
- [Author](#Author)

## Prerequisites

Before running this application, ensure you have the following prerequisites installed on your system:

- Python 3.7 and above
- GTK 3 library (usually included with Linux distributions)
- [PyGObject](https://pygobject.readthedocs.io/) - Python bindings for GObject introspection libraries.
Run `sudo apt install libgtk-3-dev` if not available

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/wisdom209/gtk-popup-menu.git
   cd gtk-3
2. Install the needeed packages
`pip install -r requirements.txt`


## Usage
`python3 main.py`

You will see a system tray icon with an associated popup menu. Clicking on "Weather Report" or "Random Quote" will display relevant information in a dialog.


## Limitations
Project is dependent on external api and may break if these api endpoints are no longer valid

## Author
Ononiwu Ifeanyi Wisdom <ononiwuwisdom2@gmail.com> 
