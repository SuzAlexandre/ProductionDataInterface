#!/usr/bin/env python3

# import package
import tkinter as tk
#from tkinter import ttk
import datetime
import time

# import events class
from class_events import *

# import functions
from get_event_unique_name import *


# create labels for pages
home_title = "Welcome to production data manager.\n Select main function"
data_viewer_title = "View datas"
data_recorder = "Record production data"
configuration = "Software configuration"

class App(tk.Frame):
        
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        min_clearance_x = screen_width*0.01
        min_clearance_y = screen_height*0.05

        self.master.maxsize(screen_width, screen_height)
        self.master.minsize(500, 400)
        self["padx"] = min_clearance_x
        self["cursor"]="hand2"
        self.pack()
        self.create_all_stuff()

    def create_all_stuff(self):

    
        # create title label
        self.welcome_label = tk.Label(self)
        self.welcome_label["text"]="Welcome to production management"
        self.welcome_label["fg"]="Black"
        self.welcome_label["justify"]="center"
        self.welcome_label["width"]=50
        self.welcome_label["wraplength"]=50
        self.welcome_label.place(x=50,y=10)
        self.welcome_label.pack(side="top")



        # create button 1
        self.left_side_button = tk.Button(self)
        self.left_side_button["text"]="Production brake"
        self.left_side_button["padx"]=5
        self.left_side_button["pady"]=2
        self.left_side_button["height"]=45
        self.left_side_button["width"]=45
        self.left_side_button["wraplength"]=100
        self.left_side_button["bg"]="#54FF9F"
        self.left_side_button.pack(side='left')
        #print(self.left_side_button.config())

        # create button 2
        self.center_side_button = tk.Button(self)
        self.center_side_button["text"]="Maintenance issue"
        self.center_side_button["padx"]=5
        self.center_side_button["pady"]=2
        self.center_side_button["height"]=45
        self.center_side_button["width"]=45
        self.center_side_button["wraplength"]=100
        self.center_side_button["bg"]="#F08080"
        self.center_side_button.pack(side='left')
        
        # create button 3
        self.right_side_button = tk.Button(self)
        self.right_side_button["text"]="Tool change"
        self.right_side_button["padx"]=5
        self.right_side_button["pady"]=2
        self.right_side_button["height"]=45
        self.right_side_button["width"]=45
        self.right_side_button["wraplength"]=100
        self.right_side_button["bg"]="#ADEAEA"
        self.right_side_button.pack(side='left')
    
        
# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")



# start the program
myapp.mainloop()





"""


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        self.hi_there.config(fg = "red")
#        self.config(height=400, width=400, bg="blue")
#        self.hi_there.config(height=20, width=20, bg = "blue",fg = "red")



class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = tk.StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())

root = tk.Tk()
app = App(master=root)
app.mainloop()






# create the home page for the function
root = Tk()
root.title("Production data manager")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

little_message = simpledialog()

#mainframe = ttk.Frame(root, padding='3 3 900 1440')
#mainframe.grid(column=0, row=0, sticky=(N,E,S,W))
#mainframe.columnconfigure(0, weight=1)
#mainframe.rowconfigure(0, weight=1)

# create the maint title
#Label(mainframe, text = home_title, fg="black", bg="blue").grid(column=2, row=1, sticky=(E,W))

# create the different buttons
#but_1 = Button(mainframe, text = data_viewer_title, bg="blue").grid(column=1, row=2, sticky=(E))

#Button(mainframe, text = data_recorder).grid(column=2, row=2, sticky=(E))
#Button(mainframe, text = configuration).grid(column=3, row=2, sticky=(E))                                                       

#for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


# a = get_event_unique_name('AAA', "qq", "007")

# print(a)

root.mainloop()
"""
