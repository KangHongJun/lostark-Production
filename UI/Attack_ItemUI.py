import sys
import pandas as pd
from pandas import Series, DataFrame
from multipledispatch import dispatch
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
  @dispatch(int, int, int, int, int)
  def pri(self,x,y,z,p):
    return x+y+z+p
  @dispatch(int, int, int, int)
  def pri(self,x,y,z,p):
    return x+y+z+p
  @dispatch(int, int, int)
  def pri(self,x,y,z,p):
    return x+y+z+p
  @dispatch(int, int)
  def pri(self,x,y):
    return x+y
  
#수수료    
def Lifting(value):
  if(value == 1):
    return 0
  if ((value*0.05)%10 != 0):
    value = int(value*0.05) + 1
    return value
  if ((value*0.05)%10 == 0):
    return int(value*0.05)  
  
#템 값(수수료빠진 값) - 재료값 = 이익
def Set_Profit(val,get):
  Lift_val = Lifting(val)
  text = str(val) + "(" + str(Lift_val) +")" + "-" + str(get) + "=" + str(Lift_val - get)
  return text
  
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
  
  label5 = QLabel()
  label5.setText("철광석x5")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[10]21], Life_list[9][2], Life_list[8][2], Life_list[19][2],15)
  propit.setText(Set_Profit(Attack_list[0][2]), get)

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
  
  label5 = QLabel()
  label5.setText("부드러운 목재x2")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[17][2],15)
  propit.setText(Set_Profit(Attack_list[1][2]), get)
  
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
  
  label5 = QLabel()
  label5.setText("철광석x5")

  label6 = QLabel()
  label6.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[19][2],15)
  propit.setText(Set_Profit(Attack_list[2][2]), get)

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
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[19][2],15)
  propit.setText(Set_Profit(Attack_list[3][2]), get)


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
  
  label5 = QLabel()
  label5.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[17][2],15)
  propit.setText(Set_Profit(Attack_list[4][2]), get)

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
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
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[20][2],15)
  propit.setText(Set_Profit(Attack_list[5][2]), get)
  
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
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[24][2],15)
  propit.setText(Set_Profit(Attack_list[6][2]), get)
  
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
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[19][2],15)
 propit.setText(Set_Profit(Attack_list[7][2]), get)

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
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[19][2],15)
  propit.setText(Set_Profit(Attack_list[8][2]), get)

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
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[19][2],15)
  propit.setText(Set_Profit(Attack_list[9][2]), get)

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
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[19][2],15)
  propit.setText(Set_Profit(Attack_list[10][2]), get)

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
  get = get.four(Life_list[10][2], Life_list[9][2], Life_list[8][2], Life_list[20][2],15)
  propit.setText(Set_Profit(Attack_list[11][2]), get)

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
  get = get.four(Attack_list[0][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[12][2]), get)

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
  get = get.four(Attack_list[1][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[13][2]), get)

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
  label3.setText("화려한 버섯x4")ㅇ

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Attack_list[2][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[14][2]), get)

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
  get = get.four(Attack_list[3][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[15][2]), get)


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
  get = get.four(Attack_list[4][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[16][2]), get)


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
  get = get.four(Attack_list[5][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[17][2]), get)

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
  get = get.four(Attack_list[6][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[18][2]), get)
  
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
  get = get.four(Attack_list[7][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[19][2]), get)

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
  get = get.four(Attack_list[8][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[20][2]), get)

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
  label2.setText("부식 폭탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x2")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Attack_list[9][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[21][2]), get)
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)    
  
def S_Holy(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 성스러운 폭탄\n")

  label2 = QLabel()
  label2.setText("성스러운 폭탄x3 - " + "골드")

  label3 = QLabel()
  label3.setText("화려한 버섯x4")

  label4 = QLabel()
  label4.setText("15골드")
  
  propit = QLabel()
  get = Get_Profit()
  get = get.four(Attack_list[10][2],Life_list[10][2],15)
  propit.setText(Set_Profit(Attack_list[22][2]), get)

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)      

def display(self, i):
  self.Stack.setCurrentIndex(i)




