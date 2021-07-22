#벌목
import requests
from bs4 import BeautifulSoup

url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90300&characterClass=&tier=' \
    '0&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762403'

response = requests.get(url)

def Get_price():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
       
    #목재 
    Wood = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    int(Wood.text)
    
    #부드러운 목재 
    Soft_Wood = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    int(Soft_Wood.text)
        
    #튼튼한 목재 
    Strong_Wood = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    int(Strong_Wood.text)
    
    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 15",(Wood,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 16", (Soft_Wood,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 17", (Strong_Wood,))
    con.commit()
