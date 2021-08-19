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
attack = pd.read_sql("SELECT * FROM Attack_item",conn,index_col=None)
attack_list = attack.values.tolist()

  
  
def Flash(self):
      layout = QFormLayout()

      label1 = QLabel()
      label1.setText("섬광 수류탄\n")

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
      
def Flame(self):
      layout = QFormLayout()

      label1 = QLabel()
      label1.setText("화염 수류탄\n")

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

def Cold_Air (self):
      layout = QFormLayout()

      label1 = QLabel()
      label1.setText("냉기 수류탄\n")

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
     
def Dark(self):
      layout = QFormLayout()

      label1 = QLabel()
      label1.setText("엄훅 수류탄\n")

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
      
def Corrosion(self):
      layout = QFormLayout()

      label1 = QLabel()
      label1.setText("부식 폭탄\n")

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
      
def Flash(self):
      layout = QFormLayout()

      label1 = QLabel()
      label1.setText("섬광 수류탄\n")

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

def Flash(self):
      layout = QFormLayout()

      label1 = QLabel()
      label1.setText("섬광 수류탄\n")

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
      
def Flash(self):
      layout = QFormLayout()

      label1 = QLabel()
      label1.setText("섬광 수류탄\n")

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

      
        
        
