import sys
import pandas as pd
from pandas import Series, DataFrame
from multipledispatch import dispatch
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import Attack_Item_list
Attack_Item_list.Attack()

#read db life_list 
conn = sqlite3.connect("life.db")
Life = pd.read_sql("SELECT * FROM life",conn,index_col=None)
Life_list = Life.values.tolist()

#read db etc
conn = sqlite3.connect("etc.db")
Attack = pd.read_sql("SELECT * FROM Attack_item",conn,index_col=None)
Attack_list = Attack.values.tolist()
  
#재료값*개수 + ..., 조합비)
class Material_price():
  @dispatch(int, int, int, int, int, int, int, int, int, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, Item_four, fourth, Item_five, fifth, fee):
    result = Item_one * first + Item_two * second + Item_three * third + Item_four * fourth + Item_five * fifth + fee
    return result

  @dispatch(float, int, float, int, float, int, float, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, Item_four, fourth, fee):
    result = (Item_one * first) + (Item_two * second) + (Item_three * third) + (Item_four * fourth) + fee
    print(Item_one, Item_two, Item_three, Item_four)
    return round(result, 2)

  @dispatch(int, int, int, int, int, int, int)
  def Mprice(self, Item_one, first, Item_two, second, Item_three, third, fee):
    result = Item_one * first + Item_two * second + Item_three * third + fee
    return round(result, 2)

  @dispatch(int, int, int, int, int)
  def Mprice(self, Item_one, first, Item_two, second, fee):
    result = Item_one * first + Item_two * second + fee
    return result


# 수수료
def Lifting(value):
  if (value == 1):
    return 0
  if ((value * 0.05) < 20):
    return 1
  if ((value * 0.05) % 10 != 0):
    value = int(value * 0.05) + 1
    return value
  if ((value * 0.05) % 10 == 0):
    return int(value * 0.05)

  # 템 값(수수료빠진 값) - 재료값 = 이익 /


def Set_Profit(Item, Item_Num, Mprice):
  Item = Item * Item_Num
  Lift_Item = Lifting(Item) * Item_Num
  text = str(Item) + "(" + str(Lift_Item) + ")" + "-" + str(Mprice) + "=" + str(
    round(Item - Lift_Item - Mprice, 2)) + "골드"
  return text
  
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

