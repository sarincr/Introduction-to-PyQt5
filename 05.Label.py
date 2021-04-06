import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel,QPushButton

def clicked_button():
    print("Clicked")

def main():
        
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 200, 200)
    win.setWindowTitle("GUI")
    
    lab = QLabel(win)
    lab.setText("Hello World")
    lab.move(50,50)
    
    btn = QPushButton(win)
    btn.setText("Hello World")
    btn.clicked.connect(clicked_button)
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
