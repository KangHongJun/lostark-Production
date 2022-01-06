import pandas as pd
from multipledispatch import dispatch
from PyQt5.QtWidgets import *
import sqlite3

#read db life_list 
conn = sqlite3.connect("life.db")
Life = pd.read_sql("SELECT * FROM life",conn,index_col=None)
Life_list = Life.values.tolist()

#read db etc
conn = sqlite3.connect("etc.db")
etc = pd.read_sql("SELECT * FROM Etc",conn,index_col=None)
etc_list = etc.values.tolist()

#read db data
from UI import getdata
a = getdata.getdata_db()
print("test"+str(a.dbetc_list[0][0]))

#재료값*개수 + ..., 조합비)
class Material_price():
  @dispatch(float, int, float, int, float, int, float, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, Item_four, fourth, Item_five, fifth, fee):
    result = Item_one * first + Item_two * second + Item_three * third + Item_four * fourth + Item_five * fifth + fee
    return result

  @dispatch(float, int, float, int, float, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, Item_four, fourth, fee):
    result = (Item_one * first) + (Item_two * second) + (Item_three * third) + (Item_four * fourth) + fee
    return round(result, 2)

  @dispatch(float, int, float, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, fee):
    result = Item_one * first + Item_two * second + Item_three * third + fee
    return round(result, 2)

  @dispatch(float, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, fee):
    result = Item_one * first + Item_two * second + fee
    return result


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
  Min_Item = Item * Item_Num
  Item = (Item+1) * Item_Num
  Min_Item_price = round(Min_Item - Lift_Item - Mprice, 2)
  Item_price = round(Item - Lift_Item - Mprice, 2)

  text = str(Min_Item) + " - " + str(Lift_Item) + " - " + str(Mprice) + " = " + str(Min_Item_price) + " ~ " + str(Item_price) +"골드"
  return text

#수렵
def H_Low(self):

  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("하급 오레하 융화재료x30\n")

  label2 = QLabel()
  label2.setText("오레하 두툼한 생고기x9")

  label3 = QLabel()
  label3.setText("두툼한 생고기x72")

  label4 = QLabel()
  label4.setText("질긴 가죽x36")

  label5 = QLabel()
  label5.setText("203골드")

  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[14][2],9,Life_list[12][2],72,Life_list[15][2],36,203)
  propit.setText(Set_Profit(etc_list[0][2], 30, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.h_low.setLayout(layout)

def H_Mid(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("중급 오레하 융화재료x30\n")

  label2 = QLabel()
  label2.setText("오레하 두툼한 생고기x10")

  label3 = QLabel()
  label3.setText("두툼한 생고기x80")

  label4 = QLabel()
  label4.setText("질긴 가죽x40")

  label5 = QLabel()
  label5.setText("205골드")

  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[14][2], 10, Life_list[12][2], 80, Life_list[15][2], 40, 205)
  propit.setText(Set_Profit(etc_list[1][2], 30, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.h_mid.setLayout(layout)

def H_High(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("상급 오레하 융화재료x20\n")

  label2 = QLabel()
  label2.setText("오레하 두툼한 생고기x16")

  label3 = QLabel()
  label3.setText("두툼한 생고기x128")

  label4 = QLabel()
  label4.setText("질긴 가죽x64")

  label5 = QLabel()
  label5.setText("250골드")

  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[14][2], 16, Life_list[12][2], 128, Life_list[15][2], 64, 250)
  propit.setText(Set_Profit(etc_list[2][2], 20, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.h_high.setLayout(layout)

def F_Low(self):

  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("하급 오레하 융화재료x30\n")

  label2 = QLabel()
  label2.setText("오레하 태양 잉어x9")

  label3 = QLabel()
  label3.setText("생선x72")

  label4 = QLabel()
  label4.setText("자연산 진주x36")

  label5 = QLabel()
  label5.setText("203골드")

  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[1][2],9,Life_list[4][2],72,Life_list[3][2],36,203)
  propit.setText(Set_Profit(etc_list[0][2], 30, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.f_low.setLayout(layout)

def F_Mid(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("중급 오레하 융화재료x30\n")

  label2 = QLabel()
  label2.setText("오레하 태양 잉어x10")

  label3 = QLabel()
  label3.setText("생선x80")

  label4 = QLabel()
  label4.setText("자연산 진주x40")

  label5 = QLabel()
  label5.setText("205골드")

  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[1][2], 10, Life_list[4][2], 80, Life_list[3][2], 40, 205)
  propit.setText(Set_Profit(etc_list[1][2], 30, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.f_mid.setLayout(layout)

def F_High(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("상급 오레하 융화재료x20\n")

  label2 = QLabel()
  label2.setText("오레하 태양 잉어x16")

  label3 = QLabel()
  label3.setText("생선x128")

  label4 = QLabel()
  label4.setText("자연산 진주x64")

  label5 = QLabel()
  label5.setText("250골드")

  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[1][2], 16, Life_list[4][2], 128, Life_list[3][2], 64, 250)
  propit.setText(Set_Profit(etc_list[2][2], 20, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.f_high.setLayout(layout)

def A_Low(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("하급 오레하 융화재료x30\n")

  label2 = QLabel()
  label2.setText("오레하 유물x7")

  label3 = QLabel()
  label3.setText("희귀한 유물x28")

  label4 = QLabel()
  label4.setText("고대 유물x56")

  label5 = QLabel()
  label5.setText("골드203")


  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[23][2],9,Life_list[24][2],28,Life_list[25][2],56,203)
  propit.setText(Set_Profit(etc_list[0][2], 30, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.a_low.setLayout(layout)

def A_Mid(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("중급 오레하 융화재료x30\n")

  label2 = QLabel()
  label2.setText("오레하 유물x8")

  label3 = QLabel()
  label3.setText("희귀한 유물x26")

  label4 = QLabel()
  label4.setText("고대 유물x64")

  label5 = QLabel()
  label5.setText("골드205")


  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[23][2],8,Life_list[24][2],26,Life_list[25][2],64,205)
  propit.setText(Set_Profit(etc_list[1][2], 30, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.a_mid.setLayout(layout)

def A_High(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("상급 오레하 융화재료x20\n")

  label2 = QLabel()
  label2.setText("오레하 유물x16")

  label3 = QLabel()
  label3.setText("희귀한 유물x29")

  label4 = QLabel()
  label4.setText("고대 유물x94")

  label5 = QLabel()
  label5.setText("골드250")


  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[23][2],16,Life_list[24][2],29,Life_list[25][2],94,250)
  propit.setText(Set_Profit(etc_list[2][2], 20, mprice))

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(propit)

  self.a_high.setLayout(layout)

#요리는 3가지-보류  
def Artisan(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("장인의 요리시리즈\n")

  label2 = QLabel()
  label2.setText("다듬은 생고기x20 - " + "골드") 

  label3 = QLabel()
  label3.setText("두툼한 생고기x32")
  
  label4 = QLabel()
  label4.setText("붉은 살 생선x20")

  label5 = QLabel()
  label5.setText("생선x32")
  
  label6 = QLabel()
  label6.setText("실링x1000")
  
  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[11][2], Life_list[12][2], Life_list[2][2], Life_list[4][2])
  propit.setText(Set_Profit("추가"), mprice)

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)


  self.artisan.setLayout(layout)
  
  
def Maven(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("달인의 요리 시리즈\n")

  label2 = QLabel()
  label2.setText("다듬은 생고기x20 - " + "골드") 

  label3 = QLabel()
  label3.setText("두툼한 생고기x40")
  
  label4 = QLabel()
  label4.setText("칼다르 두툼한 생고기x5 - " + "골드") 
  
  label5 = QLabel()
  label5.setText("칼다르 태양 잉어x20")
  
  label6 = QLabel()
  label6.setText("붉은 살 생선x20")

  label7 = QLabel()
  label7.setText("생선x32")

  label8 = QLabel()
  label8.setText("20골드")
  
  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[11][2], Life_list[12][2], Life_list[13][2], Life_list[0][2], Life_list[2][2], Life_list[4][2])
  propit.setText(Set_Profit("추가"), mprice)
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(label7)
  layout.addWidget(label8)


  self.maven.setLayout(layout)
  
def Matser(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("명인의 요리 시리즈\n")

  label2 = QLabel()
  label2.setText("다듬은 생고기x24 - " + "골드") 

  label3 = QLabel()
  label3.setText("두툼한 생고기x48")
  
  label2 = QLabel()
  label2.setText("오레하 두툼한 생고기x6 - " + "골드") 
  
  label4 = QLabel()
  label4.setText("오레하 태양 잉어x5")
  
  label4 = QLabel()
  label4.setText("붉은 살 생선x20")

  label5 = QLabel()
  label5.setText("생선x40")
  
  label6 = QLabel()
  label6.setText("35골드")
  
  propit = QLabel()
  mprice = Material_price()
  mprice = mprice.Mprice(Life_list[11][2], Life_list[12][2], Life_list[14][2], Life_list[1][2], Life_list[2][2], Life_list[4][2])
  propit.setText(Set_Profit(Life_list[1][1], mprice))
  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)

  self.matser.setLayout(layout)  
  
def display(self, i):
  self.Stack.setCurrentIndex(i)

