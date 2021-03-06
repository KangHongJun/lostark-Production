#전투보조
import requests
from bs4 import BeautifulSoup
import sqlite3

def Assistance(driver):
    A_url1='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60400&characterClass=&tier=0&grade=99&itemName=' \
           '&pageNo=1&isInit=false&sortType=1&_=1627911349466'
    A_url2='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60400&characterClass=&tier=0&grade=99&itemName=' \
           '&pageNo=2&isInit=false&sortType=1&_=1627911349466'

    #1page
    driver.get(A_url1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #신호탄
    Signal_Gun = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Signal_Gun = int(Signal_Gun.text)
    
    #빛나는 신호탄
    S_Signal_Gun = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    S_Signal_Gun = int(S_Signal_Gun.text)
    
    #만능 물약
    All_purpose = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    All_purpose = int(All_purpose.text)
    
    #도발 허수아비
    Scarecrow = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    Scarecrow = int(Scarecrow.text)
    
    #모닥불
    Bonfire = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    Bonfire = int(Bonfire.text)
    
    #위장 로브
    Camouflage = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Camouflage = int(Camouflage.text)
    
    #성스러운 부적
    Amulet = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
    Amulet = int(Amulet.text)
    
    #정비소 이동 포탈 주문서
    Spell = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
    Spell = int(Spell.text)
    
    #페로몬 폭탄
    Pheromones = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
    Pheromones = int(Pheromones.text)
    
    #빛나는 만능 물약
    S_All_purpose = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_All_purpose = int(S_All_purpose.text)
    
    con = sqlite3.connect("Combat_Assistance.db")
    cursor = con.cursor()
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 1", (Signal_Gun,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 2", (S_Signal_Gun,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 3", (All_purpose,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 4", (Scarecrow,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 5", (Bonfire,))

    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 6", (Camouflage,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 7", (Amulet,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 8", (Spell,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 9", (Pheromones,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 10", (S_All_purpose,))
   
    #2page
    driver.get(A_url2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    #빛나는 위장 로브
    S_Camouflage = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    S_Camouflage = int(S_Camouflage.text)
    
    #빛나는 모닥불
    S_Bonfire = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    S_Bonfire = int(S_Bonfire.text)
    
    #빛나는 도발 허수아비
    S_Scarecrow = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    S_Scarecrow = int(S_Scarecrow.text)
    
    #빛나는 성스러운 부적
    S_Amulet = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    S_Amulet = int(S_Amulet.text)
    
    #은신 로브
    Hiding = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    Hiding = int(Hiding.text)
    
    #루테란의 나팔
    Trumpet = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Trumpet = int(Trumpet.text)
    
    #시간 정지 물약
    Static_time = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
    Static_time = int(Static_time.text)
    
    #빛나는 은신 로브
    #S_Hiding = soup.select_oCombat_Assistancene('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
    #S_Hiding = int(S_Hiding.text)
    
    #con = sqlite3.connect(".db")
    #cursor = con.cursor()
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 11", (S_Camouflage,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 12", (S_Bonfire,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 13", (S_Scarecrow,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 14", (S_Amulet,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 15", (Hiding,))

    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 16", (Trumpet,))
    cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 17", (Static_time,))
    #cursor.execute("UPDATE Combat_Assistance SET Price = ? WHERE Number = 18", (S_Hiding,))
    con.commit()
    
    
    
    
    
    
    
    
    
    
    
    
