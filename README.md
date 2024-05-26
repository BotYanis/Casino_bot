# Telegram Casino Bot

Telegram Casino Bot is a Python-based application that uses the aiogram, sqlite3, pyqiwip2p, glQiwiApi, requests, and coinbase libraries to implement a casino-style game on Telegram. It provides a fun and engaging way for users to play games and win prizes, all within the Telegram messaging platform. The bot also includes an admin panel for managing user accounts and game settings.

## Features

- Play a variety of casino-style games, including slots, roulette, and more
- Track user balances and allow for deposits and withdrawals using Telegram payments and QIWI P2P payments
- Customizable game settings, including payouts and bet limits
- Admin panel for managing user accounts and game settings
- Integration with Coinbase API for cryptocurrency transactions

## Requirements

- Python 3.7 or higher
- aiogram 2.14.2 or higher
- sqlite3
- pyqiwip2p 0.3.3 or higher
- glQiwiApi 1.0.1 or higher
- requests
- coinbase 2.2.0 or higher

## Installation

To install Telegram Casino Bot, clone this repository and install the required dependencies using pip:

```
git clone https://github.com/BotYanis/telegram-casino-bot.git
cd telegram-casino-bot
pip install -r requirements.txt
```

## Usage

To use Telegram Casino Bot, you will need to set up a Telegram bot using the BotFather, and obtain API keys for QIWI P2P, glQiwiApi, and Coinbase. Once you have these keys, create a configuration file called `config.ini` in the project directory and add change values.

To run the bot, simply run the `bot.py` file:

```
python bot.py
```

To access the admin panel, visit the `admin` in profile. You will need to authenticate with a username and password defined in the `config.ini` file.
