import time
from PySide.QtCore import *
from PySide.QtGui import *
app = QApplication([])  # no need to import sys
# ----- start your widget test code ----
def tick():
    # get the current local time in hh:mm:ss format
    currtime = time.strftime('%H:%M:%S')
    lcd.display(currtime)
lcd = QLCDNumber()
lcd.setDigitCount(8)
# use style sheet to set background color
# color is a string in #RRGGBB format
blue = "#0000ff"
style_str = "QWidget {background-color: %s}"
lcd.setStyleSheet(style_str % blue)
# call tick() every second to update clock display
timer = QTimer()
timer.timeout.connect(tick)
timer.start(1000)
lcd.show()
# ---- end of widget test code -----
app.exec_()
h
