# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:51:55 2021

@author: hjkmo
"""
# Import the required libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk

import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw 

# Create an instance of tkinter frame or window
win=Tk()
win.title("Zoom Ready Window")

# Set the size of the window
win.geometry("350x350")

# import an image instead of drawing it
ico_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
def import_image(colorStatus): 
    if colorStatus == "green":
        filename = 'ZoomReady_StatusIcons_Green.jpg'
        img = Image.open(filename) 
    elif colorStatus == "yellow": 
        filename = 'ZoomReady_StatusIcons_Yellow.jpg'
        img = Image.open(filename)
    elif colorStatus == "red": 
        filename = 'ZoomReady_StatusIcons_Red.jpg'
        img = Image.open(filename)
    else: 
        filename = 'ZoomReady_StatusIcons_Black.jpg'
        img = Image.open(filename)
        print("Status Unknown")
    return img  

# Define a function for quit the window
def quit_window(icon, item):
   icon.stop()
   win.destroy()

# Define a function to show the window again
def show_window(icon, item):
   icon.stop()
   win.after(0,win.deiconify())

# Hide the window and show on the system taskbar
def hide_window():
   win.withdraw()
   img = import_image("green") 
   menu=(item('Quit', quit_window), item('Show', show_window))
   icon=pystray.Icon("name", img, "My System Tray Icon", menu)
   icon.run()

# Have an initial incidence of the icon
img = import_image("Black") 
menu=(item('Quit', quit_window), item('Show', show_window))
icon=pystray.Icon("name", img, "My System Tray Icon", menu)
icon.run()

win.protocol('WM_DELETE_WINDOW', hide_window)
win.mainloop()
  

