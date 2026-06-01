from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

if not api_key or not api_secret:
    raise EnvironmentError(
        "Missing Binance Futures credentials. Set API_KEY and API_SECRET in .env."
    )

invalid_placeholder = (
    api_key.lower().startswith("your_"),
    api_secret.lower().startswith("your_"),
    "replace" in api_key.lower(),
    "replace" in api_secret.lower(),
)
if any(invalid_placeholder):
    raise EnvironmentError(
        "The API_KEY and API_SECRET in .env look like placeholders. "
        "Replace them with valid Binance Futures Testnet credentials."
    )

client = Client(api_key, api_secret)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

def get_client():
    return client