# Binance Futures Testnet Trading Bot

## Description
This is a simple Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- MARKET orders
- LIMIT orders
- BUY and SELL support
- Error handling
- Logging

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

## Run

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

## Files

- `client.py` - Binance connection
- `orders.py` - Order functions
- `main.py` - CLI application
- `requirements.txt` - Dependencies
- `README.md` - Documentation