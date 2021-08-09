import requests
from bs4 import BeautifulSoup

def Potion #이후 수정
    P_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60200&characterClass=&tier=0&grade=99&itemName=&pageNo=1 '/
    '&isInit=false&sortType=7&_=1627911349463'

    response = requests.get(F_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


    #회복약
    K_Carp =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    K_Carp = int(K_Carp.text)

    #고급 회복약
    O_Carp = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    O_Carp = int(O_Carp.text)

    #정령의 회복약
    Red_Fish = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Red_Fish = int(Red_Fish.text)

    #빛나는 정령의 회복약
    Pearl = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Pearl = int(Pearl.text)

    #만능 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    #빛나는 만능 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    #각성 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    #보호 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    #빛나는 보호 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    #천둥 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    #빛나는 천둥 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    #아드로핀 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    #시간 정지 물약
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    
    
    

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 1",(K_Carp,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 2", (O_Carp,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 3", (Red_Fish,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 4", (Pearl,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 5", (Fish,))
    con.commit()
