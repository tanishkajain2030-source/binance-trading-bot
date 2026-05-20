# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot for Binance Futures Testnet (USDT-M) that supports MARKET and LIMIT order placement with validation, logging, and error handling.


# Features

- Place MARKET orders  
- Place LIMIT orders  
- Supports BUY and SELL operations  
- Command Line Interface (CLI) support  
- Input validation  
- Structured project architecture  
- Logging system for API activity and errors  
- Exception handling for invalid inputs and API failures  


# Tech Stack

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging


# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading.log
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```


# Installation

## 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd trading_bot
```


## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```


## 3. Install Dependencies

```bash
pip install -r requirements.txt
```


# Binance Futures Testnet Setup

1. Create a Binance Futures Testnet account  
2. Generate API credentials  
3. Add credentials inside `.env`

Example:

```env
API_KEY=your_api_key
API_SECRET=your_secret_key
```

Testnet URL used:

```text
https://testnet.binancefuture.com
```


# Usage

## MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```


## LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000
```


# Input Parameters

| Parameter | Description | Example |
|---|---|---|
| `--symbol` | Trading pair | BTCUSDT |
| `--side` | BUY or SELL | BUY |
| `--type` | MARKET or LIMIT | MARKET |
| `--quantity` | Order quantity | 0.001 |
| `--price` | Required for LIMIT orders | 80000 |


# Logging

Logs are automatically stored in:

```text
logs/trading.log
```

Logs include:
- successful orders
- API responses
- validation errors
- exceptions


# Validation & Error Handling

The bot validates:
- order side
- order type
- quantity
- limit price

Handled exceptions include:
- invalid user input
- Binance API errors
- network failures


# Example Output

```text
========== ORDER SUMMARY ==========

Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.001

===================================

Order Placed Successfully

Order ID: 123456
Status: FILLED
Executed Quantity: 0.001
```


# Requirements

Dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```


# Notes

- This project uses Binance Futures Testnet only
- No real funds are used
- Built for educational and evaluation purposes


# Author

Tanishka Jain
