#!/usr/bin/env python3

import requests

r = requests.get('http://api.open-notify.org/astros.json')

astro= r.json()

print( "People in Space:" + str(astro["number"]))
for x in astro["people"]:
    print(f' {x["name"]} is on the {x["craft"]}')
