import requests
from bs4 import BeautifulSoup

A_url1='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1627911349464'
A_url2='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300&characterClass=&tier=0&grade=99&itemName=&pageNo=2&isInit=false&sortType=1&_=1627911349464'
A_url3='https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300&characterClass=&tier=0&grade=99&itemName=&pageNo=3&isInit=false&sortType=1&_=1627911349464'

response1 = requests.get(A_url1)
response2 = requests.get(A_url2)
response3 = requests.get(A_url3)
  
html1 = response1.text
html2 = response2.text
html3 = response3.text
  
soup1 = BeautifulSoup(html1, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')
soup3 = BeautifulSoup(html3, 'html.parser')

#A B C에 각 값 넣음
A = []
B = []
C = []

page1 = soup1.select("td:nth-child(4) > div.price > em")
print(page1)

for x in page1:
    A.append(x.text)

page2 = soup2.select("td:nth-child(4) > div.price > em")
for x in page2:
    B.append(x.text)

page3 = soup3.select("td:nth-child(4) > div.price > em")
for x in page3:
    C.append(x.text)
    
    
    """
     A
['10', '11', '8', '3', '11', '11', '4', '11', '11', '11']
 B
['5', '11', '36', '37', '30', '18', '30', '33', '29', '24']
 C
['30', '23', '16']
    """


  
