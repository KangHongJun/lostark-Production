# 공격아이템(Bomb) - type_A

import requests
from bs4 import BeautifulSoup
import sqlite3


def Attack(driver):
    A_url1 = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300&characterClass=&tier=0&grade=99' \
             '&itemName=&pageNo=1&isInit=false&sortType=1&_=1627911349464'
    A_url2 = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300&characterClass=&tier=0&grade=99' \
             '&itemName=&pageNo=2&isInit=false&sortType=1&_=1627911349464'

    A_url3 = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300&characterClass=&tier=0&grade=99' \
             '&itemName=&pageNo=3&isInit=false&sortType=1&_=1627911349464'

    driver.get(A_url1)
    html = driver.page_source
    soup1 = BeautifulSoup(html, 'html.parser')

    driver.get(A_url2)
    html = driver.page_source
    soup2 = BeautifulSoup(html, 'html.parser')

    driver.get(A_url3)
    html = driver.page_source
    soup3 = BeautifulSoup(html, 'html.parser')

    # page1
    # 섬광수류탄
    Flash = soup1.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    print(Flash)
    Flash = int(Flash.text)

    # 화염 수류탄
    Flame = soup1.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Flame = int(Flame.text)

    # 냉기 수류탄
    Cold_Air = soup1.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Cold_Air = int(Cold_Air.text)

    # 전기수류탄
    Electric = soup1.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    Electric = int(Electric.text)

    # 암흑 수류탄
    Dark = soup1.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    Dark = int(Dark.text)

    # 부식 폭탄
    Corrosion = soup1.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Corrosion = int(Corrosion.text)

    # 천둥 물약
    Thunder = soup1.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
    Thunder = int(Thunder.text)

    # 회오리 수류탄
    Tornado = soup1.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
    Tornado = int(Tornado.text)

    # 점토 수류탄
    Clay = soup1.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
    Clay = int(Clay.text)

    # 수면 폭탄
    Sleeping = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Sleeping = int(Sleeping.text)

    con = sqlite3.connect("../Attack_item.db")
    cursor = con.cursor()
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 1", (Flash,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 2", (Flame,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 3", (Cold_Air,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 4", (Electric,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 5", (Dark,))

    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 6", (Corrosion,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 7", (Thunder,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 8", (Tornado,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 9", (Clay,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 10", (Sleeping,))
    con.commit()

    # 2apge
    # 성스러운 폭탄
    Holy = soup2.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Holy = int(Holy.text)

    # 파괴 폭탄
    Destruction = soup2.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Destruction = int(Destruction.text)

    # 빛나는 섬광 수류탄
    S_Flash = soup2.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    S_Flash = int(S_Flash.text)

    # 빛나는 화염 수류탄
    S_Flame = soup2.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    S_Flame = int(S_Flame.text)

    # 빛나는 냉기 수류탄
    S_Cold_Air = soup2.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    S_Cold_Air = int(S_Cold_Air.text)

    # 빛나는 전기 수류탄
    S_Electric = soup2.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    S_Electric = int(S_Electric.text)

    # 빛나는 점토 수류탄
    S_Clay = soup2.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
    S_Clay = int(S_Clay.text)

    # 빛나는 회오리 수류탄
    S_Tornado = soup2.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
    S_Tornado = int(S_Tornado.text)

    # 빛나는 암흑 수류탄
    S_Dark = soup2.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
    S_Dark = int(S_Dark.text)

    # 빛나는 수면 폭탄
    S_sleeping = soup2.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_sleeping = int(S_sleeping.text)

    con = sqlite3.connect("../Attack_item.db")
    cursor = con.cursor()
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 11", (Holy,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 12", (Destruction,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 13", (S_Flash,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 14", (S_Flame,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 15", (S_Cold_Air,))

    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 16", (S_Electric,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 17", (S_Clay,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 18", (S_Tornado,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 19", (S_Dark,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 20", (S_sleeping,))
    con.commit()

    # 3page
    # 빛나는 파괴 폭탄
    S_Destruction = soup3.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    S_Destruction = int(S_Destruction.text)

    # 빛나는 부식 폭탄
    S_Corrosion = soup3.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    S_Corrosion = int(S_Corrosion.text)

    # 빛나는 성스러운 폭탄
    #S_Holy = soup3.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    #S_Holy = int(S_Holy.text)

    con = sqlite3.connect("../Attack_item.db")
    cursor = con.cursor()
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 21", (S_Destruction,))
    cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 22", (S_Corrosion,))
    #cursor.execute("UPDATE Attack_item SET Price = ? WHERE Number = 23", (S_Holy,))
    con.commit()


















