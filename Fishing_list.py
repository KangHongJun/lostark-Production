#낚시
import requests
from bs4 import BeautifulSoup

#진주(Pearl-P)
P_DarkClouds="먹구름 진주"
P_Stain="얼룩 진주"
P_Brown="갈색 진주"
P_Dark="검은 진주"
P_ThreeColors="삼색 진주"


url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90600&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762406'
response = requests.get(url)

def Get_price():
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        #데이터 하나씩 뽑아와야함
        title = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
        print(title)
    else:
        print(response.status_code)
        print('sd')