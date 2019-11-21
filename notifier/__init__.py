import click

from notifier.render import Renderer
from notifier.slack import post_message


@click.group()
def cli():
    pass


@cli.command()
@click.argument('template')
def post(template):
    rnd = Renderer()
    rnd.use_os_env()
    text = rnd.parse_file(template)
    rv = post_message(text)

    if not rv:
        print('Post message to slack failed.')

