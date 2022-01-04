import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from UI import EtcUI,Attack_ItemUI
from LIST import Attack_Item_list,Combat_Assistance_list,Etc_list,Life_list

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--de')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"]="none"


driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)



driver.get(
    'https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fMarket')
driver.maximize_window()
login_x_path = '/html/body/div[1]/div[2]/div/fieldset[1]/div[4]/button'
            #/html/body/div[1]/div[2]/div/fieldset[1]/div[4]/button/span
ID = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[1]/input')
ID.clear()
ID.send_keys('starmine325@gmail.com')
PW = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[2]/input')
PW.clear()
PW.send_keys('starmine97@')

# login
driver.find_element_by_xpath(login_x_path).click()
#wait(driver, 10)
driver.implicitly_wait(10)


# Life-Fishing

driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[3]/div[1]/ul/li[8]/a').click()

Life_list.Life(driver)
Etc_list.Etc(driver)
Attack_Item_list.Attack(driver)
Combat_Assistance_list.Assistance(driver)



#포션
class Potion(QWidget):
    def __init__(self):
        super(Potion, self).__init__()
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


        label5 = QLabel()
        label5.setText("0골드")
        
        profit = QLabel()




        
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
class buff_Item(QWidget):
    def __init__(self):
        super(Special_Item, self).__init__()

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

#Speical_Item
class Special_Item(QWidget):
    def __init__(self):
        super(Special_Item, self).__init__()

        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '하급-수렵')
        self.leftlist.insertItem(1, '중급-수렵')
        self.leftlist.insertItem(2, '상급-수렵')
        self.leftlist.insertItem(3, '하급-낚시')
        self.leftlist.insertItem(4, '중급-낚시')
        self.leftlist.insertItem(5, '상급-낚시')
        self.leftlist.insertItem(6, '하급-고고학')
        self.leftlist.insertItem(7, '중급-고고학')
        self.leftlist.insertItem(8, '상급-고고학')


        self.h_low = QWidget()
        self.h_mid = QWidget()
        self.h_high = QWidget()
        self.f_low = QWidget()
        self.f_mid = QWidget()
        self.f_high = QWidget()
        self.a_low = QWidget()
        self.a_mid = QWidget()
        self.a_high = QWidget()

        EtcUI.H_Low(self)
        EtcUI.H_Mid(self)
        EtcUI.H_High(self)
        EtcUI.F_Low(self)
        EtcUI.F_Mid(self)
        EtcUI.F_High(self)
        EtcUI.A_Low(self)
        EtcUI.A_Mid(self)
        EtcUI.A_High(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.h_low)
        self.Stack.addWidget(self.h_mid)
        self.Stack.addWidget(self.h_high)
        self.Stack.addWidget(self.f_low)
        self.Stack.addWidget(self.f_mid)
        self.Stack.addWidget(self.f_high)
        self.Stack.addWidget(self.a_low)
        self.Stack.addWidget(self.a_mid)
        self.Stack.addWidget(self.a_high)


        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()
    
    def display(self, i):
        self.Stack.setCurrentIndex(i)


class Attack_Item(QWidget):
    def __init__(self):
        super(Attack_Item, self).__init__()

        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '섬광 수류탄')
        self.leftlist.insertItem(1, '화염 수류탄')
        self.leftlist.insertItem(2, '냉기 수류탄')
        self.leftlist.insertItem(3, '전기 수류탄')
        self.leftlist.insertItem(4, '암흑 수류탄')
        self.leftlist.insertItem(5, '부식 폭탄')
        self.leftlist.insertItem(6, '천둥 물약')
        self.leftlist.insertItem(7, '회오리 수류탄')
        self.leftlist.insertItem(8, '점토 수류탄')
        self.leftlist.insertItem(9, '수면 폭탄')
        self.leftlist.insertItem(10, '성스러운 폭탄')
        self.leftlist.insertItem(11, '파괴 폭탄')
        self.leftlist.insertItem(12, '빛나는 섬광 수류탄')
        self.leftlist.insertItem(13, '빛나는 화염 수류탄')
        self.leftlist.insertItem(14, '빛나는 냉기 수류탄')
        self.leftlist.insertItem(15, '빛나는 전기 수류탄')
        self.leftlist.insertItem(16, '빛나는 점토 수류탄')
        self.leftlist.insertItem(17, '빛나는 회오리 수류탄')
        self.leftlist.insertItem(18, '빛나는 암흑 수류탄')
        self.leftlist.insertItem(19, '빛나는 수면 폭탄')
        self.leftlist.insertItem(20, '빛나는 파괴 폭탄')
        self.leftlist.insertItem(21, '빛나는 부식 폭탄')
        self.leftlist.insertItem(22, '빛나는 성스러운 폭탄')

        self.flash = QWidget()
        self.flame = QWidget()
        self.coldair = QWidget()
        self.electric = QWidget()
        self.dark = QWidget()
        self.corrosion = QWidget()
        self.thunder = QWidget()
        self.Tornado = QWidget()
        self.clay = QWidget()
        self.sleeping = QWidget()
        self.holy = QWidget()
        self.destruction = QWidget()
        self.s_flash = QWidget()
        self.s_flame = QWidget()
        self.s_coldair = QWidget()
        self.s_electric = QWidget()
        self.s_clay = QWidget()
        self.s_tornado = QWidget()
        self.s_dark = QWidget()
        self.s_sleeping = QWidget()
        self.s_destruction = QWidget()
        self.s_corrosion = QWidget()
        self.s_holy = QWidget()



        Attack_ItemUI.Flash(self)
        Attack_ItemUI.Flame(self)
        Attack_ItemUI.Cold_Air(self)
        Attack_ItemUI.Electric(self)
        Attack_ItemUI.Dark(self)
        Attack_ItemUI.Corrosion(self)
        Attack_ItemUI.Thunder(self)
        Attack_ItemUI.Tornado(self)
        Attack_ItemUI.Clay(self)
        Attack_ItemUI.Sleeping(self)
        Attack_ItemUI.Holy(self)
        Attack_ItemUI.Destruction(self)
        Attack_ItemUI.S_Flash(self)
        Attack_ItemUI.S_Flame(self)
        Attack_ItemUI.S_Cold_Air(self)
        Attack_ItemUI.S_Electric(self)
        Attack_ItemUI.S_Clay(self)
        Attack_ItemUI.S_Tornado(self)
        Attack_ItemUI.S_Dark(self)
        Attack_ItemUI.S_Sleeping(self)
        Attack_ItemUI.S_Destruction(self)
        Attack_ItemUI.S_Corrosion(self)
        Attack_ItemUI.S_Holy(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.flash)
        self.Stack.addWidget(self.flame)
        self.Stack.addWidget(self.coldair)
        self.Stack.addWidget(self.electric)
        self.Stack.addWidget(self.dark)
        self.Stack.addWidget(self.corrosion)
        self.Stack.addWidget(self.thunder)
        self.Stack.addWidget(self.Tornado)
        self.Stack.addWidget(self.clay)
        self.Stack.addWidget(self.sleeping)
        self.Stack.addWidget(self.holy)
        self.Stack.addWidget(self.destruction)
        self.Stack.addWidget(self.s_flash)
        self.Stack.addWidget(self.s_flame)
        self.Stack.addWidget(self.s_coldair)
        self.Stack.addWidget(self.s_electric)
        self.Stack.addWidget(self.s_clay)
        self.Stack.addWidget(self.s_tornado)
        self.Stack.addWidget(self.s_dark)
        self.Stack.addWidget(self.s_sleeping)
        self.Stack.addWidget(self.s_destruction)
        self.Stack.addWidget(self.s_corrosion)
        self.Stack.addWidget(self.s_holy)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()

    def display(self, i):
        self.Stack.setCurrentIndex(i)


class Combat_Assistance(QWidget):
    def __init__(self):
        super(Combat_Assistance, self).__init__()

        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '섬광 수류탄')
        self.leftlist.insertItem(1, '화염 수류탄')
        self.leftlist.insertItem(2, '냉기 수류탄')
        self.leftlist.insertItem(3, '전기 수류탄')
        self.leftlist.insertItem(4, '암흑 수류탄')
        self.leftlist.insertItem(5, '부식 폭탄')
        self.leftlist.insertItem(6, '천둥 물약')
        self.leftlist.insertItem(7, '회오리 수류탄')
        self.leftlist.insertItem(8, '점토 수류탄')
        self.leftlist.insertItem(9, '수면 폭탄')
        self.leftlist.insertItem(10, '성스러운 폭탄')
        self.leftlist.insertItem(11, '파괴 폭탄')
        self.leftlist.insertItem(12, '빛나는 섬광 수류탄')
        self.leftlist.insertItem(13, '빛나는 화염 수류탄')
        self.leftlist.insertItem(14, '빛나는 냉기 수류탄')
        self.leftlist.insertItem(15, '빛나는 전기 수류탄')
        self.leftlist.insertItem(16, '빛나는 점토 수류탄')
        self.leftlist.insertItem(17, '빛나는 회오리 수류탄')
        self.leftlist.insertItem(18, '빛나는 암흑 수류탄')
        self.leftlist.insertItem(19, '빛나는 수면 폭탄')
        self.leftlist.insertItem(20, '빛나는 파괴 폭탄')
        self.leftlist.insertItem(21, '빛나는 부식 폭탄')
        self.leftlist.insertItem(22, '빛나는 성스러운 폭탄')

        self.flash = QWidget()
        self.flame = QWidget()
        self.coldair = QWidget()
        self.electric = QWidget()
        self.dark = QWidget()
        self.corrosion = QWidget()
        self.thunder = QWidget()
        self.Tornado = QWidget()
        self.clay = QWidget()
        self.sleeping = QWidget()
        self.holy = QWidget()
        self.destruction = QWidget()
        self.s_flash = QWidget()
        self.s_flame = QWidget()
        self.s_coldair = QWidget()
        self.s_electric = QWidget()
        self.s_clay = QWidget()
        self.s_tornado = QWidget()
        self.s_dark = QWidget()
        self.s_sleeping = QWidget()
        self.s_destruction = QWidget()
        self.s_corrosion = QWidget()
        self.s_holy = QWidget()



        Attack_ItemUI.Flash(self)
        Attack_ItemUI.Flame(self)
        Attack_ItemUI.Cold_Air(self)
        Attack_ItemUI.Electric(self)
        Attack_ItemUI.Dark(self)
        Attack_ItemUI.Corrosion(self)
        Attack_ItemUI.Thunder(self)
        Attack_ItemUI.Tornado(self)
        Attack_ItemUI.Clay(self)
        Attack_ItemUI.Sleeping(self)
        Attack_ItemUI.Holy(self)
        Attack_ItemUI.Destruction(self)
        Attack_ItemUI.S_Flash(self)
        Attack_ItemUI.S_Flame(self)
        Attack_ItemUI.S_Cold_Air(self)
        Attack_ItemUI.S_Electric(self)
        Attack_ItemUI.S_Clay(self)
        Attack_ItemUI.S_Tornado(self)
        Attack_ItemUI.S_Dark(self)
        Attack_ItemUI.S_Sleeping(self)
        Attack_ItemUI.S_Destruction(self)
        Attack_ItemUI.S_Corrosion(self)
        Attack_ItemUI.S_Holy(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.flash)
        self.Stack.addWidget(self.flame)
        self.Stack.addWidget(self.coldair)
        self.Stack.addWidget(self.electric)
        self.Stack.addWidget(self.dark)
        self.Stack.addWidget(self.corrosion)
        self.Stack.addWidget(self.thunder)
        self.Stack.addWidget(self.Tornado)
        self.Stack.addWidget(self.clay)
        self.Stack.addWidget(self.sleeping)
        self.Stack.addWidget(self.holy)
        self.Stack.addWidget(self.destruction)
        self.Stack.addWidget(self.s_flash)
        self.Stack.addWidget(self.s_flame)
        self.Stack.addWidget(self.s_coldair)
        self.Stack.addWidget(self.s_electric)
        self.Stack.addWidget(self.s_clay)
        self.Stack.addWidget(self.s_tornado)
        self.Stack.addWidget(self.s_dark)
        self.Stack.addWidget(self.s_sleeping)
        self.Stack.addWidget(self.s_destruction)
        self.Stack.addWidget(self.s_corrosion)
        self.Stack.addWidget(self.s_holy)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()

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
        tabs.addTab(self.Tab_Potion(), '포션')
        tabs.addTab(self.Tab_Special_Item(), '특수 아이템')
        tabs.addTab(self.Tab_Attack_Item(), '공격 아이템')
        tabs.addTab(self.Tab_Combat_Assistance(), '전투보조 아이템')
        self.setCentralWidget(tabs)

    def Tab_Potion(self):
        wg = Potion()
        self.setCentralWidget(wg)

        hbox = QHBoxLayout()
        hbox.addWidget(wg)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab
    
    def Tab_Special_Item(self):
        wg = Special_Item()
        self.setCentralWidget(wg)

        hbox = QHBoxLayout()
        hbox.addWidget(wg)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab

    def Tab_Attack_Item(self):
        wg = Attack_Item()
        self.setCentralWidget(wg)

        hbox = QHBoxLayout()
        hbox.addWidget(wg)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab

    def Tab_Combat_Assistance(self):
        wg = Combat_Assistance()
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
