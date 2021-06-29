import requests
from bs4 import BeautifulSoup

url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90400&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762400'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(1) > div > span.slot')
    print(title)
else : 
    print(response.status_code)


import requests
from bs4 import BeautifulSoup

url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90400&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762400'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(2) > div > em')
    print(title)
else : 
    print(response.status_code)




