from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('pyqt5')

        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('ctrl+q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(exitAct)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
