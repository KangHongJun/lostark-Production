import sys
import pandas as pd
from pandas import Series, DataFrame
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Life_list
import Attack_Item_list

from UI import Attack_ItemUI

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

#포션
class grid(QWidget):
    def __init__(self):
        super(grid, self).__init__()
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '1')
        self.leftlist.insertItem(1, '2')
        self.leftlist.insertItem(2, '3')
        self.leftlist.insertItem(3, '4')
        
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        
        self.Healing()
        self.Rare_Healing()
        self.Spirit_Healing()
        self.S_Spirit_Healing()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()
    
    #회복약
    def Healing(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("회복약\n")

        label2 = QLabel()
        label2.setText("수줍은 들꽃x5 - " + "골드")

        label3 = QLabel()
        label3.setText("들꽃x10")

        label4 = QLabel()
        label4.setText('실링 x1200')
        label4.setText(str(df_list[0][2]))

        label5 = QLabel()
        label5.setText("0골드")
        
        profit = QLabel()
        profit.setText(Q)

        str(df_list[0][2])

        
        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addWidget(profit)

        self.stack1.setLayout(layout)
        
    #고급 회복약
    def Rare_Healing (self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("고급 회복약\n")

        label2 = QLabel()
        label2.setText("수줍은 들꽃x9 - " + "골드")

        label3 = QLabel()
        label3.setText("들꽃x18")

        label4 = QLabel()
        label4.setText("15골드")
        
        profit = QLabel()
        profit.setText("제작템 값*수수료 계산" + "재료값" +"= 이익")

        
        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(profit)

        self.stack1.setLayout(layout)



    def Spirit_Healing(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("정령의 회복약\n")

        label2 = QLabel()
        label2.setText("화사한 들꽃x6 - " + "골드")

        label3 = QLabel()
        label3.setText("수줍은 들꽃x24")

        label4 = QLabel()
        label4.setText('들꽃x48')

        label5 = QLabel()
        label5.setText("30골드")
        


        
        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)


        self.stack1.setLayout(layout)

        
    def S_Spirit_Healing(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("고급 정령의 회복약\n")

        label2 = QLabel()
        label2.setText("정령의 회복약x3 - " + "골드")

        label3 = QLabel()
        label3.setText("화사한 들꽃x8")

        label4 = QLabel()
        label4.setText("30골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

#버프 아이템
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
        

        self.Protection()
        self.Flag()
        self.Quick()

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
    
    #보호 물약
    def Protection(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("보호 물약\n")

        label2 = QLabel()
        label2.setText("화려한 버섯x4 - " + "골드")

        label3 = QLabel()
        label3.setText("싱싱한 버섯x16")
        
        label4 = QLabel()
        label4.setText("투박한 버섯x32")
        
        label5 = QLabel()
        label5.setText("희귀한 유물x5")

        label6 = QLabel()
        label6.setText("15골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)

    #진군의 깃발
    def Flag(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("진군의 깃발\n")

        label2 = QLabel()
        label2.setText("화려한 버섯x4 - " + "골드")

        label3 = QLabel()
        label3.setText("투박한 버섯x38")
        
        label4 = QLabel()
        label4.setText("자연산 진주x8")

        label5 = QLabel()
        label5.setText("15골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)
        
    #신속 로브
    def Quick(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("신속 로브\n")

        label2 = QLabel()
        label2.setText("질간 가죽x22 - " + "골드")

        label3 = QLabel()
        label3.setText("수줍은 들꽃x17")
        
        label4 = QLabel()
        label4.setText("들꽃x27")
        

        label5 = QLabel()
        label5.setText("15골드")


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)
        
    #각성 물약
    def Arousal(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("각성 물약\n")

        label2 = QLabel()
        label2.setText("화려한 버섯x5 - " + "골드")

        label3 = QLabel()
        label3.setText("싱싱한 버섯x20")
        
        label4 = QLabel()
        label4.setText("투박한 버섯x40")
        
        label5 = QLabel()
        label5.setText("희귀한 유물x4")
        
        label6 = QLabel()
        label6.setText("튼튼한 목재x2")

        label7 = QLabel()
        label7.setText("15골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)
        
    #아드로핀 물약
    def Atropine(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("아드로핀 물약\n")

        label2 = QLabel()
        label2.setText("화사한 들꽃x6 - " + "골드")

        label3 = QLabel()
        label3.setText("수줍은 들꽃x24")
        
        label4 = QLabel()
        label4.setText("들꽃x48")
        
        label5 = QLabel()
        label5.setText("희귀한 유물x2")
        
        label6 = QLabel()
        label6.setText("단단한 철광석x2")

        label7 = QLabel()
        label7.setText("30골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)
        
    #빛나는 보호 물약
    def S_Protection(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("빛나는 보호 물약\n")

        label2 = QLabel()
        label2.setText("보호 물약x3 - " + "골드")

        label3 = QLabel()
        label3.setText("화려한 버섯x3")

        label4 = QLabel()
        label4.setText("15골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)
        
     #빛나는 진군의 깃발
    def S_Flag(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("빛나는 진군의 깃발\n")

        label2 = QLabel()
        label2.setText("진군의 깃발x3 - " + "골드")

        label3 = QLabel()
        label3.setText("화려한 버섯x3")
      
        label4 = QLabel()
        label4.setText("15골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)
        
     #빛나는 신속 로브
    def S_Quick(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("빛나는 신속 물약\n")

        label2 = QLabel()
        label2.setText("신속 로브x3 - " + "골드")

        label3 = QLabel()
        label3.setText("화려한 버섯x9")

        label4 = QLabel()
        label4.setText("15골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)
        
    
class grid(QWidget):
    def __init__(self):
        super(grid, self).__init__()
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '1')
        self.leftlist.insertItem(1, '2')
        self.leftlist.insertItem(2, '3')
        self.leftlist.insertItem(3, '4')
        
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        
        self.Healing()
        self.Rare_Healing()
        self.Spirit_Healing()
        self.S_Spirit_Healing()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()
    
    #회복약
    def Healing(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("회복약\n")

        label2 = QLabel()
        label2.setText("수줍은 들꽃x5 - " + "골드")

        label3 = QLabel()
        label3.setText("들꽃x10")

        label4 = QLabel()
        label4.setText('실링 x1200')
        label4.setText(str(df_list[0][2]))

        label5 = QLabel()
        label5.setText("0골드")
        
        profit = QLabel()
        profit.setText(Q)

        str(df_list[0][2])

        
        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addWidget(profit)

        self.stack1.setLayout(layout)
        
    #고급 회복약
    def Rare_Healing (self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("고급 회복약\n")

        label2 = QLabel()
        label2.setText("수줍은 들꽃x9 - " + "골드")

        label3 = QLabel()
        label3.setText("들꽃x18")

        label4 = QLabel()
        label4.setText("15골드")
        
        profit = QLabel()
        profit.setText("제작템 값*수수료 계산" + "재료값" +"= 이익")

        
        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(profit)

        self.stack1.setLayout(layout)



    def Spirit_Healing(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("정령의 회복약\n")

        label2 = QLabel()
        label2.setText("화사한 들꽃x6 - " + "골드")

        label3 = QLabel()
        label3.setText("수줍은 들꽃x24")

        label4 = QLabel()
        label4.setText('들꽃x48')

        label5 = QLabel()
        label5.setText("30골드")
        


        
        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)


        self.stack1.setLayout(layout)

        
    def S_Spirit_Healing(self):
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("고급 정령의 회복약\n")

        label2 = QLabel()
        label2.setText("정령의 회복약x3 - " + "골드")

        label3 = QLabel()
        label3.setText("화사한 들꽃x8")

        label4 = QLabel()
        label4.setText("30골드")
        


        #label.move(20, 20) 형식으로 제작템 가격 - 수수료 계산
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)


        self.stack1.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

#Attack_Item
class grid2(QWidget):
    def __init__(self):
        super(grid2, self).__init__()

        self.Protection()
        self.Flag()
        self.Quick()

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
        
        
    def Flash(self):
        Attack_ItemUI.Flash()
        

    
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
        tabs.addTab(self.tab1(), '포션')
        tabs.addTab(self.tab2(), '전투 아이템')
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
    
    def tab2(self):
        wg = grid2()
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
