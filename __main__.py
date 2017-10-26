import json
import os
import requests

# TODO: Get owner and name from STDIN, then use it in json below
owner = "dmarcoux"
name = "grc"
# TODO: Check if nodes { name } is really want we need
json = {'query': '{ repository(owner: "facebook", name: "graphql") { releases(last: 1) { nodes { name } } } }'}
# TODO: Error out if GITHUB_OAUTH_TOKEN is not set
headers = {"Authorization": "token %s" % os.environ['GITHUB_OAUTH_TOKEN']}

r = requests.post(url='https://api.github.com/graphql', json=json, headers=headers)
# TODO: Check if there's a node before fetching name, otherwise out of range error
print(r.json()['data']['repository']['releases']['nodes'][0]['name'])
