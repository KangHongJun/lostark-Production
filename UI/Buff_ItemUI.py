import sys
import pandas as pd
from pandas import Series, DataFrame
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import Buff_Item
Buff_Item.Assistance()

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

  layout.addWidget(label1)
  layout.addWidget(label2)
  layout.addWidget(label3)
  layout.addWidget(label4)
  layout.addWidget(label5)
  layout.addWidget(profit)

  self.stack1.setLayout(layout)
  
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

  
