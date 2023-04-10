
#!/usr/bin/env python3

import requests, yaml, sys
import json
from requests.packages import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://spotify23.p.rapidapi.com/search/"

querystring = {"q":"<REQUIRED>","type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}

headers = {
	"X-RapidAPI-Key": "<KEY>",
	"X-RapidAPI-Host": "<HOST>"
}

response = requests.request("GET", url, headers=headers, params=querystring)
music = response.json()
#print(json_res['albums'])

#for key in json_res.items() :
 #   print (f'KEY** ', key)


music_keys = music.keys() #prints keys
#music_values = music.values() #prints values
#print(music_keys)
#print (json.dumps(music, indent=2, default=str))

Festival_Arists = ['Emery', 'Laura Dreyfuss', 'Papy Jeico', 'INTERWORLD', 'Dahako']

# Make a dict of all Artists matched to URI

# Find URIs for Artist Name

# For artists in Featured Artists, print Album names and Genres
