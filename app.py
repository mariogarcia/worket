import click
from api import api


@click.group()
def cli():
    pass


@cli.command()
def runapp():
    """startup REST api"""
    app = api.setup_app()
    app.run(host='0.0.0.0', threaded=True)


if __name__ == '__main__':
    cli()
