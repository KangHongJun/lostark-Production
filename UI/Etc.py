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
  get = Get_Profit()
  get = get.four(Life_list[2][12], Life_list[2][13], Life_list[2][3], Life_list[2][5])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)
  
  
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
  get = Get_Profit()
  get = get.four(Life_list[2][12], Life_list[2][13], Life_list[2][14], Life_list[2][1], Life_list[2][3], Life_list[2][5])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(label7)
  layout.addWidget(label8)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)
  
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
  get = Get_Profit()
  get = get.four(Life_list[2][12], Life_list[2][13], Life_list[2][15], Life_list[2][2], Life_list[2][3], Life_list[2][5])
  propit.setText("제작템-수수료 - get = 이익금")

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(label6)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)  
  
def display(self, i):
  self.Stack.setCurrentIndex(i)

