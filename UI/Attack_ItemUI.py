import pandas as pd
from multipledispatch import dispatch
from PyQt5.QtWidgets import *
import sqlite3

#Attack_Item_list.Attack()

#read db life_list 
conn = sqlite3.connect("life.db")
Life = pd.read_sql("SELECT * FROM life",conn,index_col=None)
Life_list = Life.values.tolist()

#read db Attack_item
conn = sqlite3.connect("Attack_item.db")
Attack = pd.read_sql("SELECT * FROM Attack_item",conn,index_col=None)
Attack_list = Attack.values.tolist()

#class Material_price를 아래의 수수료 / 이익금 까지 넣을지 고민

class Material_price():
  @dispatch(float, int, float, int, float, int, float, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, Item_four, fourth, Item_five, fifth, fee):
    result = (Item_one * first) + (Item_two * second) + (Item_three * third) + (Item_four * fourth) + (Item_five * fifth) + fee
    return round(result, 2)

  @dispatch(float, int, float, int, float, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, Item_four, fourth, fee):
    result = (Item_one * first) + (Item_two * second) + (Item_three * third) + (Item_four * fourth) + fee
    return round(result, 2)

  @dispatch(float, int, float, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, fee):
    result = (Item_one * first) + (Item_two * second) + (Item_three * third) + fee
    return round(result, 2)

  @dispatch(int, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, fee):
    result = (Item_one * first) + (Item_two * second) + fee
    return round(result, 2)


# 수수료
def Lifting(value):
  if (value == 1):
    return 0
  if (value < 20):
    return 1
  if ((value * 0.05) % 10 != 0):
    value = int(value * 0.05) + 1
    return value
  if ((value * 0.05) % 10 == 0):
    return int(value * 0.05)

  # 템 값(수수료빠진 값) - 재료값 = 이익 /


def Set_Profit(Item, Item_Num, Mprice):
  Lift_Item = Lifting(Item) * Item_Num
  Item = Item * Item_Num
  text = str(Item) + "(" + str(Lift_Item) + ")" + "-" + str(Mprice) + "=" + str(
    round(Item - Lift_Item - Mprice, 2)) + "골드"
  return text
  

def Flash(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("섬광 수류탄x3\n")

  label2 = QLabel()
  label2.setText("화려한 버섯x3")

  label3 = QLabel()
  label3.setText("싱싱한 버섯x12")

  label4 = QLabel()
  label4.setText("투박한 버섯x24")
  
  label5 = QLabel()
  label5.setText("철광석x5")

  label6 = QLabel()
  label6.setText("15골드\n")
  
  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],3, Life_list[9][2],12, Life_list[8][2],24, Life_list[19][2],5, 15)
  propit.setText(Set_Profit(Attack_list[0][2],3,mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.flash.setLayout(layout)

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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],3, Life_list[9][2],12, Life_list[8][2],24, Life_list[17][2],2,15)
  propit.setText(Set_Profit(Attack_list[1][2],3,mprice))
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.flame.setLayout(layout)

def Cold_Air(self):
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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],3 ,Life_list[9][2],12, Life_list[8][2],24, Life_list[19][2],5,15)
  propit.setText(Set_Profit(Attack_list[2][2],3, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.coldair.setLayout(layout)

def Electric(self):
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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],3, Life_list[9][2],12, Life_list[8][2],24, Life_list[19][2],5,15)
  propit.setText(Set_Profit(Attack_list[3][2],3, mprice))
             
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.electric.setLayout(layout)      

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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],3, Life_list[9][2],12, Life_list[8][2],24, Life_list[17][2],3,15)
  propit.setText(Set_Profit(Attack_list[4][2],3, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.dark.setLayout(layout)

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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],4, Life_list[9][2],12, Life_list[8][2],32, Life_list[20][2],6,15)
  propit.setText(Set_Profit(Attack_list[5][2],3, mprice))
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.corrosion.setLayout(layout)

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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],4, Life_list[9][2],16, Life_list[8][2],32, Life_list[24][2],5,15)
  propit.setText(Set_Profit(Attack_list[6][2],3, mprice))
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.thunder.setLayout(layout)

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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],3, Life_list[9][2],12, Life_list[8][2],24, Life_list[19][2],5,15)
  propit.setText(Set_Profit(Attack_list[7][2],3, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)           
  layout.addWidget(propit)

  self.Tornado.setLayout(layout)

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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],3, Life_list[9][2],12, Life_list[8][2],24, Life_list[19][2],5,15)
  propit.setText(Set_Profit(Attack_list[8][2],3, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.clay.setLayout(layout)     

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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],4, Life_list[9][2],12, Life_list[8][2],32, Life_list[19][2],10,15)
  propit.setText(Set_Profit(Attack_list[9][2],3, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.sleeping.setLayout(layout)  
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],3, Life_list[9][2],12, Life_list[8][2],24, Life_list[19][2],3,15)
  propit.setText(Set_Profit(Attack_list[10][2],3, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.holy.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[10][2],4, Life_list[9][2],12, Life_list[8][2],32, Life_list[20][2],6,15)
  propit.setText(Set_Profit(Attack_list[11][2],3, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(propit)

  self.destruction.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[0][2],3,Life_list[10][2],4,15)
  propit.setText(Set_Profit(Attack_list[12][2],2, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)

  self.s_flash.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[1][2],3,Life_list[10][2],4,15)
  propit.setText(Set_Profit(Attack_list[13][2],2, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)

  self.s_flame.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[2][2],3,Life_list[10][2],4,15)
  propit.setText(Set_Profit(Attack_list[14][2],2, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)

  self.s_coldair.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[3][2],3,Life_list[10][2],4,15)
  propit.setText(Set_Profit(Attack_list[15][2],2, mprice))


  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)

  self.s_electric.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[4][2],3,Life_list[10][2],4,15)
  propit.setText(Set_Profit(Attack_list[16][2],2, mprice))


  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)
             
  self.s_clay.setLayout(layout)
  
def S_Tornado(self):
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[5][2],3,Life_list[10][2],4,15)
  propit.setText(Set_Profit(Attack_list[17][2],2, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)

  self.s_tornado.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[6][2],3,Life_list[10][2],4,15)
  propit.setText(Set_Profit(Attack_list[18][2],2, mprice))
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)

  self.s_dark.setLayout(layout)
  
def S_Sleeping(self):
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[7][2],3,Life_list[10][2],2,15)
  propit.setText(Set_Profit(Attack_list[19][2],2, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.s_sleeping.setLayout(layout)
  

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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[8][2],3,Life_list[10][2],2,15)
  propit.setText(Set_Profit(Attack_list[20][2],2, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.s_destruction.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[9][2],3,Life_list[10][2],2,15)
  propit.setText(Set_Profit(Attack_list[21][2],2, mprice))
  
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)

  self.s_corrosion.setLayout(layout)
  
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
  mprice = Material_price()
  mprice = mprice.Mprice(Attack_list[10][2],3,Life_list[10][2],4,15)
  propit.setText(Set_Profit(Attack_list[22][2],2, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(propit)

  self.s_holy.setLayout(layout)

def display(self, i):
  self.Stack.setCurrentIndex(i)




