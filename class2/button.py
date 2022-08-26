import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Ico(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('pyqt5')
        self.setWindowIcon(QIcon('icon.ico'))

        qb = QPushButton('退出', self)
        qb.clicked.connect(QCoreApplication.instance().quit)
        qb.resize(70, 30)
        qb.move(50, 50)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())
