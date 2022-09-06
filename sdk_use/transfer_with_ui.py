from PyQt5.QtWidgets import *
from transfer import Ui_MainWindow
from PyQt5.QtGui import QIcon
import sys
import pyperclip
from transfer_reg import RegTransfer


class Action(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Action, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('寄存器映射转换')
        self.setWindowIcon(QIcon('icon.png'))
        self.transfer_button.clicked.connect(self.transfer)
        self.show()

    def transfer(self):
        name = self.name.text()
        text = str(pyperclip.paste())
        reg = RegTransfer(name, text)

        # 是否进行切片
        if self.slice_check.isChecked():
            reg.slice = True
            if self.start.text():
                reg.start = int(self.start.text())
            else:
                reg.start = None

            if self.end.text():
                reg.end = int(self.end.text())
            else:
                reg.end = None

        result = reg.transfer()
        if result:
            # print(reg.out)
            pyperclip.copy(reg.out)
            self.text_result.setText(reg.out)
        else:
            print(reg.err)
            QMessageBox.warning(self, 'error', reg.err)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    action = Action()
    sys.exit(app.exec_())
