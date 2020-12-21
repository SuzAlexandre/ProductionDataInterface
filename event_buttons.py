#!/usr/bin/env python3
#event_buttons.py

import tkinter as tk

# events definition
class maintenance_event_button():
    # define class for object event of type maintenance
    def __init__(self,master,event_title):
        # intialize all fields to default values
        btn = tk.Button(master,
            text = event_title,
            font = ("Purisa", 20),
            fg = "black",
            bg = "white")

        btn.pack()
        btn["command"] = self._ON_CLICK_maintenance_event_button

    def _ON_CLICK_maintenance_event_button(self):
        print(self.btn.config())
        self["text"] = "Ben dis donc"