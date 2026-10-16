from typing import Final

from rich.console import Console
from rich.theme import Theme

TL_THEME: Final = Theme(
    {
        "cyclopts.border": "none",
        "cyclopts.usage": "bold",
        "cyclopts.name": "cyan",
        "cyclopts.required": "red",
        "cyclopts.required_marker": "red bold",
        "cyclopts.default": "grey62",
        "cyclopts.choices": "grey62",
        "cyclopts.env_var": "grey62",
    }
)

out_console: Final = Console(theme=TL_THEME)
err_console: Final = Console(stderr=True, theme=TL_THEME)
