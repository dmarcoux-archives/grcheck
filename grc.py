import os
import click
import requests

def validate_token(ctx, param, value):
    if value is None:
        raise click.BadParameter('Pass a GitHub OAuth token with "%s" or set the environment variable %s' % ('" / "'.join(param.opts), param.envvar))

def validate_repository(ctx, param, value):
    try:
        owner, name = value.split('/')
        return (owner, name)
    except ValueError:
        raise click.BadParameter('"%s" must be in format owner/name (https://github.com/%s)' % (param.name, click.style('dmarcoux/grc', bold=True)))

@click.command()
@click.option('-t', '--token', envvar='GITHUB_OAUTH_TOKEN', callback=validate_token)
@click.argument('repository', callback=validate_repository)
def cli(token, repository):
    headers = {"Authorization": "token %s" % token}

    query = {'query': '{ repository(owner: "%s", name: "%s") { releases(last: 1) { nodes { tag { name } } } } }' % repository}

    r = requests.post(url='https://api.github.com/graphql', json=query, headers=headers)
    # TODO: Check if there's a node before fetching name, otherwise out of range error
    click.echo(r.json()['data']['repository']['releases']['nodes'][0]['tag']['name'])
