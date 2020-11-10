import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.jtbc.joins.com/html/165/NB11978165.html')
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())