#!/usr/bin/env python3
#class_events.py

''' This file defines the type of events.
Each of them will have different attributes and methods.
'''

# events definition
class event_maintenance(object):
    # define class for object event of type maintenance
    def __init__(self, prod_line, cnc_ref, creation_time):
        # intialize all fields to default values
        self.remark = ''
        self.time_end = ''
        self.event_ref = ''
        self.time_total = ''
        self.event_status = "open"

        # define event name
        self.unique_name = str(creation_time) + "_" + "mtn" + "_" + prod_line + "_" + cnc_ref 

        # register the basic event inforamtion
        self.time_creation = creation_time
        self.time_start = creation_time
        self.cnc_ref = cnc_ref
        self.prod_line = prod_line
        self.event_type = "maintenance"


    def add_remark(self, remark):
        self.remark = remark

    def add_event_ref(self, event_ref):
    	self.event_ref = event_ref

    def close_event(self, end_time, saving_folder):
    	# register end time
    	self.time_end = end_time

    	# calculate the total time
    	self.time_total = self.time_end - self.time_start

    	# update element status
    	self.event_status = "close"

    	# save Json file


