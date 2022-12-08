"""This module provides the DCS CLI."""
# dcs/cli.py

from typing import Optional
import os

import typer

from dcs import __app_name__, __version__
from dcs.setup._airtable import _Airtable


app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
def setup(value: str = typer.Argument(..., help="Enter a specific API to setup e.g \"Airtable\" or launch the setup GUI with no arguments.")):
    typer.echo(f"{value}")
    from dcs.setup import setup_gui
    setup.create_gui()
    setup_gui.app
    raise typer.Exit()


@app.command()
def airtable():
    typer.echo("setting up airtable")
    # TODO: move api key get to init file
    at_key = os.environ.get('AIRTABLE_API_KEY', 'No Airtable API key found.')
    at = _Airtable(at_key)
    at.create_record()
    raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ) #,
    # setup: str = typer.Option(
    #     "",
    #     "--setup",
    #     "-s",
    #     help="Launch the setup GUI to configure API credentials.",
    #     callback=setup,
    #     is_eager=True,
    # )

) -> None:
    return

# if __name__ == "__main__":
#     app()