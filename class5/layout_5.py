import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit)

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('pyqt5')

        formlayout = QFormLayout()
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        introductionLabel = QLabel("简介")
        introductionLineedit = QTextEdit("")

        formlayout.addRow(nameLabel, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLineedit)
        self.setLayout(formlayout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())