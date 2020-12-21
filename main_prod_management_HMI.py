#!/usr/bin/env python3.3 !!

# import package
from tkinter import *
import tkinter as tk
import datetime
import time
import functools
import sys

#from PySide import QtGui

clock_time = ''

# import all label names (default language = english)
from register_label_names import *

# import maintenance button class
import event_buttons

# import production line configuration 
#import production_lines_list

list_production_lines = ["G38 RK" , "C1/E2 RK" , "D2xx" , "EMP2 FLCA"]

# define the application class containing the main HMI frame
class App(tk.Frame):

        # setup char size and fonts
        global default_font
        default_font = 'Hind'
        global default_size
        default_size = 18
        
        # define the initilisation method
        def __init__(self, master=None):
                tk.Frame.__init__(self, master)

                # get screen height and width (in order to do a full screen app)
                self.screen_height = int(self.winfo_screenheight()*0.8)
                self.screen_width = self.winfo_screenwidth()

                # setup master geometry according to  full screen size
                self.master.geometry("%sx%s+%s+%s" % (self.screen_width,self.screen_height,0,0))

                self._create_top_canvas()

                self._create_main_middle_canvas()

                self._create_main_right_side_canvas()


        # define the top frame
        def _create_top_canvas(self):

                # defines top canvas size and place:
                global top_canvas_width
                top_canvas_width = int(self.screen_width*7/10)
                global top_canvas_height
                top_canvas_height = int(self.screen_height*1/10)
                global top_canvas_x
                top_canvas_x = int((self.screen_width *1/10)/3)
                global top_canvas_y
                top_canvas_y = int(0.025*self.screen_height)

                # create the top canvas
                self.top_canvas = tk.Canvas(self.master,
                        relief = "ridge",
                        bg = "white",
                        borderwidth = 3)
                
                self.top_canvas.place(x=top_canvas_x,
                        y=top_canvas_y,
                        width = top_canvas_width,
                        height = top_canvas_height)

                # define the start button size and place

                # define the line button size and place
                line_button_width = int((top_canvas_width - 0.05*4*top_canvas_width)/3)
                line_button_height = int(top_canvas_height*0.8)
                line_button_x = int(top_canvas_width*0.05)
                line_button_y = int(top_canvas_height*0.1)

                
                # create production line dropdown list
                variable = StringVar(self)
                variable.set(list_production_lines[1]) # default value

                self.line_button = tk.OptionMenu(self.top_canvas, variable, *[x for x in list_production_lines])
                self.line_button.place(x = line_button_x,
                        y = line_button_y,
                        width = line_button_width,
                        height = line_button_height)

                # create the line button
                #self.line_button = tk.Button(self.top_canvas,
                #        text = "Line selection",
                #        font = (default_font, default_size),
                #        fg = "black",
                #        bg = "white",
                #        command = self._ON_CLICK_line_button)
                #self.line_button.place(x = line_button_x,
                #        y = line_button_y,
                #        width = line_button_width,
                #        height = line_button_height)

                # define the CNC button size and place
                cnc_button_width = line_button_width
                cnc_button_height = line_button_height
                cnc_button_x = 2*line_button_x + line_button_width
                cnc_button_y = line_button_y
                
                # create the CNC button
                self.cnc_button = tk.Button(self.top_canvas,
                        text="Select a CNC",
                        font = (default_font, default_size),
                        fg="red",
                        bg="white")
                self.cnc_button.place(x = cnc_button_x,
                        y = cnc_button_y,
                        width = cnc_button_width,
                        height = cnc_button_height)
                self.cnc_button["command"]=self._ON_CLICK_cnc_button
                
                # create the clock
                self.time_label = tk.Label(self.top_canvas,
                        font = (default_font, default_size),
                        fg = "black",
                        bg = "yellow",
                        anchor = "w",
                        text = clock_time)
                self.time_label.place(x = int(0.480*self.screen_width),
                        y = int(0.1*0.33*self.screen_height),
                        width = int(0.08*self.screen_width),
                        height = int(0.1/3*self.screen_height))

                # define the time function
                def tic_tac():
                        global clock_time
                        # get computer time
                        current_time = time.strftime('%H:%M:%S')
                        # if time string has changed, update it
                        if current_time != clock_time:
                                clock_time = current_time
                                self.time_label.config(text=clock_time)
                        self.time_label.after(200, tic_tac)
                tic_tac()

                # define switch off button size and place
                switch_button_width = line_button_width / 2
                switch_button_height = line_button_height
                switch_button_x = 2*line_button_x + line_button_width * 2
                switch_button_y = line_button_y
                
                # create the switch button
                self.switch_button = tk.Button(self.top_canvas,
                        text="OFF",
                        font = (default_font, default_size),
                        fg="red",
                        bg="white")
                self.switch_button.place(x = switch_button_x,
                        y = switch_button_y,
                        width = switch_button_width,
                        height = switch_button_height)
                self.switch_button["command"]=self._ON_CLICK_switch_button



        # define the main middle canvas (the one with the 3 buttons)
        def _create_main_middle_canvas(self):
                
                # defines middle canvas size and place
                global middle_canvas_width
                middle_canvas_width = top_canvas_width
                global middle_canvas_height
                middle_canvas_height = self.screen_height-(3*top_canvas_y + top_canvas_height)
                global middle_canvas_x
                middle_canvas_x = top_canvas_x
                global middle_canvas_y
                middle_canvas_y = (2*top_canvas_y + top_canvas_height)

                # create the middle canvas
                self.main_middle_canvas = tk.Canvas(self.master,
                        relief = "ridge",
                        bg = "white",
                        borderwidth = 3)

                self.main_middle_canvas.place(x = middle_canvas_x,
                        y = middle_canvas_y,
                        width = middle_canvas_width,
                        height = middle_canvas_height)

                # define maintenance event button size and place
                maintenance_event_button_width = int((middle_canvas_width - 0.05*4*middle_canvas_width)/3 )
                maintenance_event_button_height = int((middle_canvas_height - 0.05*3*middle_canvas_height)*3/4)
                maintenance_event_button_x = int(0.05*middle_canvas_width)
                maintenance_event_button_y = int(0.05*middle_canvas_height)

                # add mainntenance event button
                self.main_button_new_maintenance_issue = tk.Button(self.main_middle_canvas,
                        text = "Start a maintenance event",
                        font = (default_font, default_size),
                        fg = "black",
                        bg = "white")

                self.main_button_new_maintenance_issue.place(x = maintenance_event_button_x,
                        y = maintenance_event_button_y,
                        width = maintenance_event_button_width,
                        height = maintenance_event_button_height)
                self.main_button_new_maintenance_issue["command"] = self._ON_CLICK_add_maintenance_event

                # define production break button size and place
                production_break_button_width = maintenance_event_button_width
                production_break_button_height = maintenance_event_button_height
                production_break_button_x = int(2*maintenance_event_button_x + maintenance_event_button_width)
                production_break_button_y = maintenance_event_button_y

                # add production break button
                self.main_button_new_production_break = tk.Button(self.main_middle_canvas,
                        text = "Start a production break",
                        font = (default_font, default_size),
                        fg = "black",
                        bg = "white")

                self.main_button_new_production_break.place(x = production_break_button_x,
                        y = production_break_button_y,
                        width = production_break_button_width,
                        height = production_break_button_height)
                self.main_button_new_production_break["command"] = self._ON_CLICK_add_production_break

                # define tool change button size and place
                tool_change_button_width = maintenance_event_button_width
                tool_change_button_height = maintenance_event_button_height
                tool_change_button_x = int(3*maintenance_event_button_x + 2*maintenance_event_button_width)
                tool_change_button_y = maintenance_event_button_y

                # add tool change button
                self.main_button_new_tool_change = tk.Button(self.main_middle_canvas,
                        text = "Tool change",
                        font = (default_font, default_size),
                        fg = "black",
                        bg = "white")

                self.main_button_new_tool_change.place(x = tool_change_button_x,
                        y = tool_change_button_y,
                        width = tool_change_button_width,
                        height = tool_change_button_height)
                self.main_button_new_tool_change["command"] = self._ON_CLICK_add_tool_change

                # define the scrap button size
                scrap_button_width = int(3*maintenance_event_button_width + 2*maintenance_event_button_x)
                scrap_button_height = int((middle_canvas_height - 0.05*3*middle_canvas_height)*1/4)
                scrap_button_x = maintenance_event_button_x
                scrap_button_y = 2*maintenance_event_button_y + maintenance_event_button_height

                # add scrap button
                self.main_button_new_scrap = tk.Button(self.main_middle_canvas,
                        text = "Add scrap",
                        font = (default_font, default_size),
                        fg = "black",
                        bg = "white")

                self.main_button_new_scrap.place(x = scrap_button_x,
                        y = scrap_button_y,
                        width = scrap_button_width,
                        height = scrap_button_height)
                self.main_button_new_scrap["command"] = self._ON_CLICK_add_scrap

        # define the main right side canvas (to do a daily record of the events)
        def _create_main_right_side_canvas(self):
                
                # defines right side canvas size and place
                global right_side_canvas_width
                right_side_canvas_width = int((self.screen_width-3*top_canvas_x)*1/4)
                global right_side_canvas_height
                right_side_canvas_height = int(self.screen_height-(2*top_canvas_y))
                global right_side_canvas_x
                right_side_canvas_x = int(top_canvas_x*2 + top_canvas_width)
                global right_side_canvas_y
                right_side_canvas_y = top_canvas_y

                # create the middle canvas
                self.main_right_side_canvas = tk.Canvas(self.master,
                        relief = "ridge",
                        bg = "blue",
                        borderwidth = 3)

                self.main_right_side_canvas.place(x = right_side_canvas_x,
                        y = right_side_canvas_y,
                        width = right_side_canvas_width,
                        height = right_side_canvas_height)

        '''

        Start the definition of the ON_CLICK function for top canvas

        '''

        def _ON_CLICK_cnc_button(self):
                # try to hide some of the elements
                self.main_middle_canvas.destroy()
                print("remove or not?")
                #self.master.destroy()

        def _ON_CLICK_switch_button(self):
                self.master.destroy()

        def _ON_CLICK_line_button(self):
                self.production_line_selection_main = tk.Toplevel()
                self.production_line_selection_main.title("Change production line")

                msg = tk.Message(self.production_line_selection_main, text="Select a prodution line")
                msg.pack()

                # loop on the production lines to create the buttons
                for cmpt in range(len(list_production_lines)):
                        tk.Button(self.production_line_selection_main,
                                text = list_production_lines[cmpt],
                                font = ("Purisa",20),
                                command = functools.partial(self._ON_CLICK_production_line_selection,
                                        list_production_lines[cmpt])).pack()

        def _ON_CLICK_production_line_selection(self,production_line_ref):
                self.line_button["text"] = production_line_ref
                self.production_line_selection_main.destroy()

        '''
        Start the definition of the ON_CLICK function for middle canvas
        '''

        def _ON_CLICK_add_maintenance_event(self):
                self.add_maintenance_event_main = tk.Toplevel()
                self.add_maintenance_event_main["takefocus"]="True"
                self.add_maintenance_event_main.title("Add a maintenance event")

                maintenance_event_list = ["Event 01" , "Event 02" , "Event 03"]
                maintenance_event_reference_numbers = [1 , 2 , 3]

                for cmpt in range(len(maintenance_event_list)):
                        tk.Button(self.add_maintenance_event_main,
                                text = maintenance_event_list[cmpt],
                                font = ("Purisa",20),
                                command = functools.partial(self._ON_CLICK_activate_maintenance_event, 
                                        maintenance_event_reference_numbers[cmpt])).pack()

        def _ON_CLICK_activate_maintenance_event(self,ref_number):
                print(ref_number)
                print(clock_time)
                self.add_maintenance_event_main.destroy()

        def _ON_CLICK_add_production_break(self):
                self.main_button_new_production_break["text"] = "Back to production"
                self.production_break_start_time = time.time()
                self.main_button_new_production_break["command"] = self._ON_CLICK_end_production_break

        def _ON_CLICK_end_production_break(self):
                self.main_button_new_production_break["text"] = "Start a production break"
                self.maintenance_break_time = time.time() - self.production_break_start_time
                print("Production down time : " + str(round(self.maintenance_break_time,2)) + " seconds")
                self.main_button_new_production_break["command"] = self._ON_CLICK_add_production_break
        
        def _ON_CLICK_add_tool_change(self):
                print("Tool change !!!")

        def _ON_CLICK_add_scrap(self):
                self.main_button_new_scrap["text"] = "Rhooo"
                print("coucou")

# create an App instance
myapp = App()

# run the app
myapp.mainloop()
