#사냥
import requests
from bs4 import BeautifulSoup

url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90500&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762405'

response = requests.get(url)

def Get_price():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
       
    
        #다듬은 생고기 
        Meat = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
        Meat = int(Meat)
        
        #칼다르 두툼한 생고기 
        K_Meat= soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
        K_Meat = int(K_Meat)
        
        #오레하 두툼한 생고기 
        O_Meat= soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
        O_Meat = int(O_Meat)
        
        #두툼한 생고기(100) 
        Thick_Meat= soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
        Thick_Meat = int(Thick_Meat)

        #질긴가죽 
        Tough_Leather= soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
        Tough_Leather = int(Tough_Leather)
        
        #수렵 결정 (5)


       
        print(Meat)
    else:
        print(response.status_code)
        print('sd')
