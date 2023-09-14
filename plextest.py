import requests
from auth import *
from plexapi.server import PlexServer

plex = PlexServer(baseurl, token)
headers = {
    "X-Plex-Token": token
}

# update Movie Library
movies = plex.library.section(movies)
movies.update()

# update TV Show Library
tvshows = plex.library.section(shows)
tvshows.update()

# reload Guide
requests.post(baseurl + "/livetv/dvrs/" + dvrid + "/reloadGuide", headers=headers)

# Reload DVR
reload = requests.get(baseurl + "/livetv/sessions", headers=headers)
print(reload.content)

