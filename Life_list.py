import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.sessions import Session
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

import sqlite3


def Life():

    F_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90600&characterClass=&tier=0%27%20\%20%27&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762406%27'


    chrome_optios = webdriver.ChromeOptions()
    chrome_optios.add_argument('--headless')
    chrome_optios.add_argument('--no-sandbox')
    chrome_optios.add_argument('--disable-dev-shm-usage')
    chrome_optios.add_argument("disable-gpu")
    driver = webdriver.Chrome('C:/Users/rkdgh/chromedriver',chrome_options=chrome_optios)

    #driver.get('https://member.onstove.com/auth/login')

    driver.get('https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fMarket')
    login_x_path = '/html/body/div[1]/div[2]/div/fieldset[1]/div[3]/button'
    ID = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[1]/input')
    ID.clear()
    ID.send_keys('starmine325@gmail.com')
    PW = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[2]/input')
    PW.clear()
    PW.send_keys('starmine97@')

    #login
    driver.find_element_by_xpath(login_x_path).click()
    driver.implicitly_wait(10)
    #Life-Fishing
    driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div[1]/ul/li[8]/a').click()

    driver.get(F_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')




    # 칼다르 태양잉어
    K_Carp = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    K_Carp = int(K_Carp.text)/10

    # 오레하 태양잉어
    O_Carp = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    O_Carp = int(O_Carp.text)/10

    # 붉은살 생선
    Red_Fish = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Red_Fish = int(Red_Fish.text)/10

    # 자연산 진주
    Pearl = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Pearl = int(Pearl.text)/10

    # 생선
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)/100
    # 낚시 결정 5

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 1", (K_Carp,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 2", (O_Carp,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 3", (Red_Fish,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 4", (Pearl,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 5", (Fish,))
    con.commit()

    P_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90200&characterClass=&tier=0' \
            '&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762402'

    driver.get(P_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 들꽃
    Flower = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Flower = int(Flower.text)/100

    # 수줍은 들꽃
    Shy_flower = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Shy_flower = int(Shy_flower.text)/10

    # 화사한 들꽃
    Bright_flower = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Bright_flower = int(Bright_flower.text)/10

    # 투박한 버섯
    Coarse_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Coarse_mushroom = int(Coarse_mushroom.text)/100

    # 싱싱한 버섯
    Fresh_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    Fresh_mushroom = int(Fresh_mushroom.text)/10

    # 화려한 버섯
    Fancy_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    Fancy_mushroom = int(Fancy_mushroom.text)/10

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 6", (Flower,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 7", (Shy_flower,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 8", (Bright_flower,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 9", (Coarse_mushroom,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 10", (Fresh_mushroom,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 11", (Fancy_mushroom,))
    con.commit()

    H_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90500&characterClass=&tier=0' \
            '&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762405'

    driver.get(H_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 다듬은 생고기
    Meat = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Meat = int(Meat.text)/10

    # 두툼한 생고기(100)
    Thick_Meat = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Thick_Meat = int(Thick_Meat.text)/100

    # 칼다르 두툼한 생고기
    K_Meat = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    K_Meat = int(K_Meat.text)/10

    # 오레하 두툼한 생고기
    O_Meat = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    O_Meat = int(O_Meat.text)/10

    # 질긴가죽
    Tough_Leather = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Tough_Leather = int(Tough_Leather.text)/10

    # 수렵 결정 (5)

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 12", (Meat,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 13", (Thick_Meat,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 14", (K_Meat,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 15", (O_Meat,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 16", (Tough_Leather,))
    con.commit()

    L_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90300&characterClass=&tier=' \
            '0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762403'

    driver.get(L_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 목재
    Wood = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Wood = int(Wood.text)/100

    # 부드러운 목재
    Soft_Wood = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Soft_Wood = int(Soft_Wood.text)/10

    # 튼튼한 목재
    Strong_Wood = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Strong_Wood = int(Strong_Wood.text)/10

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 17", (Wood,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 18", (Soft_Wood,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 19", (Strong_Wood,))
    con.commit()

    M_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90400&characterClass=&tier=0' \
            '&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762404'

    driver.get(M_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 철광석
    Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Iron_ore = int(Iron_ore.text)/100

    # 묵직한 철광석
    Heavy_Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Heavy_Iron_ore = int(Heavy_Iron_ore.text)/10

    # 단단한 철광석
    Hard_Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Hard_Iron_ore = int(Hard_Iron_ore.text)/10

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 20", (Iron_ore,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 21", (Heavy_Iron_ore,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 22", (Hard_Iron_ore,))
    con.commit()

    A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90700&characterClass=&tier=0' \
            '&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

    driver.get(A_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 칼다르 유물
    K_Relic = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    K_Relic = int(K_Relic.text)/10

    # 오레하 유물
    O_Relic = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    O_Relic = int(O_Relic.text)/10

    # 희귀한 유물
    Rare_Relic = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Rare_Relic = int(Rare_Relic.text)/10

    # 고대 유물
    Ancient_Relic = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Ancient_Relic = int(Ancient_Relic.text)/100

    # 고고학 결정(3)

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 23", (K_Relic,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 24", (O_Relic,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 25", (Rare_Relic,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 26", (Ancient_Relic,))
    con.commit()




    
    
    
