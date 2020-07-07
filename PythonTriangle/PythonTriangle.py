import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QLCDNumber, QDoubleSpinBox
from PyQt5.QtCore import QCoreApplication, pyqtSignal
from PyQt5.QtGui import QIcon, QColor
import math


app = QtWidgets.QApplication([])

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('my_triangle.ui', self)
        
        self.setStyleSheet("QMainWindow {background-color:rgba(0, 75, 100, 255)}")
        self.setWindowTitle('Triangle')
        self.setWindowIcon(QIcon('protractor.png'))  # вставляем иконку
        
        self.label.setFont(QtGui.QFont('SansSerif', 14))   # изменяем шрифт
        self.label.setGeometry(QtCore.QRect(10, 5, 200, 30))   # изменяет размер label
        self.label.setText("Введите стороны треугольника")   # изменяем текст в label
        self.label.setStyleSheet("color: rgba(0, 200, 255, 255);")   # цвет текса в label
        self.label.adjustSize()
        
        self.pushButton_1.setStyleSheet("background-color: rgba(255, 0, 0, 255);")   # цвет pushButton
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 120, 255, 255);")
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 155, 0, 255);")

        self.lineEdit_1.setStyleSheet("background-color: rgba(100, 215, 225, 255); border: rgb(255, 255, 255);")   # цвет lineEdit
        self.lineEdit_3.setStyleSheet("background-color: rgba(100, 215, 225, 255); border: rgb(255, 255, 255);")
        self.lineEdit_5.setStyleSheet("background-color: rgba(100, 215, 225, 255); border: rgb(255, 255, 255);")
        self.lineEdit_6.setStyleSheet("background-color: rgba(100, 215, 225, 255); border: rgb(255, 255, 255);")
        
        self.spinBox_1.setStyleSheet("background-color: rgba(100, 155, 225, 255); border: rgb(255, 255, 225);")   # цвет spinbox 
        self.spinBox_2.setStyleSheet("background-color: rgba(100, 155, 225, 255); border: rgb(255, 255, 255);")

        self.lcdNumber_1.setStyleSheet("background-color: rgba(100, 155, 225, 255);")
        self.lcdNumber_2.setStyleSheet("background-color: rgba(100, 155, 225, 255);")


        self.pushButton_1.clicked.connect(QCoreApplication.instance().quit)   # выключение программы        
        self.pushButton_2.clicked.connect(self.corners)   # подсчет

                
    def corners(self):
        self.value_a = self.spinBox_1.value()
        self.value_b = self.spinBox_2.value()
        a = self.value_a
        b = self.value_b
        
        A_r = math.sin(a / b)
        A = A_r * 180 / math.pi
        B = 180 - 90 - A
            
        self.lcdNumber_1.display(A)   
        self.lcdNumber_2.display(B)
         
        
        self.signClear = QtWidgets.QPushButton('ОЧИСТИТЬ')   # очистка введенных значений
        

myWindow = MainWindow()
myWindow.show()
sys.exit(app.exec())
