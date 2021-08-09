#공격아이템(Bomb) - type_A

import requests
from bs4 import BeautifulSoup

def Attack:
    A_url1='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60200&characterClass=&tier=0&grade=99&itemName=&pageNo=1 '/
    '&isInit=false&sortType=7&_=1627911349463'
    
    A_url2='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60200&characterClass=&tier=0&grade=99&itemName=&pageNo=2 '/
    '&isInit=false&sortType=7&_=1627911349464'
    
    A_url3='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60200&characterClass=&tier=0&grade=99&itemName=&pageNo=3 '/
    '&isInit=false&sortType=7&_=1627911349464'

    response = requests.get(F_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    #수면 폭탄
    Sleeping = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Sleeping = int(Sleeping.text)
    
     #빛나는 수면 폭탄
    S_sleeping = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    S_sleeping = int(S_sleeping.text)
    
     #성스러운 폭탄
    Holy = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Holy = int(Holy.text)
    
    #빛나는 성스러운 폭탄
    S_Holy = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    S_Holy = int(S_Holy.text)
    
    #부식 폭탄
    Corrosion = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Corrosion = int(Corrosion.text)
    
    #빛나는 부식 폭탄
    S_Corrosion = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    S_Corrosion = int(S_Corrosion.text)
    
    #파괴 폭탄
    Destruction = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Destruction = int(Destruction.text)
    
    #빛나는 파괴 폭탄
    S_Destruction = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    S_Destruction = int(S_Destruction.text)
    
    #페로몬 폭탄
    Pheromones = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Pheromones = int(Pheromones.text)
    
  
    
    
    
    
    
    
    
   
