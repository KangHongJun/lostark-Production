#낚시
import sqlite3
import requests
from bs4 import BeautifulSoup

#1페이지
page1_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90600&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762406'
response = requests.get(page1_url)


def Fishing_price():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        #칼다르 태양잉어 
        K_Carp =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
        K_Carp = int(K_Carp.text)
        
        #오레하 태양잉어 
        O_Carp = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
        O_Carp = int(O_Carp.text)
        
        #붉은살 생선 
        Red_Fish = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
        Red_Fish = int(Red_Fish.text)
        
        #자연산 진주 
        Pearl = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
        Pearl = int(Pearl.text)
        
        #생선 
        Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
        Fish = int(Fish.text)
        #낚시 결정 5

        
        
        print(K_Carp)
        


        con = sqlite3.connect("test.db")
        cursor = con.cursor()
        cursor.execute("UPDATE test SET ID = ? WHERE NAME='sd'",(K_Carp,))
        con.commit()









