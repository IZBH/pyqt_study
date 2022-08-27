from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
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
        exitAct.triggered.connect(qApp.exit)

        saveMenu = QMenu('保存方式(&s)', self)
        saveAct = QAction(QIcon('save.png'), '保存...', self)
        saveAct.setShortcut('ctrl+s')

        saveasAct = QAction(QIcon('saveas.png'), '另存为...(&0)', self)
        saveAct.setStatusTip('文件另存为')

        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction(QIcon('new.png'), '新建(&N)', self)
        newAct.setShortcut('ctrl+n')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
