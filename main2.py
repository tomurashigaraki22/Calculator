import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget, QApplication
from PySide6 import QtGui
import re

from ui_form import Ui_Widget

class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        self.calcUi = Ui_Widget()
        self.calcUi.setupUi(self)
        self.calcUi.pushButton.clicked.connect(self.button_nine)
        self.calcUi.pushButton_2.clicked.connect(self.button_eight)
        self.calcUi.pushButton_3.clicked.connect(self.button_seven)
        self.calcUi.pushButton_4.clicked.connect(self.button_six)
        self.calcUi.pushButton_5.clicked.connect(self.button_five)
        self.calcUi.pushButton_6.clicked.connect(self.button_four)
        self.calcUi.pushButton_7.clicked.connect(self.button_three)
        self.calcUi.pushButton_8.clicked.connect(self.button_two)
        self.calcUi.pushButton_9.clicked.connect(self.button_one)
        self.calcUi.pushButton_10.clicked.connect(self.button_zero)
        self.calcUi.pushButton_13.clicked.connect(self.calculate)
        self.calcUi.pushButton_11.clicked.connect(self.plusAdd)
        self.calcUi.pushButton_12.clicked.connect(self.plusMinus)
        self.calcUi.pushButton_14.clicked.connect(self.clearScreen)

    def button_nine(self):
        self.calcUi.plainTextEdit.insertPlainText('9')

    def button_eight(self):
        self.calcUi.plainTextEdit.insertPlainText('8')

    def button_seven(self):
        self.calcUi.plainTextEdit.insertPlainText('7')

    def button_six(self):
        self.calcUi.plainTextEdit.insertPlainText('6')

    def button_five(self):
        self.calcUi.plainTextEdit.insertPlainText('5')

    def button_four(self):
        self.calcUi.plainTextEdit.insertPlainText('4')

    def button_three(self):
        self.calcUi.plainTextEdit.insertPlainText('3')

    def button_two(self):
        self.calcUi.plainTextEdit.insertPlainText('2')

    def button_one(self):
        self.calcUi.plainTextEdit.insertPlainText('1')

    def button_zero(self):
        self.calcUi.plainTextEdit.insertPlainText('0')
    
    def plusAdd(self):
        self.calcUi.plainTextEdit.insertPlainText('+')

    def plusMinus(self):
        self.calcUi.plainTextEdit.insertPlainText('-')

    def clearScreen(self):
        self.calcUi.plainTextEdit.clear()


    def calculate(self):
        expression = self.calcUi.plainTextEdit.toPlainText()
        matches = re.match(r'(\d+)([+\-])(\d+)', expression)
        if matches:
            a = int(matches.group(1))
            sign = matches.group(2)
            b = int(matches.group(3))
            if sign == '+':
                t = a + b
            elif sign == '-':
                t = a - b
            self.calcUi.plainTextEdit.clear()
            self.calcUi.plainTextEdit.insertPlainText(str(t))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec())
