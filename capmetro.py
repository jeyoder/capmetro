#!/usr/bin/python3

import requests
import pprint

r = requests.get('https://data.texas.gov/download/cuc7-ywmd/text%2Fplain')

d = r.json()

vehs = d['entity']

print('Got data for {} vehicles.'.format(len(vehs)))

veh = vehs[0]

print(veh.keys())

pprint.pprint(veh)
pprint.pprint(vehs[65])
pprint.pprint(vehs[126])
