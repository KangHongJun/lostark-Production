#전투보조 목롯 수정

import requests
from bs4 import BeautifulSoup

def Potion
    P_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60200&characterClass=&tier=0&grade=99&itemName=&pageNo=1 '/
    '&isInit=false&sortType=7&_=1627911349463'

    response = requests.get(F_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
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
