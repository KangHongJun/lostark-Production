#전투보조
import requests
from bs4 import BeautifulSoup

def Assistance:
    A_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60000&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1627911349466'
   
    response = requests.get(A_url)
    
    html = response1.text
    
    soup = BeautifulSoup(html, 'html.parser')
   
    #1page
    
    #보호 물약
    Protection =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Protection = int(Healing.text)
    
    #진군의 깃발
    Flag =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Flag = int(Flag.text)
    
    #신속 로브
    Quick =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Quick = int(Quick.text)
    
    #각성 물약
    Arousal =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Arousal = int(Arousal.text)
    
    #아드로핀 물약
    Atropine =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Atropine = int(Atropine.text)
    
    #빛나는 보호 물약
    S_Protection =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    S_Protection = int(S_Protection.text)
    
    #빛나는 진군의 깃발
    S_Flag =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    S_Flag = int(S_Flag.text)
    
    #빛나는 신속 
    S_Quick =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    S_Quick = int(S_Quick.text)

    
    #etc 
    con = sqlite3.connect(".db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 5",(Protection,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 6", (Flag,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 7", (Quick,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 8", (Arousal,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 9", (Atropine,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 10", (S_Protection,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 11", (S_Flag,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 12", (S_Quick,))
    con.commit()
    
    
    
    
    
    
    
