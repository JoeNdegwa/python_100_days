from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movie_name = []

for movie in movies:
    movie_title = movie.getText()
    movie_name.append(movie_title)

# Order the list in reverse
ordered_movies = movie_name[::-1]

with open("movies.txt", mode="w") as file:
    for item in ordered_movies:
        file.write(f"{item}\n")
