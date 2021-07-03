#낚시
import sqlite3
import requests
from bs4 import BeautifulSoup

#진주(Pearl-P)
P_DarkClouds="먹구름 진주"
P_Stain="얼룩 진주"




#1페이지
page1_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90600&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762406'
response1 = requests.get(page1_url)
#2페이지
page2_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90600&characterClass=&tier=0' \
          '&grade=99&itemName=&pageNo=2&isInit=false&sortType=7&_=1625207570513'

response2 = requests.get(page2_url)

def Fishing_price():
    if response2.status_code == 200:
        html = response2.text
        soup = BeautifulSoup(html, 'html.parser')

        #갈색 진주
        P_Brown = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
        P_Brown = int(P_Brown.text)
        #검은 진주
        P_Dark = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
        #삼색 진주
        P_ThreeColors = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')

        print(P_Brown)
        print(P_Dark)
        print(P_ThreeColors)


        con = sqlite3.connect("test.db")
        cursor = con.cursor()
        cursor.execute("UPDATE test SET ID = ? WHERE NAME='sd'",(P_Brown,))
        con.commit()









