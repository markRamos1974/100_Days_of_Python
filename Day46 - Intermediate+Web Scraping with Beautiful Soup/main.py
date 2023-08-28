from scraper import Scraper
from spotify_manager import SpotifyManager

date = input("Which year do you want to travel to? (YYYY-MM-DD): ")
scraper = Scraper(date)
titles = scraper.get_all_titles()
spotify_manager = SpotifyManager()
playlist_id = spotify_manager.create_playlist(playlist_name=f"{date} Billboard 100")
spotify_manager.add_to_playlist(playlist_id, titles)

print("playlist created successfully...")
