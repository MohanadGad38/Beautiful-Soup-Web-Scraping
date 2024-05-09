from bs4 import BeautifulSoup
import requests
import json


htmlT = requests.get('https://elcinema.com/en/lineup/9990411/').text
# print(htmlT)
# with open('home.html','r') as html_file:
#     content=html_file.read()

soup = BeautifulSoup(htmlT, 'lxml')
top10ActionMovies = soup.find_all('ul', class_='unstyled')
movies: list = []
for c in top10ActionMovies:
    # print(c.a.text) #movie name
    # print(c.p.text) #description
    top10ActionMoviesRates = c.find('span', class_='legend')
    # print(top10ActionMoviesRates.text)  #movie rate
    obj = {
        "Movie  Name": c.a.text,
        "description ": c.p.text,
        "Rate": top10ActionMoviesRates.text

    }
    movies.append(obj)


with open('top10.jsonl', 'w') as f:
    json.dump(movies, f)
movies = []
print("if rate >5")
for c in top10ActionMovies:
    top10ActionMoviesRates = c.find('span', class_='legend')
    if (float(top10ActionMoviesRates.text) > 5):
        # print(c.a.text) #movie name
        # print(c.p.text) #description
        # print(top10ActionMoviesRates.text)  #movie rate
        # print(top10ActionMoviesRates.text)  #movie rate
        obj = {
            "Movie  Name": c.a.text,
            "description ": c.p.text,
            "Rate": top10ActionMoviesRates.text

        }
    movies.append(obj)
with open('top10if-rate>5.jsonl', 'w') as f:
    json.dump(movies, f)
# top10ActionMoviesRates=soup.find_all('span',class_='legend')
# for c in top10ActionMoviesRates:
#     print(c.text) #movie rtes
