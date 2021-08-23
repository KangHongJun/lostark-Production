import sys
import pandas as pd
from pandas import Series, DataFrame
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import Attack_Item_list
Attack_Item_list.Attack()

#read db life_list 
conn = sqlite3.connect("life.db")
Life = pd.read_sql("SELECT * FROM life",conn,index_col=None)
Life_list = Life.values.tolist()

#read db Attack_item
conn = sqlite3.connect("Attack_item.db")
Attack = pd.read_sql("SELECT * FROM Attack_item",conn,index_col=None)
Attack_list = Attack.values.tolist()
  
class Get_Profit():
  def four(self,x,y,z,p):
    return x+y+z+p
  
  
def Flash(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("섬광 수류탄\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x3 - " + "골드") 

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x24")
  label4.setText(str(df_list[0][2]))
  
  label5 = QLabel()
  label5.setText("철광석x5")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][20])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)

def Flame(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("화염 수류탄\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x3 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x24")
  label4.setText(str(df_list[0][2]))
  
  label5 = QLabel()
  label5.setText("부드러운 목재x2")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][18])
  propit.setText("제작템-수수료 - get = 이익금")
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)

def Cold_Air (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("냉기 수류탄\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x3 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x24")
  label4.setText(str(df_list[0][2]))
  
  label5 = QLabel()
  label5.setText("철광석x5")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][20])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)

def Electric  (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("전기 수류탄\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x3 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x24")
  
  label5 = QLabel()
  label5.setText("철광석x5")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][20])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)      

def Dark(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("암흑 수류탄\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x3 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x24")
  
  label5 = QLabel()
  label5.setText("부드러운 목재x3")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][18])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)

def Corrosion(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("부식 폭탄\n")
  
  label2 = QLabel()
  label2.setText("화려한 버섯x4 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x32")
  
  label5 = QLabel()
  label5.setText("묵직한 철광석x6")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][21])
  propit.setText("제작템-수수료 - get = 이익금")
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)

def Thunder(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("천둥 물약\n")

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
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][25])
  propit.setText("제작템-수수료 - get = 이익금")
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)

def Tornado(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("회오리 수류탄\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x3 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x24")
  
  label5 = QLabel()
  label5.setText("철광석x5")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][20])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)

def Clay(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("점토 수류탄\n")


  label2 = QLabel()
  label2.setText("화려한 버섯x3 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x24")
  
  label5 = QLabel()
  label5.setText("철광석x5")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][20])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)     

def Sleeping(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("수면 폭탄\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x4 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText('투박한 버섯x32')
  
  label5 = QLabel()
  label5.setText('철광석x10')

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][20])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)  
  

##  
def Holy(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("성스러운 폭탄\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x3 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText('투박한 버섯x24')
  
  label5 = QLabel()
  label5.setText('철광석x3')

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][20])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)
  
def Destruction (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("파괴 폭탄\n")

 label2 = QLabel()
  label2.setText("화려한 버섯x4 - " + "골드")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText('투박한 버섯x32')
  
  label5 = QLabel()
  label5.setText('묵직한 철광석x6')

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11], Life_list[2][10], Life_list[2][9], Life_list[2][21])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)
  
def S_Flash (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 섬광 수류탄\n")

  label2 = QLabel()
  label2.setText("섬광 수류탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x4")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four()
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)

  self.stack1.setLayout(layout)
  
def S_Flame(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 화염 수류탄\n")

  label2 = QLabel()
  label2.setText("화염 수류탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x4")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)
  
def S_Cold_Air (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 냉기 수류탄\n")

 label2 = QLabel()
  label2.setText("냉기 수류탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x4")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)

  self.stack1.setLayout(layout)
  
def S_Electric (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 전기 수류탄\n")

  label2 = QLabel()
  label2.setText("전기 수류탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x4")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)

  self.stack1.setLayout(layout)
  
def S_Clay (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 점토 수류탄\n")

  label2 = QLabel()
  label2.setText("점토 수류탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x4")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  self.stack1.setLayout(layout)  
  
def S_Tornado  (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 회오리 수류탄\n")

  label2 = QLabel()
  label2.setText("회오리 수류탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x4")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)

  self.stack1.setLayout(layout)  
  
def S_Dark (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 암흑 수류탄\n")

  label2 = QLabel()
  label2.setText("암흑 수류탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x4")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11])
  propit.setText("제작템-수수료 - get = 이익금")
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)    
  
def S_sleeping(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 수면 폭탄\n")

  label2 = QLabel()
  label2.setText("수면 폭탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x2")

  label5 = QLabel()
  label5.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)      
  

def S_Destruction (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 파괴 폭탄\n")

  label2 = QLabel()
  label2.setText("파괴 폭탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x2")

  label5 = QLabel()
  label5.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][11])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)     
  
def S_Corrosion (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 부식 폭탄\n")

  label2 = QLabel()
  label2.setText("수줍은 들꽃x5 - " + "골드")

  label3 = QLabel()
  label3.setText("들꽃x10")

  label4 = QLabel()
  label4.setText('실링 x1200')
  label4.setText(str(df_list[0][2]))

  label5 = QLabel()
  label5.setText("0골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[2][6], Life_list[2][7])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)    
  
def S_Holy(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 성스러운 폭탄\n")

  label2 = QLabel()
  label2.setText("수줍은 들꽃x5 - " + "골드")

  label3 = QLabel()
  label3.setText("들꽃x10")

  label4 = QLabel()
  label4.setText('실링 x1200')
  label4.setText(str(df_list[0][2]))

  label5 = QLabel()
  label5.setText("0골드")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)      

def display(self, i):
  self.Stack.setCurrentIndex(i)




