# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bit\Desktop\aug.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from util2 import *
from data_aug_for_yolo import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.flag = False
        self.res = 1
        self.rot = 0
        self.sc = 1
        self.h_flip_flag = -1
        self.v_flip_flag = -1
        self.pgbar_num = 0

        # MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 450)
        self.centralwidget = QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 651, 51))
        # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout.setObjectName("horizontalLayout")

        self.dir_label = QLabel(self.horizontalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir_label.sizePolicy().hasHeightForWidth())

        self.dir_label.setSizePolicy(sizePolicy)
        self.dir_label.setBaseSize(QSize(0, 0))
        # self.dir_label.setObjectName("dir_label")
        self.horizontalLayout.addWidget(self.dir_label)

        self.dir_line = QLineEdit(self.horizontalLayoutWidget)
        # self.dir_line.setObjectName("dir_line")
        self.horizontalLayout.addWidget(self.dir_line)

        self.dir_warn_label = QLabel(self.centralwidget)
        self.dir_warn_label.setGeometry(QRect(95, 49, 241, 31))
        self.dir_warn_label.setText("")
        # self.dir_warn_label.setObjectName("dir_warn_label")

        self.find_btn = QPushButton(self.horizontalLayoutWidget)
        # self.find_btn.setObjectName("find_btn")
        self.horizontalLayout.addWidget(self.find_btn)

        self.option_box = QGroupBox(self.centralwidget)
        self.option_box.setGeometry(QRect(20, 80, 651, 341))
        # self.option_box.setObjectName("option_box")

        self.resize_label = QLabel(self.option_box)
        self.resize_label.setGeometry(QRect(67, 40, 41, 21))
        self.resize_label.setLayoutDirection(Qt.LeftToRight)
        # self.resize_label.setObjectName("resize_label")

        self.x_size = QLabel(self.option_box)
        self.x_size.setGeometry(QRect(67, 70, 41, 21))
        self.x_size.setLayoutDirection(Qt.LeftToRight)
        # self.x_size.setObjectName("x_size")

        self.x_line = QSpinBox(self.option_box)
        self.x_line.setGeometry(QRect(110, 70, 50, 20))
        # self.x_line.setObjectName("x_line")
        self.x_line.setRange(0, 2000)
        self.x_line.setSingleStep(1)

        self.y_size = QLabel(self.option_box)
        self.y_size.setGeometry(QRect(167, 70, 41, 21))
        self.y_size.setLayoutDirection(Qt.LeftToRight)
        # self.y_size.setObjectName("y_size")

        self.y_line = QSpinBox(self.option_box)
        self.y_line.setGeometry(QRect(210, 70, 50, 20))
        # self.y_line.setObjectName("y_line")
        self.y_line.setRange(0, 2000)
        self.y_line.setSingleStep(1)

        self.explain_size = QLabel(self.option_box)
        self.explain_size.setGeometry(QRect(267, 70, 280, 21))
        self.explain_size.setLayoutDirection(Qt.LeftToRight)
        # self.explain_size.setObjectName("explain_size")

        self.resize_line = QDoubleSpinBox(self.option_box)
        self.resize_line.setGeometry(QRect(110, 40, 38, 20))
        # self.resize_line.setObjectName("resize_line")
        self.resize_line.setRange(0, 4)
        self.resize_line.setSingleStep(0.1)


        self.rotate_label = QLabel(self.option_box)
        self.rotate_label.setGeometry(QRect(294, 40, 41, 20))
        # self.rotate_label.setObjectName("rotate_label")

        self.rotate_line = QSpinBox(self.option_box)
        self.rotate_line.setGeometry(QRect(337, 40, 45, 20))
        # self.rotate_line.setObjectName("rotate_line")
        self.rotate_line.setRange(0, 360)
        self.rotate_line.setSingleStep(1)

        self.degree_label = QLabel(self.option_box)
        self.degree_label.setGeometry(QRect(377, 40, 91, 20))
        # self.degree_label.setObjectName("degree_label")

        self.flip_label = QLabel(self.option_box)
        self.flip_label.setGeometry(QRect(22, 143, 31, 31))
        # self.flip_label.setObjectName("flip_label")

        self.v_flip_label = QLabel(self.option_box)
        self.v_flip_label.setGeometry(QRect(71, 143, 31, 31))
        # self.v_flip_label.setObjectName("v_flip_label")

        self.v_flip_cb = QCheckBox(self.option_box)
        self.v_flip_cb.setGeometry(QRect(117, 148, 16, 21))
        self.v_flip_cb.setText("")
        # self.v_flip_cb.setObjectName("v_flip_cb")

        self.h_flip_label = QLabel(self.option_box)
        self.h_flip_label.setGeometry(QRect(155, 143, 31, 31))
        # self.h_flip_label.setObjectName("h_flip_label")

        self.h_flip_cb = QCheckBox(self.option_box)
        self.h_flip_cb.setGeometry(QRect(203, 148, 16, 21))
        self.h_flip_cb.setText("")
        # self.h_flip_cb.setObjectName("h_flip_cb")

        self.rrs_label = QLabel(self.option_box)
        self.rrs_label.setGeometry(QRect(20, 35, 31, 31))
        # self.rrs_label.setObjectName("rrs_label")

        self.pgbar = QProgressBar(self.option_box)
        self.pgbar.setGeometry(QRect(70, 303, 450, 20))
        # self.pgbar.setObjectName("pgbar")
        self.pgbar.setMaximum(100)

        self.start_btn = QPushButton(self.option_box)
        self.start_btn.setGeometry(QRect(530, 301, 70, 23))
        # self.start_btn.setObjectName("start_btn")

        self.pg_label = QLabel(self.option_box)
        self.pg_label.setGeometry(QRect(10, 303, 61, 20))
        # self.pg_label.setObjectName("pg_label")

        self.rs_times_label = QLabel(self.option_box)
        self.rs_times_label.setGeometry(QRect(150, 40, 111, 20))
        # self.rs_times_label.setObjectName("rs_times_label")

        self.scale_label = QLabel(self.option_box)
        self.scale_label.setGeometry(QRect(70, 110, 41, 21))
        # self.scale_label.setObjectName("scale_label")

        self.scale_line = QDoubleSpinBox(self.option_box)
        self.scale_line.setGeometry(QRect(110, 110, 38, 20))
        # self.scale_line.setObjectName("scale_line")
        self.scale_line.setRange(0, 1)
        self.scale_line.setSingleStep(0.1)

        self.sc_times_label = QLabel(self.option_box)
        self.sc_times_label.setGeometry(QRect(150, 110, 111, 20))
        # self.sc_times_label.setObjectName("sc_times_label")

        self.rename_label = QLabel(self.option_box)
        self.rename_label.setGeometry(QRect(11, 183, 50, 31))
        # self.rename_label.setObjectName("rename_label")

        self.rename_exp_label = QLabel(self.option_box)
        self.rename_exp_label.setGeometry(QRect(80, 210, 50, 31))
        # self.rename_exp_label.setObjectName("rename_exp_label")

        self.all_rb = QRadioButton(self.option_box)
        self.all_rb.setGeometry(QRect(80, 190, 90, 16))
        # self.all_rb.setObjectName("all_rb")
        self.all_rb.setChecked(True)

        self.what_rb = QRadioButton(self.option_box)
        self.what_rb.setGeometry(QRect(280, 190, 111, 16))
        # self.what_rb.setObjectName("what_rb")

        self.no_rb = QRadioButton(self.option_box)
        self.no_rb.setGeometry(QRect(180, 190, 90, 16))
        # self.no_rb.setObjectName("no_rb")

        self.what_line = QLineEdit(self.option_box)
        self.what_line.setGeometry(QRect(397, 188, 71, 20))
        # self.what_line.setObjectName("what_line")
        self.what_line.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 736, 21))
        # self.menubar.setObjectName("menubar")
        self.menuImage_Data_Augmentation = QMenu(self.menubar)
        # self.menuImage_Data_Augmentation.setObjectName("menuImage_Data_Augmentation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.utilUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle("IDA(Image Data Augmentation)")
        self.dir_label.setText("Directory")
        self.dir_line.setPlaceholderText("Put image path")
        self.find_btn.setText("&Find")
        self.option_box.setTitle("Option")
        self.resize_label.setText("Resize")
        self.x_size.setText("X_size")
        self.y_size.setText("Y_size")
        self.explain_size.setText("px  (When Resize is 1, You can use X, Y size.)")
        self.resize_line.setValue(1)
        self.resize_line.setDecimals(1)
        self.rotate_label.setText("Rotate")
        self.rotate_line.setValue(0)
        self.degree_label.setText("  °(도) (Default)")
        self.flip_label.setText("Flip")
        self.v_flip_label.setText("v_flip")
        self.h_flip_label.setText("h_flip")
        self.rrs_label.setText("RRS")
        self.start_btn.setText("&Start")
        # self.stop_btn.setText("&Stop")
        self.pg_label.setText("Progress")
        self.rs_times_label.setText("times(배) (Default)")
        self.scale_label.setText("Scale")
        self.scale_line.setValue(1)
        self.scale_line.setDecimals(1)
        self.sc_times_label.setText("times(배) (Default)")
        self.rename_label.setText("Rename")
        self.rename_exp_label.setText("all")
        self.all_rb.setText(" &All")
        self.what_rb.setText(" &What you want")
        self.no_rb.setText(" &No")

    def utilUi(self, MainWindow):
        self.dir_line.textChanged[str].connect(self.dir_line_changed)
        self.find_btn.clicked.connect(self.dir_btn_clicked)
        self.start_btn.clicked.connect(self.start_btn_clicked)
        # self.stop_btn.clicked.connect(self.stop_btn_clicked)
        self.resize_line.valueChanged.connect(self.resize_line_changed)
        self.h_flip_cb.stateChanged.connect(self.h_flip_state_changed)
        self.v_flip_cb.stateChanged.connect(self.v_flip_state_changed)
        self.all_rb.clicked.connect(self.rename_changed)
        self.no_rb.clicked.connect(self.rename_changed)
        self.what_rb.clicked.connect(self.rename_changed)

    def dir_line_changed(self):
        self.start_btn.setEnabled(True)

    def dir_btn_clicked(self):
        fname = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:/Users/bit/Desktop', QFileDialog.ShowDirsOnly)
        self.dir_line.setText(fname)

    def resize_line_changed(self):
        if self.resize_line.value() == 1.0:
            self.x_line.setEnabled(True)
            self.y_line.setEnabled(True)
        else:
            self.x_line.setEnabled(False)
            self.y_line.setEnabled(False)

    def v_flip_state_changed(self):
        self.v_flip_flag *= -1

    def h_flip_state_changed(self):
        self.h_flip_flag *= -1

    def rename_changed(self):
        if self.all_rb.isChecked():
            self.what_line.setEnabled(False)
            self.rename_exp_label.setText("all")
        if self.no_rb.isChecked():
            self.what_line.setEnabled(False)
            self.rename_exp_label.setText("no")
        if self.what_rb.isChecked():
            self.what_line.setEnabled(True)
            self.rename_exp_label.setText("what")

    def start_btn_clicked(self):
        self.pgbar_num = 0
        self.flag = True
        self.augmentation()

    def augmentation(self):
        addr = self.dir_line.text()
        if check_directory(addr) == -1:
            self.dir_warn_label.setStyleSheet("color: red")
            self.dir_warn_label.setText("There's no directory")
            self.start_btn.setEnabled(False)
            self.flag = False
            self.start_btn.setText("&Start")
        else:
            self.dir_warn_label.clear()

            dir_list = make_directory()
            img_list = make_image_list()
            if img_list is None:
                self.dir_warn_label.setStyleSheet("color: red")
                self.dir_warn_label.setText("There's no image file (.jpg, .png, .bmp)")
                self.start_btn.setEnabled(False)
                self.flag = False

            else:
                for image_name in img_list:
                    img, bbox, save_path = read_yolo_data(dir_list, image_name)
                    if self.h_flip_flag == 1:
                        img, bbox = RandomFlip(img, bbox, mode=1)

                    if self.v_flip_flag == 1:
                        img, bbox = RandomFlip(img, bbox, mode=0)

                    img, bbox = RandomScale(img, bbox, self.scale_line.value())

                    if self.x_line.value()!= 0 and self.y_line.value()!= 0 and self.resize_line.value() == 1:
                        img = RandomResize(img, self.x_line.value(), self.y_line.value(), self.resize_line.value(), 0)
                    else:
                        img = RandomResize(img, (img.shape)[1], (img.shape)[0], self.resize_line.value(), 0)

                    img = RandomRotate(img, self.rotate_line.value())

                    if self.all_rb.isChecked():
                        image_name = image_name[:-4] + "_aug____"

                    if self.no_rb.isChecked():
                        pass

                    if self.what_rb.isChecked():
                        image_name = image_name[:-4] + self.what_line.text() + "____"

                    if bbox == []:
                        SaveImage(img, save_path, image_name)
                    else:
                        SaveImage(img, save_path, image_name, bbox)
                    img_num = len(img_list)
                    cnt_up = 100 / img_num
                    self.pgbar_num += cnt_up

                    self.pgbar.setValue(self.pgbar_num)

                    if self.flag == False:
                        return

                self.flag = False

# def exception_hook(exctype, value, traceback):
#     print(exctype, value, traceback)
#     sys._excepthook(exctype, value, traceback)
#     sys.exit(1)

if __name__ == "__main__":
    import sys

    # sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

