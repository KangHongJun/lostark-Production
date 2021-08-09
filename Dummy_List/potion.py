import requests
from bs4 import BeautifulSoup

def Potion #이후 수정
    P_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60200&characterClass=&tier=0&grade=99&itemName=&pageNo=1 '/
    '&isInit=false&sortType=7&_=1627911349463'

    response = requests.get(F_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


    #회복약
    Healing =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Healing = int(Healing.text)

    #고급 회복약
    Rare_Healing = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Rare_Healing = int(Rare_Healing.text)

    #정령의 회복약
    Spirit_Healing = Spirit_Healing.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Spirit_Healing = int(Spirit_Healing.text)

    #빛나는 정령의 회복약
    S_Spirit_Healing = S_Spirit_Healing.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    S_Spirit_Healing = int(S_Spirit_Healing.text)

    
    
    
    
    
    

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 1",(K_Carp,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 2", (O_Carp,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 3", (Red_Fish,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 4", (Pearl,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 5", (Fish,))
    con.commit()
