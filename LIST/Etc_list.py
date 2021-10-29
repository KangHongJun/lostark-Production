# 전투보조
import requests
from bs4 import BeautifulSoup
import sqlite3


def Etc(driver):
    E_url1 = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010&characterClass=&tier=0&grade=99' \
            '&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'
    E_url2 = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010&characterClass=&tier=0&grade=99' \
             '&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'

    # 1page
    driver.get(E_url1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 하급 오레하 융합
    Low_union = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
    Low_union = int(Low_union.text)


    con = sqlite3.connect("Etc.db")
    cursor = con.cursor()
    cursor.execute("UPDATE Etc SET Price = ? WHERE Number = 1", (Low_union,))


    driver.get(E_url2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 2page

    # 중급 오레하 융합
    Mid_union = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Mid_union = int(Mid_union.text)
    print(Mid_union)

    # 상급 오레하 융합
    High_union = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
    High_union = int(High_union.text)
    print(High_union)



    cursor.execute("UPDATE Etc SET Price = ? WHERE Number = 2", (Mid_union,))
    cursor.execute("UPDATE Etc SET Price = ? WHERE Number = 3", (High_union,))
    con.commit()











