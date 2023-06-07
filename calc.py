import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []

    def initUI(self):
        self.setGeometry(150, 400, 350, 420)
        self.setWindowTitle("Калькулятор")
        self.setWindowIcon(QIcon('static/img/icon.png'))
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow {background-color: black;}")

        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: black; color: white")
        self.label.setText('0')
        self.label.setFont(QFont('', 14))
        self.label.resize(270, 45)
        self.label.move(7, 15)

        self.num_1 = QPushButton('1', self)
        self.num_1.setStyleSheet("background-color: #e7e8e5")
        self.num_1.setFont(QFont('', 14))
        self.num_1.resize(70, 70)
        self.num_1.move(0, 70)

        self.num_2 = QPushButton('2', self)
        self.num_2.setStyleSheet("background-color: #e7e8e5")
        self.num_2.setFont(QFont('', 14))
        self.num_2.resize(70, 70)
        self.num_2.move(70, 70)

        self.num_3 = QPushButton('3', self)
        self.num_3.setStyleSheet("background-color: #e7e8e5")
        self.num_3.setFont(QFont('', 14))
        self.num_3.resize(70, 70)
        self.num_3.move(140, 70)

        self.div = QPushButton('/', self)
        self.div.setStyleSheet("background-color: #ff9f4e")
        self.div.setFont(QFont('', 14))
        self.div.resize(70, 70)
        self.div.move(210, 70)

        self.num_4 = QPushButton('4', self)
        self.num_4.setStyleSheet("background-color: #e7e8e5")
        self.num_4.setFont(QFont('', 14))
        self.num_4.resize(70, 70)
        self.num_4.move(0, 140)

        self.num_5 = QPushButton('5', self)
        self.num_5.setStyleSheet("background-color: #e7e8e5")
        self.num_5.setFont(QFont('', 14))
        self.num_5.resize(70, 70)
        self.num_5.move(70, 140)

        self.num_6 = QPushButton('6', self)
        self.num_6.setStyleSheet("background-color: #e7e8e5")
        self.num_6.setFont(QFont('', 14))
        self.num_6.resize(70, 70)
        self.num_6.move(140, 140)

        self.mul = QPushButton('*', self)
        self.mul.setStyleSheet("background-color: #ff9f4e")
        self.mul.setFont(QFont('', 14))
        self.mul.resize(70, 70)
        self.mul.move(210, 140)

        self.num_7 = QPushButton('7', self)
        self.num_7.setStyleSheet("background-color: #e7e8e5")
        self.num_7.setFont(QFont('', 14))
        self.num_7.resize(70, 70)
        self.num_7.move(0, 210)

        self.num_8 = QPushButton('8', self)
        self.num_8.setStyleSheet("background-color: #e7e8e5")
        self.num_8.setFont(QFont('', 14))
        self.num_8.resize(70, 70)
        self.num_8.move(70, 210)

        self.num_9 = QPushButton('9', self)
        self.num_9.setStyleSheet("background-color: #e7e8e5")
        self.num_9.setFont(QFont('', 14))
        self.num_9.resize(70, 70)
        self.num_9.move(140, 210)

        self.plus = QPushButton('+', self)
        self.plus.setStyleSheet("background-color: #ff9f4e")
        self.plus.setFont(QFont('', 14))
        self.plus.resize(70, 70)
        self.plus.move(210, 210)

        self.num_0 = QPushButton('0', self)
        self.num_0.setStyleSheet("background-color: #e7e8e5")
        self.num_0.setFont(QFont('', 14))
        self.num_0.resize(210, 70)
        self.num_0.move(0, 280)

        self.minus = QPushButton('-', self)
        self.minus.setStyleSheet("background-color: #ff9f4e")
        self.minus.setFont(QFont('', 14))
        self.minus.resize(70, 70)
        self.minus.move(210, 280)

        self.step = QPushButton('^', self)
        self.step.setStyleSheet("background-color: #ff9f4e")
        self.step.setFont(QFont('', 14))
        self.step.resize(70, 70)
        self.step.move(280, 210)

        self.ostatok = QPushButton('%', self)
        self.ostatok.setStyleSheet("background-color: #ff9f4e")
        self.ostatok.setFont(QFont('', 14))
        self.ostatok.resize(70, 70)
        self.ostatok.move(280, 70)

        self.integer = QPushButton('//', self)
        self.integer.setStyleSheet("background-color: #ff9f4e")
        self.integer.setFont(QFont('', 14))
        self.integer.resize(70, 70)
        self.integer.move(280, 140)

        self.sqrt = QPushButton('√', self)
        self.sqrt.setStyleSheet("background-color: #ff9f4e")
        self.sqrt.setFont(QFont('', 14))
        self.sqrt.resize(70, 70)
        self.sqrt.move(280, 280)

        self.ravn = QPushButton('=', self)
        self.ravn.setStyleSheet("background-color: #f3882d")
        self.ravn.setFont(QFont('', 14))
        self.ravn.resize(280, 70)
        self.ravn.move(0, 350)

        self.c = QPushButton('C', self)
        self.c.setStyleSheet("background-color: #f3882d")
        self.c.setFont(QFont('', 14))
        self.c.resize(70, 70)
        self.c.move(280, 350)


        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.mul.clicked.connect(self.mul_1)
        self.div.clicked.connect(self.div_1)
        self.step.clicked.connect(self.step_1)
        self.sqrt.clicked.connect(self.sqrt_1)
        self.ostatok.clicked.connect(self.ostatok_1)
        self.integer.clicked.connect(self.integer_1)

        self.ravn.clicked.connect(self.ravno)
        self.c.clicked.connect(self.clean)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def step_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')


    def integer_1(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ostatok_1(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')


    def ravno(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        elif self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        elif self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 / self.operand_2
        elif self.operation == '^':
            self.rezult = self.operand_1 ** self.operand_2
        elif self.operation == '√':
            self.rezult = self.operand_1 ** (1 / self.operand_2)
        elif self.operation == '%':
            self.rezult = self.operand_1 % self.operand_2
        elif self.operation == '//':
            self.rezult = self.operand_1 // self.operand_2

        self.label.setText(str(self.rezult))

    def clean(self):
        self.label.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
