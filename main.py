import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from song_names import SongNames
import os



date = input("Type your date of interest using the following format = YYYY-MM-DD \n")
songs = SongNames(date)
# print(songs.song_names)
#
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt"
    )
)
user = sp.current_user()["id"]

songs_uris = []
year = date.split("-")[0]
for names in songs.names:
    result = sp.search(q=f"track:{names} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{names} doesn't exist in Spotify")

playlist = sp.user_playlist_create(user=user, name=f"Top 100 music of {date}", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)
