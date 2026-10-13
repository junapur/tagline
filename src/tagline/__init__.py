from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("tagline")
except PackageNotFoundError:
    __version__ = "unknown"
