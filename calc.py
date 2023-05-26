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
        self.setGeometry(150, 400, 280, 345)
        self.setWindowTitle("Калькулятор")
        self.setWindowIcon(QIcon('static\\img\\калк.png'))
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow {background-color: black;}")

        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: white")
        self.label.setText('0')
        self.label.setFont(QFont('', 10))
        self.label.resize(265, 40)
        self.label.move(7, 15)

        self.num_1 = QPushButton('1', self)
        self.num_1.setFont(QFont('', 10))
        self.num_1.resize(50, 50)
        self.num_1.move(5, 70)

        self.num_2 = QPushButton('2', self)
        self.num_2.setFont(QFont('', 10))
        self.num_2.resize(50, 50)
        self.num_2.move(60, 70)

        self.num_3 = QPushButton('3', self)
        self.num_3.setFont(QFont('', 10))
        self.num_3.resize(50, 50)
        self.num_3.move(115, 70)

        self.div = QPushButton('/', self)
        self.div.setFont(QFont('', 10))
        self.div.resize(50, 50)
        self.div.move(170, 70)

        self.num_4 = QPushButton('4', self)
        self.num_4.setFont(QFont('', 10))
        self.num_4.resize(50, 50)
        self.num_4.move(5, 125)

        self.num_5 = QPushButton('5', self)
        self.num_5.setFont(QFont('', 10))
        self.num_5.resize(50, 50)
        self.num_5.move(60, 125)

        self.num_6 = QPushButton('6', self)
        self.num_6.setFont(QFont('', 10))
        self.num_6.resize(50, 50)
        self.num_6.move(115, 125)

        self.mul = QPushButton('*', self)
        self.mul.setFont(QFont('', 12))
        self.mul.resize(50, 50)
        self.mul.move(170, 125)

        self.num_7 = QPushButton('7', self)
        self.num_7.setFont(QFont('', 10))
        self.num_7.resize(50, 50)
        self.num_7.move(5, 180)

        self.num_8 = QPushButton('8', self)
        self.num_8.setFont(QFont('', 10))
        self.num_8.resize(50, 50)
        self.num_8.move(60, 180)

        self.num_9 = QPushButton('9', self)
        self.num_9.setFont(QFont('', 10))
        self.num_9.resize(50, 50)
        self.num_9.move(115, 180)

        self.plus = QPushButton('+', self)
        self.plus.setFont(QFont('', 10))
        self.plus.resize(50, 50)
        self.plus.move(170, 180)

        self.num_0 = QPushButton('0', self)
        self.num_0.setFont(QFont('', 10))
        self.num_0.resize(105, 50)
        self.num_0.move(5, 235)

        self.minus = QPushButton('-', self)
        self.minus.setFont(QFont('', 11))
        self.minus.resize(50, 50)
        self.minus.move(115, 235)

        self.step = QPushButton('^', self)
        self.step.setFont(QFont('', 10))
        self.step.resize(50, 50)
        self.step.move(170, 235)

        self.ostatok = QPushButton('%', self)
        self.ostatok.setFont(QFont('', 10))
        self.ostatok.resize(50, 50)
        self.ostatok.move(225, 70)

        self.integer = QPushButton('//', self)
        self.integer.setFont(QFont('', 10))
        self.integer.resize(50, 50)
        self.integer.move(225, 125)

        self.qv = QPushButton('^2', self)
        self.qv.setFont(QFont('', 10))
        self.qv.resize(50, 50)
        self.qv.move(225, 180)



        self.sqrt = QPushButton('√', self)
        self.sqrt.setFont(QFont('', 10))
        self.sqrt.resize(50, 50)
        self.sqrt.move(225, 235)

        self.ravn = QPushButton('=', self)
        self.ravn.setFont(QFont('', 10))
        self.ravn.resize(215, 50)
        self.ravn.move(5, 290)

        self.c = QPushButton('C', self)
        self.c.setFont(QFont('', 10))
        self.c.resize(50, 50)
        self.c.move(225, 290)


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
        self.qv.clicked.connect(self.qv_1)

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

    def qv_1(self):
        self.operation = '^2'
        self.operand_1 = float(self.label.text())
        self.rezult = self.operand_1 ** 2
        self.label.setText(str(self.rezult))

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
