from typing import Annotated

from cyclopts import App
from cyclopts.types import Parameter, ResolvedExistingFile

from tagline.output import err_console, out_console

app = App(
    name="tagline",
    help="Audio tags, at a glance!",
    help_epilogue="For source code, issues, etc., see the [GitHub](https://github.com/junapur/tagline)",
    help_flags=["--help", "-h"],
    version_flags=["--version", "-v"],
    console=out_console,
    error_console=err_console,
)


@app.default()
def main(
    *files: Annotated[
        ResolvedExistingFile,
        Parameter(
            help="The audio files to inspect.",
            required=True,
        ),
    ],
) -> None:
    pass
