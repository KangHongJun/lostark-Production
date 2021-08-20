import sys
import pandas as pd
from pandas import Series, DataFrame
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import Combat_AssistanceUI
Combat_AssistanceUI.Assistance()

#read db life_list 
conn = sqlite3.connect("life.db")
Life = pd.read_sql("SELECT * FROM life",conn,index_col=None)
Life_list = Life.values.tolist()

#read db Attack_item
conn = sqlite3.connect("Attack_item.db")
attack = pd.read_sql("SELECT * FROM Attack_item",conn,index_col=None)
attack_list = attack.values.tolist()

  
  
def Signal_Gun (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("신호탄\n")

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
  
 def S_Signal_Gun (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 신호탄\n")

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
  
def All_purpose(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("만능 물약\n")

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

def Scarecrow (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("도발 허수아비\n")

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

def Bonfire (self):
    layout = QFormLayout()

    label1 = QLabel()
    label1.setText("모닥불\n")

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

def Camouflage(self):
    layout = QFormLayout()

    label1 = QLabel()
    label1.setText("위장 로브\n")

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

def Amulet(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("성스러운 부적\n")

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

def Spell(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("정비소 이동 포탈 주문서\n")

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

def Pheromones(self):
    layout = QFormLayout()

    label1 = QLabel()
    label1.setText("페로몬 폭탄\n")

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
    
def S_All_purpose(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 만능 물약\n")

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
  
def S_Camouflage(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 위장 로부\n")

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
  
def S_Bonfire(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 모닥불\n")

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
  
def S_Scarecrow(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 도발 허수아비n")

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

def S_Amulet(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 성스러운 부적\n")

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
  
def Hiding(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("은신 로부\n")

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
  
def Trumpet(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("루테란의 나팔\n")

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
  
def S_Camouflage(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 위장 로부\n")

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
  
def Static_time(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("시간 정지 물약\n")

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
  
def S_Camouflage(self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 위장 로부\n")

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
  
def S_Hiding (self):
  layout = QFormLayout()

  label1 = QLabel()
  label1.setText("빛나는 은신 로부\n")

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



def display(self, i):
    self.Stack.setCurrentIndex(i)
