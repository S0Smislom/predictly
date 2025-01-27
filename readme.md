# Telegram Prediction Bot

A Telegram bot for making predictions, built with Python using `aiogram` for bot development and `Django` for backend management.

## Installation and Usage

With docker installed, run the following:

```
    $ git clone git@github.com:S0Smislom/predictly.git
    $ cd predictly
    $ docker compose up
```

To run migrations:
```
    $ docker exec -it predictly-server /bin/bash
    $ python manage.py migrate
```
