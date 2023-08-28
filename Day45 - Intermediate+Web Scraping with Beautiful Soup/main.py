from bs4 import BeautifulSoup
import requests
# with open("./website.html", mode="r", encoding="utf-8") as website:
#     html_doc = website.read()
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     all_p_elements = soup.find(name="h3", class_="heading")

#     print(all_p_elements)

hacker_news_link = "https://news.ycombinator.com/"
response = requests.get(hacker_news_link)
response = response.text

soup = BeautifulSoup(response, "html.parser")
all_titles_tags = soup.find_all(name="span", class_="titleline")
all_scores = soup.find_all(name="span", class_="score")
data = []

print(len(all_titles_tags), len(all_scores))


for index in range(len(all_titles_tags)):
    title = all_titles_tags[index].find("a").getText()
    link = all_titles_tags[index].find("a").get("href")
    
    try:
        score = all_scores[index].getText()
    except IndexError:
        print("an error occured here")
        print(index)
        print(f"{title} \n{link} ---> not available\n\n")
    
    else:
        print(f"{title} \n{link} ---> {score}\n\n")
