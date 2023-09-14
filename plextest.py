import requests
from auth import *
from plexapi.server import PlexServer

plex = PlexServer(baseurl, token)
headers = {
    "X-Plex-Token": token
}

# update Movie Library
def addmovies():
    movies = plex.library.section(movielibrary)
    movies.update()

# update TV Show Library
def addshows():
    tvshows = plex.library.section(showlibrary)
    tvshows.update()

# reload Guide
def reloadguide():
    requests.post(baseurl + "/livetv/dvrs/" + dvrid + "/reloadGuide", headers=headers)

# Reload DVR
# reload = requests.get(baseurl + "/livetv/sessions", headers=headers)
# print(reload.content)

# show 5 latest movies
def lastmovies():
    movies = plex.library.section(movielibrary)
    movielist = movies.recentlyAdded()
    movielist = movielist[:5]
    for movie in movielist:
        print(movie.title)


def main():
    lastmovies()

if __name__ == "__main__":
    main()