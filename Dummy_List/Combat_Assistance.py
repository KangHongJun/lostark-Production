#전투보조
import requests
from bs4 import BeautifulSoup

def Assistance:
    A_url1='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60400&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1627911349466'
    A_url2='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60400&characterClass=&tier=0&grade=99&itemName=&pageNo=2&isInit=false&sortType=1&_=1627911349466'

    response1 = requests.get(A_url1)
    response2 = requests.get(A_url2)
    
    html = response1.text
    html = response2.text
    
    soup1 = BeautifulSoup(html1, 'html.parser')
    soup2 = BeautifulSoup(html2, 'html.parser')
   
    #1page
    
    #신호탄
    Signal_Gun = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Signal_Gun = int(Signal_Gun.text)
    
    #빛나는 신호탄
    S_Signal_Gun = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_Signal_Gun = int(S_Signal_Gun.text)
    
    #만능 물약
    All_purpose = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    All_purpose = int(All_purpose.text)
    
    #도발 허수아비
    Scarecrow = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Scarecrow = int(Scarecrow.text)
    
    #모닥불
    Bonfire = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Bonfire = int(Bonfire.text)
    
    #위장 로브
    Camouflage = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Camouflage = int(Camouflage.text)
    
    #성스러운 부적
    Amulet = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Amulet = int(Amulet.text)
    
    #정비소 이동 포탈 주문서
    Spell = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Spell = int(Spell.text)
    
    #페로몬 폭탄
    Pheromones = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Pheromones = int(Pheromones.text)
    
    #빛나는 만능 물약
    S_All_purpose = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_All_purpose = int(S_All_purpose.text)
    
   
   
    #2page
    
    #빛나는 위장 로브
    S_Camouflage = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_Camouflage = int(S_Camouflage.text)
    
    #빛나는 모닥불
    S_Bonfire = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_Bonfire = int(S_Bonfire.text)
    
    #빛나는 도발 허수아비
    S_Scarecrow = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_Scarecrow = int(S_Scarecrow.text)
    
    #빛나는 성스러운 부적
    S_Amulet = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_Amulet = int(S_Amulet.text)
    
    #은신 로브
    Hiding = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Hiding = int(Hiding.text)
    
    #루테란의 나팔
    Trumpet = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Trumpet = int(Trumpet.text)
    
    #시간 정지 물약
    Signal_Gun = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    Signal_Gun = int(Signal_Gun.text)
    
    #빛나는 은신 로브
    S_Hiding = soup1.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
    S_Hiding = int(S_Hiding.text)

    
    
    
    
    
    con = sqlite3.connect("Attack_item.db")
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
    
    
    
    
    
    
    
    
    
    
    
    
