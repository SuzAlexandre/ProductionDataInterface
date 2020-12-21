#!/usr/bin/env python3.4 !!

# import package
import tkinter as tk
import datetime
import time
import functools
import sys
from PySide import QtGui
from PySide.QtCore import *

clock_time = ''


# define the application class containing the main HMI frame
class App(QtGui.QWidget):
        
        # define the initilisation method
        def __init__(self):
                super(App, self).__init__()

                self.init_UI()

        def init_UI(self):

                # register the screen configuration
                self.screen_height = QtGui.QDesktopWidget().screenGeometry().height()
                self.screen_width = QtGui.QDesktopWidget().screenGeometry(2).width()

                # define a standard size for all text
                self.default_font = QtGui.QFont('Fantasy', 15, QtGui.QFont.Light)

                # create the buttons for configuration, language change and quit the app
                self.configuration_Button = QtGui.QPushButton("Config")
                self.quit_app_Button = QtGui.QPushButton("Quit / 关") 
                self.choose_language_Button = QtGui.QPushButton("English / 英语")
                
                # create the event report label
                self.event_report_title = QtGui.QLabel("Events report")
                self.event_report_title.setFont(self.default_font)
                
                # create the buttons for line choice and CNC choice
                self.production_line_Button = QtGui.QPushButton("CNC choice")
                self.production_line_Button.setFont(self.default_font)
                self.production_line_Button.setMaximumHeight(1000) # to expand the button as much as possible
                self.cnc_Button = QtGui.QPushButton("Choose the production line")
                self.cnc_Button.setFont(self.default_font)
                self.cnc_Button.setMaximumHeight(1000) # to expand the button as much as possible

                # import the Chassix logo
                self.chassix_logo = QtGui.QLabel()
                self.chassix_logo.setGeometry(0,0,self.screen_width/4,200)
                self.chassix_logo.setPixmap(QtGui.QPixmap('Chassix_logo.jpg').scaled(self.chassix_logo.size(), Qt.KeepAspectRatio))

                # create the buttons for tool change, production brake and maintenance brake
                self.tool_change_Button = QtGui.QPushButton("Tool change")
                self.tool_change_Button.setFont(self.default_font)
                self.tool_change_Button.setStyleSheet("background-color:LightBlue")
                self.tool_change_Button.setMaximumHeight(1000) # to expand the button as much as possible
                self.production_brake_Button = QtGui.QPushButton("Production brake")
                self.production_brake_Button.setFont(self.default_font)
                self.production_brake_Button.setStyleSheet("background-color:Orange")
                self.production_brake_Button.setMaximumHeight(1000) # to expand the button as much as possible
                self.maintenance_brake_Button = QtGui.QPushButton("Maintenance brake")
                self.maintenance_brake_Button.setFont(self.default_font)
                self.maintenance_brake_Button.setStyleSheet("background-color:LightGreen")
                self.maintenance_brake_Button.setMaximumHeight(1000) # to expand the button as much as possible

                # create the new scrap button
                self.new_scrap_Button = QtGui.QPushButton("New scrap")
                self.new_scrap_Button.setFont(self.default_font)
                self.new_scrap_Button.setStyleSheet("background-color:Red")
                self.new_scrap_Button.setMaximumHeight(1000) # to expand the button as much as possible

                # create the round buttons canvas
                self.round_buttons_canvas = QtGui.QHBoxLayout()
                #self.round_buttons_canvas.addStretch()
                self.round_buttons_canvas.addWidget(self.choose_language_Button)
                self.round_buttons_canvas.addWidget(self.configuration_Button)
                self.round_buttons_canvas.addWidget(self.quit_app_Button)

                # create the main grid layout
                self.main_grid = QtGui.QGridLayout()
                self.main_grid.setSpacing(45)

                # add Chassix logo
                self.main_grid.addWidget(self.chassix_logo,1,0)
                

                # add the produciton line and CNC buttons
                self.main_grid.addWidget(self.production_line_Button,1,1)
                self.main_grid.addWidget(self.cnc_Button,1,2)

                # add the buttons for tool change, production brake and maintenance brake
                self.main_grid.addWidget(self.tool_change_Button,2,0,3,1)
                self.main_grid.addWidget(self.production_brake_Button,2,1,3,1)
                self.main_grid.addWidget(self.maintenance_brake_Button,2,2,3,1)

                # add the new scrap button
                self.main_grid.addWidget(self.new_scrap_Button,5,0,1,3)
                
                # insert the round buttons in the main grid
                self.main_grid.addLayout(self.round_buttons_canvas,1,3,1,1)

                # create the event report canvas
                self.event_canvas = QtGui.QVBoxLayout()
                #self.event_canvas.addStretch()
                self.event_canvas.addWidget(self.event_report_title)

                # insert the event canvas
                self.main_grid.addLayout(self.event_canvas,2,3,1,1)
                
                """
                # create the right canvas level 1
                self.right_canvas_LVL_1 = QtGui.QVBoxLayout()
                self.right_canvas_LVL_1.addStretch(1)
                self.right_canvas_LVL_1.addLayout(self.round_buttons_canvas_LVL_2)
                self.right_canvas_LVL_1.addLayout(self.event_canvas_LVL_2)
                
                # create the top canvas level 2 (chassix logo, production line choice and CNC choice)
                self.top_canvas_LVL_2 = QtGui.QHBoxLayout()
                self.top_canvas_LVL_2.addStretch(1)
                self.top_canvas_LVL_2.addWidget(self.chassix_logo)
                self.top_canvas_LVL_2.addWidget(self.production_line_Button)
                self.top_canvas_LVL_2.addWidget(self.cnc_Button)

                # create the main buttons canvas level 2 (including tool change, production brake adn maintenance brake)
                self.main_buttons_canvas_LVL_2 = QtGui.QHBoxLayout()
                self.main_buttons_canvas_LVL_2.addStretch(1)
                self.main_buttons_canvas_LVL_2.addWidget(self.tool_change_Button)
                self.main_buttons_canvas_LVL_2.addWidget(self.production_brake_Button)
                self.main_buttons_canvas_LVL_2.addWidget(self.maintenance_brake_Button)

                # create the new scrap canvas
                self.scrap_canvas_LVL_2 = QtGui.QVBoxLayout()
                self.scrap_canvas_LVL_2.addStretch(1)
                self.scrap_canvas_LVL_2.addWidget(self.new_scrap_Button)
                
                # create the left canvas level 1
                self.left_canvas_LVL_1 = QtGui.QVBoxLayout()
                self.left_canvas_LVL_1.addStretch(0)
                self.left_canvas_LVL_1.addLayout(self.top_canvas_LVL_2)
                self.left_canvas_LVL_1.addLayout(self.main_buttons_canvas_LVL_2)
                self.left_canvas_LVL_1.addLayout(self.scrap_canvas_LVL_2)
                
                # create the main canvas
                self.main_canvas = QtGui.QHBoxLayout()
                self.main_canvas.addStretch(0)
                self.main_canvas.addLayout(self.left_canvas_LVL_1)
                self.main_canvas.addLayout(self.right_canvas_LVL_1)
                """

                self.setLayout(self.main_grid)

                self.setWindowFlags(Qt.FramelessWindowHint)
                self.showFullScreen()
                self.setWindowTitle("Production tracking application")
                
def main():

        application = QtGui.QApplication(sys.argv)
        app = App()
        sys.exit(application.exec_())

if __name__ == '__main__':
        main()
