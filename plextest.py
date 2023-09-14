import requests
from auth import *
from plexapi.server import PlexServer

plex = PlexServer(baseurl, token)
headers = {
    "X-Plex-Token": token
}

# movies = plex.library.section('Filme')
# number = 0
# for video in movies.search(unwatched=True):
#     print(video.title)
#     number += 1
# print("Number of unwatched movies:", number)

# Make a GET request to the Recording Priority endpoint
# response = requests.get(baseurl + "/media/subscriptions", headers=headers)

# response = requests.post(baseurl + "/livetv/dvrs/" + dvrid + "/reloadGuide", headers=headers)

# Print the response from the API
# print(response.content)

response2 = requests.get(baseurl + "/livetv/sessions", headers=headers)
print(response2.content)

# curl -X POST "https:/" + baseurl + "/livetv/dvrs/<dvrID>/reloadGuide?X-Plex-Token=<api token>"