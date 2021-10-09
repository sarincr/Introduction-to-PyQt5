from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

def DemoApp():
    app =QApplication(sys.argv)
    root = QMainWindow()
    root.setGeometry(200,200,200,200)
    root.setStyleSheet("background-color: green;")
    root.setWindowTitle("Hello World")
    root.show()
    sys.exit(app.exec_())


DemoApp()
