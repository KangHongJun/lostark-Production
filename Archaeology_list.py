#고고학

import requests
from bs4 import BeautifulSoup

url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90700&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762408'

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





