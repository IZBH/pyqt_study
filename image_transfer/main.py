import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from main_windows import Ui_MainWindow
from img_class import transfer_img


class MyWindow(QMainWindow, Ui_MainWindow, transfer_img):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.f_name = ""

    def initUI(self):

        # 默认批量转换
        self.dir.setChecked(True)

        # 默认选中所有输出格式中的选项
        self.hfile.setChecked(True)
        self.bin_file.setChecked(True)
        self.align_bin.setChecked(True)
        self.merge_bin.setChecked(True)

        # 默认选中所有格式转换中的选项
        self.resize.setChecked(True)
        self.crop.setChecked(True)
        self.RGB565.setChecked(True)

        self.path_input.clicked.connect(self.get_path)
        self.start_transfer.clicked.connect(transfer_img)

    def get_path(self):
        if self.file.isChecked():
            self.f_name = QFileDialog.getOpenFileName()
        elif self.files.isChecked():
            self.f_name = QFileDialog.getOpenFileNames()
        elif self.dir.isChecked():
            self.f_name = QFileDialog.getExistingDirectory()

    def transfer_img(self):
        self.crop_list = (100, 200, 300, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
