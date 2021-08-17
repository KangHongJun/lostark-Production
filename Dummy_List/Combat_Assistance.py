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
    
    #빛나는 신호탄
    
    #만능 물약
    
    #도발 허수아비
    
    #모닥불
    
    #위장 로브
    
    #성스러운 부적
    
    #정비소 이동 포탈 주문서
    
    #페로몬 폭탄
    
    #빛나는 만능 물약
   
   
    #2page
    
    #빛나는 위장 로브
    
    #빛나는 모닥불
    
    #빛나는 도발 허수아비
    
    #빛나는 성스러운 부적
    
    #은신 로브
    
    #루테란의 나팔
    
    #시간 정지 물약
    
    #빛나는 은신 로브
    
    
    
    
    
    
    
    
    
    
    
    
    
