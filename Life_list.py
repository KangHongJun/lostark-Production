import requests
from bs4 import BeautifulSoup

def Fishing():
    F_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90600&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762406'

    response = requests.get(F_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


    #칼다르 태양잉어 
    K_Carp =  soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    K_Carp = int(K_Carp.text)

    #오레하 태양잉어 
    O_Carp = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    O_Carp = int(O_Carp.text)

    #붉은살 생선 
    Red_Fish = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    Red_Fish = int(Red_Fish.text)

    #자연산 진주 
    Pearl = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Pearl = int(Pearl.text)

    #생선 
    Fish = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Fish = int(Fish.text)
    #낚시 결정 5

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 1",(K_Carp,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 2", (O_Carp,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 3", (Red_Fish,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 4", (Pearl,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 5", (Fish,))
    con.commit()
    
def Plants():
    P_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90200&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762402'

    response = requests.get(P_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


     #들꽃 
    Flower = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    int(Flower.text)
    
    #수줍은 들꽃 
    Shy_flower = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    int(Shy_flower.text)
    
    #화사한 들꽃 
    Bright_flower = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    int(Bright_flower.text)
    
    #투박한 버섯 
    Coarse_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    int(Coarse_mushroom.text)
    
    #싱싱한 버섯 
    Fresh_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    int(Fresh_mushroom.text)
    
    #화려한 버섯 
    Fancy_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    int(Fancy_mushroom.text)
    
    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 6",(Flower,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 7", (Shy_flower,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 8", (Bright_flower,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 9", (Coarse_mushroom,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 10", (Fresh_mushroom,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 11", (Fancy_mushroom,))
    con.commit()
    
def Hunting():
    H_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90500&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762405'

    response = requests.get(H_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


    #다듬은 생고기 
    Meat = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    Meat = int(Meat.text)

    #두툼한 생고기(100) 
    Thick_Meat= soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
    Thick_Meat = int(Thick_Meat.text)

    #칼다르 두툼한 생고기 
    K_Meat= soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    K_Meat = int(K_Meat.text)

    #오레하 두툼한 생고기 
    O_Meat= soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    O_Meat = int(O_Meat.text)

    #질긴가죽 
    Tough_Leather= soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    Tough_Leather = int(Tough_Leather.text)

    #수렵 결정 (5)

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 12",(Meat,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 13", (Thick_Meat,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 14", (K_Meat,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 15", (O_Meat,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 16", (Tough_Leather,))
    con.commit()

def Logging():
    L_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90300&characterClass=&tier=' \
    '0&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762403'

    response = requests.get(L_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


     #목재 
    Wood = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    int(Wood.text)
    
    #부드러운 목재 
    Soft_Wood = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    int(Soft_Wood.text)
        
    #튼튼한 목재 
    Strong_Wood = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    int(Strong_Wood.text)
    
    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 17",(Wood,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 18", (Soft_Wood,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 19", (Strong_Wood,))
    con.commit()
    
def Mining_list():
    M_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90400&characterClass=&tier=0' \
    '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762404'

    response = requests.get(M_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    #철광석 
    Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    int(iron_ore.text)        

    #묵직한 철광석
    Heavy_Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    int(heavy_iron_ore.text)    

    #단단한 철광석 
    Hard_Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
    int(hard_iron_ore.text)    

    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 20",(Iron_ore,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 21", (Heavy_Iron_ore,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 22", (Hard_Iron_ore,))
    con.commit()

def Archaeology():
    A_url='https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90700&characterClass=&tier=0' \
      '&grade=99&itemName=&pageNo=1&isInit=false&sortType=7&_=1623805762408'
    
    response = requests.get(A_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


    #칼다르 유물 
    K_Relic = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
    int(K_Relic.text)

    #오레하 유물 
    O_Relic = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
    int(O_Relic.text)

    #희귀한 유물 
    Rare_Relic= soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
    int(Rare_Relic.text)

    #고대 유물 
    Ancient_Relic = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
    int(Ancient_Relic.text)

    #고고학 결정(3)
    con = sqlite3.connect("life.db")
    cursor = con.cursor()
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 23",(K_Relic,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 24", (O_Relic,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 25", (Rare_Relic,))
    cursor.execute("UPDATE life SET Price = ? WHERE Number = 26", (Ancient_Relic,))
    con.commit()


    
    
    
