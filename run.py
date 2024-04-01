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
    top10ActionMoviesRates=c.find('span',class_='legend')
    print(top10ActionMoviesRates.text)  #movie rate
    


print("if rate >5")
for c in top10ActionMovies:
    top10ActionMoviesRates=c.find('span',class_='legend')
    if(float(top10ActionMoviesRates.text)>5):
        print(c.a.text) #movie name 
        print(c.p.text) #description 
        print(top10ActionMoviesRates.text)  #movie rate
# top10ActionMoviesRates=soup.find_all('span',class_='legend')
# for c in top10ActionMoviesRates:
#     print(c.text) #movie rtes 

