import click
import json
import urllib.parse
import requests
from requests.auth import HTTPBasicAuth

registries = [
    'https://registry.defenselayers.com/',
    'https://registry.defenselayers.dev/'
]

registry_postfix = '/v2/_catalog'


@click.command()
@click.option('-u', '--user', metavar="USERNAME", prompt=True, envvar='SHMANIFEST_USER', help='sets username.')
@click.option('-p', '--passwd', metavar="PASSWD", prompt=True, hide_input=True,
              envvar='SHMANIFEST_PASSWD', help='sets user password.')
@click.option('-v', '--verbose', is_flag=True, default=False, help='enables verbose output.')
@click.option('-r', '--registry', metavar="REGISTRYURL", multiple=True, help='adds additional registry to query.')
@click.version_option("1.0")
def cli(user, passwd, verbose, registry):
    """
    Defenselayers secure harbour manifest tool (container registry utility).
    """
    click.secho(' Defenselayers secure harbour manifest (c) Defenselayers Sp. z o.o. 2020', fg='cyan')
    click.secho(' https://defenselayers.com', fg='yellow')
    click.echo('')

    if registry:
        registries.clear()
        for r in registry:
            registries.append(r)

    for reg in registries:
        click.secho('=> Registry:', fg='blue')
        click.secho('{}'.format(reg), fg='yellow')
        registry_catalog_url = urllib.parse.urljoin(reg, registry_postfix)
        try:
            r = requests.get(registry_catalog_url, auth=HTTPBasicAuth(user, passwd))
            if r.status_code == 200:
                json_data = json.loads(r.text)
                image_list = json_data['repositories']
                if verbose:
                    click.secho(' Found {} images:'.format(len(image_list)), fg='green')
                for img in image_list:
                    click.secho('  * {}'.format(img), fg='green')
            else:
                click.secho(' ERROR: wrong response from registry or incorrect username/password (', nl=False,
                            fg='red')
                click.secho('{}'.format(r.status_code), nl=False, fg='white')
                click.secho(').', fg='red')
        except requests.exceptions.ConnectionError:
            click.secho(' ERROR: Failed to connect to registry.', fg='red')
