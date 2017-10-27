import json
import os
import requests

auth_token = os.getenv('GITHUB_OAUTH_TOKEN')
if auth_token is None:
    raise ValueError('Set environment variable GITHUB_OAUTH_TOKEN')

headers = {"Authorization": "token %s" % auth_token}

# TODO: Get owner and name from STDIN, then use it in json below
owner = "dmarcoux"
name = "grc"
json = {'query': '{ repository(owner: "%s", name: "%s") { releases(last: 1) { nodes { tag { name } } } } }' % (owner, name)}

r = requests.post(url='https://api.github.com/graphql', json=json, headers=headers)
# TODO: Check if there's a node before fetching name, otherwise out of range error
print(r.json()['data']['repository']['releases']['nodes'][0]['tag']['name'])
