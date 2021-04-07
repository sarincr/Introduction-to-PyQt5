import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    obj = QWidget()
    obj.resize(250, 150)
    obj.setWindowTitle('Hello World)
    obj.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
