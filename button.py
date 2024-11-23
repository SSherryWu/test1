from calculator import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

#tmp = 0
#def button_func():
#    a = ui.lineEdit.text()
#    b = ui.lineEdit_2.text()
#    sum = float(a)+float(b)
#    sum_1 = str(sum)
#    ui.label_3.setText(sum_1)
#    global tmp
#    tmp = tmp + 1
#ui.pushButton.clicked.connect(button_func)

tmp = 0
def button_func():
    a=ui.lineEdit_2.text()
    b=ui.lineEdit.text()
    sum = float(a)+float(b)
    sum_1 = str(sum)
    ui.label_3.setText(sum_1)
    global tmp
    tmp = tmp + 1
    print(tmp)
ui.pushButton.clicked.connect(button_func)

tmp2=""
def press1():
    global tmp2
    tmp2=tmp2+"1"
    ui.label_3.setText(tmp2)
ui.pushButton_2.clicked.connect(press1)
def press2():
    global tmp2
    tmp2=tmp2+"2"
    ui.label_3.setText(tmp2)
ui.pushButton_3.clicked.connect(press2)
def pressClear():
    global tmp2
    tmp2="0"
    ui.label_3.setText(tmp2)
ui.pushButton_4.clicked.connect(pressClear)

widget.show()
app.exec_()

