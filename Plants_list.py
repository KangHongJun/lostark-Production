#식물
import requests
from bs4 import BeautifulSoup

url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90200&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762402'

response = requests.get(url)

def Get_price():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
       
    
    #들꽃 
    Flower = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    int(Flower.text)
    
    #수줍은 들꽃 
    Shy_flower = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    int(Shy_flower.text)
    
    #화사한 들꽃 
    Bright_flower = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    int(Bright_flower.text)
    
    #투박한 버섯 
    Coarse_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    int(Coarse_mushroom.text)
    
    #싱싱한 버섯 
    Fresh_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    int(Fresh_mushroom.text)
    
    #화려한 버섯 
    Fancy_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    int(Fancy_mushroom.text)

       
    
    else:
        print(response.status_code)
        print('sd')
