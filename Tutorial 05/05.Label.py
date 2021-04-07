from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Class_Window(QMainWindow):
    def __init__(self):
        super(Class_Window,self).__init__()
        self.GUI_Function()

    def button_clicked(self):
        self.label.setText("Hello, You have pressed")
        self.Adj_Size()

    def GUI_Function(self):
        self.setGeometry(200, 200, 200, 200)
        self.setWindowTitle("Button and Label")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello, Welcome!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click")
        self.b1.clicked.connect(self.button_clicked)

    def Adj_Size(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = Class_Window()
    
    win.show()
    sys.exit(app.exec_())

window()
