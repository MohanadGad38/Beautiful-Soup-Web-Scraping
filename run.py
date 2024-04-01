from bs4 import BeautifulSoup
import requests



htmlT=requests.get('https://elcinema.com/en/lineup/9990411/').text
# print(htmlT)
# with open('home.html','r') as html_file:
#     content=html_file.read()

soup=BeautifulSoup(htmlT,'lxml')
top10ActionMovies=soup.find_all('ul',class_='unstyled')

for c in top10ActionMovies:
    print(c.a.text) #movie name 
    print(c.p.text) #description 


top10ActionMoviesRates=soup.find_all('span',class_='legend')
for c in top10ActionMoviesRates:
    print(c.text) #movie rtes 

