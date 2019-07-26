import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from util import *
from data_aug_for_yolo import *

flag = 1
class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.folder_label = QLabel('folder')
        self.folder_line = QLineEdit()
        self.folder_buttton = QPushButton("&Folder")
        self.folder_buttton.clicked.connect(self.folder_btn_clicked)
        grid.addWidget(self.folder_label, 0, 0)
        grid.addWidget(self.folder_line, 0, 1, 1, 5)
        grid.addWidget(self.folder_buttton, 0, 6)

        # self.warn1_label = QLabel()
        # grid.addWidget(self.warn1_label, 1, 1, 1, 5)

        self.resize_label = QLabel('resize')
        self.resize_line = QLineEdit('1.0')
        self.resize_line.setFixedWidth(28)
        self.rotate_label = QLabel('rotate')
        self.rotate_line = QLineEdit('45')
        self.rotate_line.setFixedWidth(28)
        grid.addWidget(self.resize_label, 2, 1)
        grid.addWidget(self.resize_line, 2, 2)
        grid.addWidget(self.rotate_label, 2, 4)
        grid.addWidget(self.rotate_line, 2, 5)

        self.v_flip_label = QLabel('v_flip')
        self.v_flip_cb = QCheckBox(self)
        self.h_flip_label = QLabel('h_flip')
        self.h_flip_cb = QCheckBox(self)
        grid.addWidget(self.v_flip_label, 4, 1)
        grid.addWidget(self.v_flip_cb, 4, 2)
        grid.addWidget(self.h_flip_label, 4, 4)
        grid.addWidget(self.h_flip_cb, 4, 5)

        self.pbar = QProgressBar(self)
        self.start_btn = QPushButton("&Start", self)
        self.start_btn.clicked.connect(self.start_btn_clicked)
        grid.addWidget(self.pbar, 5, 0, 1, 6)
        grid.addWidget(self.start_btn, 5, 6)

        self.setWindowTitle('Data Augmentation App')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def folder_btn_clicked(self):
        fname = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.folder_line.setText(fname)

    def start_btn_clicked(self):
        global flag
        flag *= -1
        if flag == -1:
            self.start_btn.setText("&Stop")
        else:
            self.start_btn.setText("&Start")
        check_directory(self.folder_line.)
        if

    def timerEvent(self, e):

        if self.step >= 100:

            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
