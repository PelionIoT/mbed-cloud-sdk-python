"""Entrypoint for module i.e. `python -m auto_version`"""
from auto_version.auto_version_tool import main_from_cli

__name__ == '__main__' and main_from_cli()
