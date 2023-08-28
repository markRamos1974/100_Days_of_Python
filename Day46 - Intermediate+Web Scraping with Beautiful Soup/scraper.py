from bs4 import BeautifulSoup
import requests
 
class Scraper(BeautifulSoup):

    def __init__(self, date):
     
        self.url = f"https://www.billboard.com/charts/hot-100/{date}/"
        self.response = requests.get(self.url)
        self.response = self.response.text

        super().__init__(self.response, "html.parser")
        self.title_tag_list = self.find_all(name="h3", class_="a-font-primary-bold-s", id="title-of-a-story")
        self.titles = [item.string.strip() for item in self.title_tag_list[2::]]

    def get_all_titles(self):
        return self.titles
 