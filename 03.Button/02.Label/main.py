from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def BTN_Fun(self):
        self.label.setText("Pressed")


    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Main Window")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Not Pressed")
        self.label.move(10,10)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click")
        self.b1.clicked.connect(self.BTN_Fun)
        self.b1.move(100,100)
        




def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
