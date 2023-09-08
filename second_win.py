from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
        
    def initUI(self):
        self.txt_name=QLabel(txt_name)
        self.txt_age = QLabel(txt_age)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_timer = QLabel(txt_timer)
        self.btn1 = QPushButton(txt_starttest1)
        self.btn2 = QPushButton(txt_starttest2)
        self.btn3 = QPushButton(txt_starttest3)
        self.btn_next = QPushButton(txt_sendresults)
        self.name = QLineEdit(txt_hintname)
        self.age = QLineEdit(txt_hintage)
        self.test1 = QLineEdit(txt_hinttest1)
        self.test2 = QLineEdit(txt_hinttest2)
        self.test3 = QLineEdit(txt_hinttest3)
        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next,alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.txt_timer,alignment=Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
        
        
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        