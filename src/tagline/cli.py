from pathlib import Path
from typing import Annotated

import typer

from tagline import __version__

app = typer.Typer(add_completion=False)


def version_callback(*, value: bool) -> None:
    if value:
        typer.echo(f"tagline {__version__}")
        raise typer.Exit


@app.command(
    help="Audio tags, at a glance!",
    epilog="For source code, issues, etc., see the [link=https://github.com/junapur/tagline]GitHub[/link]",
    context_settings={"help_option_names": ["-h", "--help"]},
    no_args_is_help=True,
)
def main(
    file: Annotated[
        Path,
        typer.Argument(
            help="The audio file to inspect.",
            exists=True,
            readable=True,
            resolve_path=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
    *,
    version: Annotated[
        bool,
        typer.Option(
            "-v",
            "--version",
            help="Show version information and exit.",
            callback=version_callback,
            is_eager=True,
        ),
    ] = False,
) -> None: ...
