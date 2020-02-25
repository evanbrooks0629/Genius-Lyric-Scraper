import requests
from bs4 import BeautifulSoup

# add_song() functionality is currently having trouble fetching the info from the url, and it seems to be retrieving from a loading page

songs = {
    "The Box": "https://genius.com/Roddy-ricch-the-box-lyrics",
    "Hot": "https://genius.com/Young-thug-hot-lyrics",
    "Tuscan Leather": "https://genius.com/Drake-tuscan-leather-lyrics",
    "Down Bad": "https://genius.com/Dreamville-down-bad-lyrics",
    "Life Is Good": "https://genius.com/Future-life-is-good-lyrics",
    "Orange Soda": "https://genius.com/Baby-keem-orange-soda-lyrics",
    "Yummy": "https://genius.com/Justin-bieber-yummy-lyrics",
    "Had Enough": "https://genius.com/Don-toliver-had-enough-lyrics",
    "Futsal Shuffle": "https://genius.com/Lil-uzi-vert-futsal-shuffle-2020-lyrics",
    "Blinding Lights": "https://genius.com/The-weeknd-blinding-lights-lyrics"
}

def menu():
    is_on = True
    while is_on:
        print(
        """
        - Type 'a' to add a song (not working right now)
        - Type 'f' to find a song 
        - Type 'q' to quit 
        """)
        user_choice = input("Type a letter to do an action: ")
        if user_choice == 'a':
            add_song()
        elif user_choice == 'f':
            find_song()
        elif user_choice == 'q':
            is_on = False
        else:
            print("No actions matched your selection.")


def find_song():
    user_song = input("Input the name of the song you want to get the lyrics for: ")
    for song, url in songs.items():
        if song == user_song:
            song_info(url)
            break
    else:
        print("No songs matched your selection.")


def add_song():
    new_url = input("Input the url of the song you want to add from genius.com: ")
    new_title = get_title(new_url)
    songs[new_title] = new_url
    print(songs)


def get_url(url):
    page_content = requests.get(url).text
    page_soup = BeautifulSoup(page_content, 'html.parser')
    return page_soup


def get_lyrics(url):
    song_url = get_url(url)
    l = song_url.find('p')
    lyrics = l.get_text()
    return lyrics
    
    
def get_title(url):
    song_url = get_url(url)
    t = song_url.find('h1')
    title = t.get_text()
    return title

    
def get_artist(url):
    song_url = get_url(url)
    a = song_url.find('h2')
    artist = a.get_text()
    return artist
    

def song_info(url):
    title = get_title(url)
    artist = get_artist(url)
    lyrics = get_lyrics(url)
    title = title.replace('\n', ' ')
    artist = artist.replace('\n', '')
    print(f"\nLyrics to {title} by {artist} \n")
    print(lyrics)

menu()