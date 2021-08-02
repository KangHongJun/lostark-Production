import requests
from bs4 import BeautifulSoup
#파싱기본

url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90400&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762400'

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

#데이터 뽑아서 DB에 넣고 main에서 읽어오는 형식





