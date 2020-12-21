from tkinter import *

master = Tk()

list_production_lines = ["G38 RK" , "C1/E2 RK" , "D2xx" , "EMP2 FLCA"]

variable = StringVar(master)
variable.set(list_production_lines[1]) # default value

w = OptionMenu(master, variable, *[x for x in list_production_lines])
w.pack()

mainloop()