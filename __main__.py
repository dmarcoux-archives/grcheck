import json
import os
import requests

# TODO: Get owner and name from STDIN, then use it in json below
owner = "dmarcoux"
name = "grc"
json = {'query': '{ repository(owner: "facebook", name: "graphql") { releases(last: 1) { nodes { tag { name } } } } }'}
# TODO: Error out if GITHUB_OAUTH_TOKEN is not set
headers = {"Authorization": "token %s" % os.environ['GITHUB_OAUTH_TOKEN']}

r = requests.post(url='https://api.github.com/graphql', json=json, headers=headers)
# TODO: Check if there's a node before fetching name, otherwise out of range error
print(r.json()['data']['repository']['releases']['nodes'][0]['tag']['name'])
