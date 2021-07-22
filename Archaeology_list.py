#고고학

import requests
from bs4 import BeautifulSoup

url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90700&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762408'

response = requests.get(url)

def Get_price():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        
        #칼다르 유물 
        K_Relic = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
        int(K_Relic.text)
        
        #오레하 유물 
        O_Relic = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
        int(O_Relic.text)
        
        #희귀한 유물 
        Rare_Relic= soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
        int(Rare_Relic.text)
        
        #고대 유물 
        Ancient_Relic = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
        int(Ancient_Relic.text)
        
        #고고학 결정(3)
        con = sqlite3.connect("life.db")
        cursor = con.cursor()
        cursor.execute("UPDATE life SET Price = ? WHERE Number = 21",(K_Relic,))
        cursor.execute("UPDATE life SET Price = ? WHERE Number = 22", (O_Relic,))
        cursor.execute("UPDATE life SET Price = ? WHERE Number = 23", (Rare_Relic,))
        cursor.execute("UPDATE life SET Price = ? WHERE Number = 24", (Ancient_Relic,))
        con.commit()
       
        




