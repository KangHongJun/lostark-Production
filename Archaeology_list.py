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

        #고대의 잔재(100)
        Remains_of_Ancient = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
        print(Remains_of_Ancient.text)
        #희귀한 파편
        Rare_Fragments = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
        print(Rare_Fragments)
        #희미한 양피지
        Faint_parchment = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
        print(Faint_parchment)
        #낡은 유물
        Old_Relics = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
        print(Old_Relics)
        #오레하 고대 석판
        Ancient_Lithography_O = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
        print(Ancient_Lithography_O)
        #찢어진 고문서
        Torn_old_book = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
        print(Torn_old_book)
        #베르닐 고대 석판
        Ancient_Lithography_B = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
        print(Ancient_Lithography_B)
        #칼다르 고대 석판
        Ancient_Lithography_K = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
        print(Ancient_Lithography_K)
        #조각난 문양
        Broken_Patterns = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
        print(Broken_Patterns)

    else:
        print(response.status_code)
        print('sd')





