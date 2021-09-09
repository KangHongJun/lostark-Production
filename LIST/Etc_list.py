# 전투보조
import requests
from bs4 import BeautifulSoup
import sqlite3
from selenium import webdriver


def Etc():
    E_url1 = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010&characterClass=&tier=0&grade=99' \
            '&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'
    E_url2 = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010&characterClass=&tier=0&grade=99' \
             '&itemName=&pageNo=3&isInit=false&sortType=1&_=1623805762408'

    chrome_optios = webdriver.ChromeOptions()
    chrome_optios.add_argument('--headless')
    chrome_optios.add_argument('--no-sandbox')
    chrome_optios.add_argument('--disable-dev-shm-usage')
    chrome_optios.add_argument("disable-gpu")
    driver = webdriver.Chrome('C:/Users/rkdgh/chromedriver', chrome_options=chrome_optios)

    # driver.get('https://member.onstove.com/auth/login')

    driver.get(
        'https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fMarket')
    login_x_path = '/html/body/div[1]/div[2]/div/fieldset[1]/div[3]/button'
    ID = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[1]/input')
    ID.clear()
    ID.send_keys('starmine325@gmail.com')
    PW = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[2]/input')
    PW.clear()
    PW.send_keys('starmine97@')

    # login
    driver.find_element_by_xpath(login_x_path).click()
    driver.implicitly_wait(10)
    # Life-Fishing
    driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div[1]/ul/li[8]/a').click()

    # 1page
    driver.get(E_url1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 하급 오레하 융합
    Low_union = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Low_union = int(Low_union.text)

    # 중급 오레하 융합
    Mid_union = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Mid_union = int(Mid_union.text)


    con = sqlite3.connect("Etc.db")
    cursor = con.cursor()
    cursor.execute("UPDATE Etc SET Price = ? WHERE Number = 1", (Low_union,))
    cursor.execute("UPDATE Etc SET Price = ? WHERE Number = 2", (Mid_union,))

    # 3page
    driver.get(E_url2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    # 상급 오레하 융합
    High_union = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    High_union = int(High_union.text)

    cursor.execute("UPDATE Etc SET Price = ? WHERE Number = 3", (High_union,))
    con.commit()











