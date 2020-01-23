from os import mkdir, path
from typing import Optional, TextIO

import click
import uvicorn
from xdg import XDG_CONFIG_HOME, XDG_DATA_HOME

from escarpolette import create_app
from escarpolette.settings import Default, Config


DEFAULT_CONFIG_FOLDER = path.join(XDG_CONFIG_HOME, "escarpolette")
DEFAULT_DATA_FOLDER = path.join(XDG_DATA_HOME, "escarpolette")


@click.command()
@click.option(
    "--config", "config_file", help="path to the config file", type=click.File("w+")
)
@click.option(
    "--host",
    default=Default.HOST,
    help="address to bind to listen for connections",
    type=str,
)
@click.option(
    "--port",
    default=Default.PORT,
    help="port to bind to listen for connections",
    type=int,
)
@click.option(
    "--dev",
    default=False,
    help="enable code autoreload and debug logs",
    type=bool,
    is_flag=True,
)
def run(config_file: Optional[TextIO], host: str, port: int, dev: bool) -> None:
    """Run the application.

    Create default folders for config and data and the default config file if
    no one is given, create the fastapi app and start the server.

    TODO: setup loging
    """
    # import pdb
    # pdb.set_trace()
    if not path.exists(DEFAULT_CONFIG_FOLDER):
        mkdir(DEFAULT_CONFIG_FOLDER)

    if not path.exists(DEFAULT_DATA_FOLDER):
        mkdir(DEFAULT_DATA_FOLDER)

    if config_file is None:
        config_file = open(
            path.join(XDG_CONFIG_HOME, "escarpolette", "escarpolette.conf"), "w+"
        )

    config = Config(config_file)
    config_file.close()

    host = host or config.HOST
    port = port or config.PORT
    uvicorn.run("escarpolette.app:app", host=host, port=port, reload=dev)


run()
