from pathlib import Path

from jinja2 import Environment, FileSystemLoader

"""
Telegram bug:
    - you cannot use underscore in markdown
    - strange markdown syntax
"""


current_dir = Path(__file__).parent.parent
environment = Environment(loader=FileSystemLoader(current_dir))
welcome_message = environment.get_template("templates/welcome.jinja")
