import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qt_test import *

class MyApp(QWidget):

        def __init__(self):
            super().__init__()

            # 디렉토리 선택 버튼
            self.select_btn = QPushButton('&select', self)
            self.select_btn.setCheckable(True)
            self.select_btn.toggle()
            self.select_btn.clicked.connect(self.select_button_clicked)

            self.open_dialog = QFileDialog()  # directory 선택을 위한 QFileDialog

            # Run button
            self.run_btn = QPushButton('&Run', self)
            self.run_btn.setCheckable(True)
            self.run_btn.toggle()
            self.run_btn.clicked.connect(self.run_button_clicked)

            # cancle button
            self.cancel_btn = QPushButton('&Cancel', self)
            self.cancel_btn.setCheckable(True)
            self.cancel_btn.toggle()
            self.cancel_btn.clicked.connect(QCoreApplication.instance().quit)
            
            # flip mode checkbox
            self.hflip_cb = QCheckBox("hflip", self)
            self.vflip_cb = QCheckBox("vflip", self)

            
            # rescale spinbox
            self.scale = QDoubleSpinBox()
            self.scale.setMinimum(0.3)
            self.scale.setMaximum(1.0)
            self.scale.setSingleStep(0.01)
            self.scale.setValue(1.00)

            # rotate angle spinbox
            self.angle= QSpinBox()
            self.angle.setRange(0,360)

            # resize contents
            self.resolution_rb = QRadioButton("Resolution")
            self.resolution_rb.clicked.connect(self.resize_rb_clicked)
            self.scale_rb = QRadioButton("Scale")
            self.scale_rb.clicked.connect(self.resize_rb_clicked)
            self.res_x = QLineEdit()
            self.res_x.setInputMask("0000")
            self.res_y = QLineEdit()
            self.res_y.setInputMask("0000")
            self.resize_scale = QLineEdit()
            self.resize_scale.setInputMask("0.00")

            #rename
            self.prefix = QLineEdit()
            self.prefix.setReadOnly(True)
            self.prefix_cb = QCheckBox("prefix", self)
            self.prefix_cb.stateChanged.connect(self.checkBoxState)
            self.suffix = QLineEdit()
            self.suffix.setReadOnly(True)
            self.suffix_cb = QCheckBox("suffix", self)
            self.suffix_cb.stateChanged.connect(self.checkBoxState)

            # 경고
            self.alert = QLabel()

            # directory path QLineEdit
            self.path_text= QLineEdit()
            self.path_text.setReadOnly(True)
            
            self.initUI()

        def initUI(self):

            # Layout
            grid = QGridLayout()
            self.setLayout(grid)

            # run / cancel layout
            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.addWidget(self.run_btn)
            hbox.addWidget(self.cancel_btn)
            hbox.addStretch(1)

            # flip chboxes layout
            flip_box = QHBoxLayout()
            flip_box.addWidget(self.hflip_cb)
            flip_box.addWidget(self.vflip_cb)

            # resize sub grid lay out
            sub_grid = QGridLayout()

            ## resolution hbox
            resolution_hbox = QHBoxLayout()
            resolution_hbox.addWidget(QLabel("x"))
            resolution_hbox.addWidget(self.res_x)
            resolution_hbox.addWidget(QLabel("y"))
            resolution_hbox.addWidget(self.res_y)

            ## resize sub_grid 위젯, 레이어 추가
            sub_grid.addWidget(self.scale_rb,0,0)
            sub_grid.addWidget(self.resize_scale,0,1)
            sub_grid.addWidget(self.resolution_rb,1,0)
            sub_grid.addLayout(resolution_hbox, 1,1)

            # rename sub layer
            prefix_vbox = QVBoxLayout()
            prefix_vbox.setAlignment(Qt.AlignCenter)
            prefix_vbox.addWidget(self.prefix_cb)
            prefix_vbox.addWidget(self.prefix)

            suffix_vbox = QVBoxLayout()
            suffix_vbox.setAlignment(Qt.AlignCenter)
            suffix_vbox.addWidget(self.suffix_cb)
            suffix_vbox.addWidget(self.suffix)

            rename_hbox = QHBoxLayout()
            rename_hbox.addLayout(prefix_vbox)
            rename_hbox.addWidget(QLabel("    name    "))
            rename_hbox.addLayout(suffix_vbox)

            grid.addWidget(QLabel('Directory select'), 0, 0)
            grid.addWidget(QLabel('Flip mode'), 1, 0)
            grid.addWidget(QLabel('Rescale'), 2, 0)
            grid.addWidget(QLabel('Rotate angle'), 3, 0)
            grid.addWidget(QLabel('Resize'),4,0)
            grid.addWidget(QLabel('Rename'),5,0)
            grid.addLayout(hbox, 6,0,1,3)
            grid.addWidget(self.alert, 7,0,2,3)

            grid.addWidget(self.path_text, 0, 1)
            grid.addLayout(flip_box,1,1)
            grid.addWidget(self.scale, 2, 1)
            grid.addWidget(self.angle, 3, 1)
            grid.addLayout(sub_grid,4,1,1,2)
            grid.addLayout(rename_hbox,5,1,1,2)
            grid.addWidget(self.select_btn,0,2)

            self.setWindowTitle('Augmentator')
            self.setGeometry(300, 300, 500, 200)
            self.show()

        def select_button_clicked(self):
            if not self.path_text.text():
                button_path = os.path.expanduser("~")
            else:
                button_path = self.path_text.text()

            button_path = self.open_dialog.getExistingDirectory(self, "Directory Path Select", button_path)

            if button_path:
                self.path_text.setText(button_path)

        def checkBoxState(self):
            if self.prefix_cb.isChecked():
                self.prefix.setReadOnly(False)
            else:
                self.prefix.setText("")
                self.prefix.setReadOnly(True)

            if self.suffix_cb.isChecked():
                self.suffix.setReadOnly(False)
            else:
                self.suffix.setText("")
                self.suffix.setReadOnly(True)

        def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',\
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

        def resize_rb_clicked(self):
            if self.resolution_rb.isChecked():
                # print("resize resolution radio")
                self.res_x.setReadOnly(False)
                self.res_y.setReadOnly(False)
                self.resize_scale.setText("")
                self.resize_scale.setReadOnly(True)
            else:
                # print("resize scale radio")
                self.resize_scale.setReadOnly(False)
                self.res_x.setReadOnly(True)
                self.res_y.setReadOnly(True)
                self.res_x.setText("")
                self.res_y.setText("")


        def run_button_clicked(self):

            if self.resolution_rb.isChecked():
                if self.res_x.text() == "" or self.res_y.text() == "":
                    res_x = 0
                    res_y = 0
                else:
                    res_x = int(self.res_x.text())
                    res_y= int(self.res_y.text())
            else:
                res_x = 0
                res_y = 0

            if self.scale_rb.isChecked():
                if self.resize_scale.text() == "":
                    resize_scale = 0
                else:
                    resize_scale = float(self.resize_scale.text())
            else:
                resize_scale = 0


            if self.path_text.text():
                main(self.path_text.text(), self.hflip_cb.checkState(), self.vflip_cb.checkState(),self.angle.value(),self.scale.value(),res_x, res_y, resize_scale,self.prefix.text(), self.suffix.text())
                self.alert.setText("실행 완료")
                print("실행 완료!")
            else:
                self.alert.setText("이미지 디렉토리를 설정하지 않았습니다.")
                print("이미지 디렉토리를 설정하지 않았습니다.")


if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())
