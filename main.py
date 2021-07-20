import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Fishing_list

Fishing_list.Fishing_price()


import sqlite3
con = sqlite3.connect("life.db")
cursor=con.cursor()
cursor.execute("SELECT * FROM life")

r = cursor.fetchall()
rr = r[0][2]

print(r[0][2])
print(r[1][2])
print(r[2][2])
print(r[3][2])
print(r[4][2])


class grid(QWidget):
    def __init__(self):
        super(grid, self).__init__()
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '1')
        self.leftlist.insertItem(1, '2')
        self.leftlist.insertItem(2, '3')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()


    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        # self.setTabText(0,"Contact Details")
        self.stack1.setLayout(layout)


    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("Date of Birth", QLineEdit())

        self.stack2.setLayout(layout)


    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.stack3.setLayout(layout)


    def display(self, i):
        self.Stack.setCurrentIndex(i)


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.make_tap()

    def initUI(self):
        #UI 기본
        self.setWindowIcon(QIcon('lostark.jpg'))
        self.setWindowTitle('제작효율')
        self.setGeometry(100, 100, 1000, 500)

        # 하단에 날짜 출력
        self.date = QDate.currentDate()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

    def make_tap(self):
        # QWidget 적용
        tabs = QTabWidget()
        tabs.addTab(self.tab1(), '배틀 아이템')
        tabs.addTab(self.tab1(), '로브')
        self.setCentralWidget(tabs)

    def tab1(self):
        wg = grid()
        self.setCentralWidget(wg)

        hbox = QHBoxLayout()
        hbox.addWidget(wg)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()

    sys.exit(app.exec_())