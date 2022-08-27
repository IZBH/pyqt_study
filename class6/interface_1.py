from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('准备就绪')
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('pyqt5')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
