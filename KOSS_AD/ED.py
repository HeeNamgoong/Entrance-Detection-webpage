from gettext import bind_textdomain_codeset
import sys
from turtle import color
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QInputDialog
from PyQt5.QtGui import QPixmap, QFont, QColor, QPainter
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import os


class Button(QWidget):
    def __init__(self):
        super().__init__()
        self.UIinit()
        
        vbox = QVBoxLayout()
        vbox.addLayout(self.vbox1)
        vbox.addLayout(self.vbox2)
        vbox.addLayout(self.vbox3)
        


        
    def UIinit(self):
    
        
        self.label1 = QLabel("OFF", self)
        self.label1.move(310, 100)
        font1 = self.label1.font()
        font1.setPointSize(50)
        font1.setFamily('Bodoni MT Black')
        font1.setBold(True)
        self.label1.setFont(font1)
        
   
        
        
        self.label2 = QLabel("택배 아저씨 버튼 눌러 주세요~", self)
        self.label2.move(3, 5)
        font2 = self.label2.font()
        font2.setPointSize(15)
        self.label2.setFont(font2)
        
        self.label1.adjustSize()
        self.label2.adjustSize()
       
        
        self.btn1 = QPushButton('택배/배달', self)
        self.btn2 = QPushButton('도둑', self)
        self.btn3 = QPushButton('풀기', self)
        self.btn1.move(50, 600)
        self.btn2.move(300, 600)
        self.btn3.move(550, 600)
        self.btn1.setFixedSize(210, 100)
        self.btn2.setFixedSize(210, 100)
        self.btn3.setFixedSize(210, 100)
        
        self.btn1.setFont(QtGui.QFont("휴먼모음T", 30))
        self.btn2.setFont(QtGui.QFont("휴먼모음T", 30))
        self.btn3.setFont(QtGui.QFont("휴먼모음T", 30))
        
        
        

        
        self.vbox1 = QHBoxLayout()
        self.vbox2 = QHBoxLayout()
        self.vbox3 = QHBoxLayout()
        
        self.vbox1.addWidget(self.label1)
        self.vbox2.addWidget(self.label2)
        self.vbox3.addWidget(self.btn1)
        self.vbox3.addWidget(self.btn2)
        self.vbox3.addWidget(self.btn3)
        
        
        
        
        
        # password
        

        
        self.btn3.clicked.connect(self.button_Second)




        self.setGeometry(500, 300, 800, 700)
        self.setWindowTitle('Main Door')
        self.show()
        
         
    
    
    
    
    def button_Second(self):
        os.system("python passsword.py")
    
    
    
    
    
    
        
        
        

        
    # def Clear(self):
        
    #     self.label1.clear()
    #     self.label2.clear()
        
        
    #     self.btn = QPushButton('Password', self)
    #     self.btn.move(30, 30)
    #     self.btn.clicked.connect(self.showDialog)

    #     self.le = QLineEdit(self)
    #     self.le.move(120, 35)
        

        
        

    #     self.setWindowTitle('Input password')
    #     self.setGeometry(500, 300, 800, 700)
    #     self.show()
        
        
    # def showDialog(self):
    #     text, ok = QInputDialog.getText(self, 'Input password', 'Enter password:')
    #     message = QMessageBox.information(self, "correct!")
    

    #     if ok:
    #         self.le.setText(str(text))
            
        
            
            
    #     if text == "koss":
    #         message
    #         sys.exit(app.exec_())
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
                       
app = QApplication(sys.argv)
ex = Button()
app.exec_()


