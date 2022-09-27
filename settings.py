import json

configfile = open('files/config.json')
config = json.load(configfile)
token = config['token']
prefix = config['prefix']