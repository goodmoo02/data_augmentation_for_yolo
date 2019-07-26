import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QMessageBox, \
        QLabel, QLineEdit, QTextEdit, QHBoxLayout, QHBoxLayout, QPushButton, QSpinBox)
from PyQt5.QtWidgets import QDoubleSpinBox, QFileDialog, QCheckBox, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
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

            
            # resize scale spinbox
            self.scale = QDoubleSpinBox()
            self.scale.setMinimum(0.3)
            self.scale.setMaximum(1.0)
            self.scale.setSingleStep(0.01)
            self.scale.setValue(1.00)

            # rotate angle spinbox
            self.angle= QSpinBox()
            self.angle.setRange(0,360)
            
            # directory path QLineEdit
            self.path_text= QLineEdit()
            
            self.initUI()

        def initUI(self):

            grid = QGridLayout()
            self.setLayout(grid)
            

            # Layout

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


            grid.addWidget(QLabel('Directory select'), 0, 0)
            grid.addWidget(QLabel('Flip mode'), 1, 0)
            grid.addWidget(QLabel('Rescale scale'), 2, 0)
            grid.addWidget(QLabel('Rotate angle'), 3, 0)
            grid.addLayout(hbox, 4,0,2,3)

            grid.addWidget(self.path_text, 0, 1)
            grid.addLayout(flip_box,1,1)
            grid.addWidget(self.scale, 2, 1)
            grid.addWidget(self.angle, 3, 1)

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
        

        def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',\
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

        def run_button_clicked(self):
            print("run button clicked")

            if self.path_text.text():
                main(self.path_text.text(), self.hflip_cb.checkState(), self.vflip_cb.checkState(),self.angle.value(),self.scale.value())

                print("실행 완료!")
            else:
                print("이미지 디렉토리를 설정하지 않았습니다.")




if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())
