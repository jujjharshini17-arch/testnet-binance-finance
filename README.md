# Binance Futures Testnet Trading Bot

## Description
This is a simple Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet. The bot allows users to place BUY and SELL orders through the command line and handles API responses, errors, and logging.

## Features
- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL operations
- Error handling with try/except
- Logging of order activity

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run the Application

```bash
python main.py
```

## Example

```text
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.01
```

## Project Structure

- `client.py` - Binance API connection and configuration
- `orders.py` - Functions for placing MARKET and LIMIT orders
- `main.py` - Command-line interface (CLI)
- `requirements.txt` - Project dependencies
- `README.md` - Project documentation

## Assumptions

- User has a Binance Futures Testnet account.
- Valid Testnet API credentials are available.
- Orders are placed on Binance USDT-M Futures Testnet.
