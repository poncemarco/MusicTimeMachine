from bs4 import BeautifulSoup
import requests




class SongNames():

    def __init__(self, date):
        url = f"https://www.billboard.com/charts/hot-100/{date}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.web_page = soup
        self.song_names_html = self.web_page.find_all("h3", id='title-of-a-story', class_='a-no-trucate')
        self.names = [song.getText().strip() for song in self.song_names_html]
