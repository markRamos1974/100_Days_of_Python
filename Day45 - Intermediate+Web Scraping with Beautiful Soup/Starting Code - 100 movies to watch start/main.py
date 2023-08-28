import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


def create_list(movie_titles):
    with open("movies.txt", mode="a", encoding="utf-8") as movie_bucket_list:

        for movie_index in range(len(movie_titles)):
            title = movie_titles[movie_index].getText()
            movie_bucket_list.write(f"{title}\n")

print("Sending request...")
response = requests.get(url=URL)
print("Response recieve")
response = response.text


soup = BeautifulSoup(response, "html.parser")
print("finding all titles...")
movie_titles = soup.find_all(name="h3", class_="title")
movie_titles.reverse()
create_list(movie_titles)
print("code finised...")
