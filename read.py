import time
import json
import logging
import requests

def setup_logger():
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  console.setFormatter(formatter)
  logger = logging.getLogger('BIRDS-EYE-VIEW')
  logger.setLevel(logging.INFO)
  logger.addHandler(console)

  return logger


logger = setup_logger()
headers = { 'Content-Type': 'application/json' }

access_token = None
with open('./auth_token.txt', 'r') as token:
  access_token = token.read()

while True:
  response = requests.get('https://developer-api.nest.com?auth='+access_token, headers=headers).json()

  thermostatsById = response['devices']['thermostats']
  thermostats = [ thermostatsById[t] for t in thermostatsById ]

  for thermostat in thermostats:
    logger.info(thermostat['name'] + ' - ' + 'ambient_degrees_c: ' + str(thermostat['ambient_temperature_c']))

  time.sleep(2)
