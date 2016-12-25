import sys
import requests
from requests.exceptions import HTTPError 


APP_AUTH_URL = "https://home.nest.com/login/oauth2?client_id=808bba92-90fd-4ff0-a0b8-76ebff67aa95&state=STATE"
ACCESS_TOKEN_URL = "https://api.home.nest.com/oauth2/access_token"

auth_code = input('Visit: ' + APP_AUTH_URL + ' to authenticate this app and copy the code in here: ')
payload = {
  'client_id': "808bba92-90fd-4ff0-a0b8-76ebff67aa95",
  'client_secret': "<CLIENT_SECRET>",
  'code': auth_code,
  'grant_type': 'authorization_code'
}

body = None
try:
  raw = requests.post(ACCESS_TOKEN_URL, data=payload)
  raw.raise_for_status()
  body = raw.json()
except (HTTPError):
  sys.exit('Oops! Somethings not right')

with open('./auth_token.txt', 'w') as config:
  config.write(body['access_token'])

print('Saved authentication token to auth_token.txt')
print(body['access_token'])