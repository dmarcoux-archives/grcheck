import click
import requests


def validate_token(ctx, param, value):
    if value is None:
        raise click.BadParameter('Pass a GitHub OAuth token with "%s" or set the environment variable %s'
                                 % ('" / "'.join(param.opts), param.envvar))
    return value


def validate_repository(ctx, param, value):
    try:
        owner, name = value.split('/')

        r = requests.get('https://github.com/%s' % value)
        r.raise_for_status()

        return (owner, name)
    except ValueError:
        raise click.BadParameter('"%s" must be in format owner/name (example: https://github.com/%s)'
                                 % (param.name, click.style('dmarcoux/grcheck', bold=True)))
    except requests.exceptions.HTTPError as error:
        if r.status_code == 404:
            raise click.BadParameter('"https://github.com/%s" is not a repository' % value)
        else:
            raise click.ClickException(error)


@click.command()
@click.option('-t', '--token', envvar='GITHUB_OAUTH_TOKEN', callback=validate_token)
@click.argument('repository', callback=validate_repository)
def cli(token, repository):
    headers = {"Authorization": "token %s" % token}

    query = {'query': '{ repository(owner: "%s", name: "%s") { releases(last: 1) { nodes { tag { name } } } } }'
             % repository}

    r = requests.post(url='https://api.github.com/graphql', json=query, headers=headers)

    nodes = r.json()['data']['repository']['releases']['nodes']
    if nodes:
        click.echo(nodes[0]['tag']['name'])
    else:
        click.echo('No release found')
