import sys
import pandas as pd
from pandas import Series, DataFrame
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Life_list
import Attack_Item_list

Life_list.Life()
Attack_Item_list.Attack()



import sqlite3
con = sqlite3.connect("life.db")
cursor=con.cursor()
cursor.execute("SELECT * FROM life")
r = cursor.fetchall()

print(r[0][2])
print(r[1][2])
print(r[2][2])
print(r[3][2])
print(r[4][2])

conn = sqlite3.connect("life.db")
df = pd.read_sql("SELECT * FROM life",conn,index_col=None)
df_list = df.values.tolist()

#df = {(1, "name",price),(2, "name",price))...}
global Q
Q = str(df_list[0][2])
print(Q)

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

        label1 = QLabel()
        label1.setText("회복약\n")

        label2 = QLabel()
        label2.setText("수줍은 들꽃x5 - "+ Q+"골드")

        label3 = QLabel()
        label3.setText("들꽃x10")

        label4 = QLabel()
        label4.setText('실링 x1200')

        label5 = QLabel()
        label5.setText("0골드")
        
        Profit = Label()
        profit.setText("제작템 값*수수료 계산" - "재료값" +"= 이익")

        
        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)

        self.stack1.setLayout(layout)
        # self.setTabText(0,"Contact Details")

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

#2번탭 
class grid2(QWidget):
    def __init__(self):
        super(grid2, self).__init__()

        """
        treeWidget = QTreeWidget()
        treewidget.setColumnCount(1)
        QList<QTreeWidgetItem()
        #headers = QStringList()    headers << tr("Subject") << tr("Default")   treeWidget.setHeaderLabels(headers)

        for i in range(0, 10):
              items.append(QTreeWidgetItem(QTreeWidget (None), QStringList(QString("item: %1").arg(i))))
        treeWidget.insertTopLevelItems(0, items)
        
        """


        #위젯의 각열에 대한 섹션이 포하묀 헤더는 setHeaderLabels()로 구성, 커스텀헤더는 QTreeWidgetItem 그리고 트리에 아이템구나는 setHeaderItem()

        #참고 https://doc.qt.io/qtforpython/overviews/model-view-programming.html#model-view-programming
        """
        cities = QTreeWidgetItem(treeWidget)
        cities.setText(0, tr("Cities"))
        osloItem = QTreeWidgetItem(cities)
        osloItem.setText(0, tr("Oslo"))
        osloItem.setText(1, tr("Yes"))
        planets = QTreeWidgetItem(treeWidget, cities)
        """
        
        

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
    
    #조합식 적기
    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        # self.setTabText(0,"Contact Details")
        label = QLabel()
        label.setText(Q)
        layout.addWidget(label)
        self.stack1.setLayout(layout)


    def display(self, i):
        self.Stack.setCurrentIndex(i)
    
    #수수료    
    def lifting(value):
      if(value == 1):
        return 0
      if ((value*0.05)%10 != 0):
        value = int(value*0.05) + 1
        return value
      if ((value*0.05)%10 == 0):
        return int(value*0.05)
        
        
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
