#채광

import requests
from bs4 import BeautifulSoup

url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90400&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762404'

response = requests.get(url)

def Mining_price():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        #철광석 
        Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
        int(iron_ore.text)        
        
        #묵직한 철광석
        Heavy_Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
        int(heavy_iron_ore.text)    
    
        #단단한 철광석 
        Hard_Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
        int(hard_iron_ore.text)    
        
        con = sqlite3.connect("life.db")
        cursor = con.cursor()
        cursor.execute("UPDATE life SET Price = ? WHERE Number = 18",(Iron_ore,))
        cursor.execute("UPDATE life SET Price = ? WHERE Number = 19", (Heavy_Iron_ore,))
        cursor.execute("UPDATE life SET Price = ? WHERE Number = 20", (Hard_Iron_ore,))
        con.commit()
        
        
  





