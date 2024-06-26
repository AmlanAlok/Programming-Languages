import requests
import os
import time
# To work with the .env file
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']*1
results = []


def run_tasks():
    for symbol in symbols:
        response = requests.get(url.format(symbol, api_key))
        response_dict = response.json()
        results.append(response_dict)


print("Timer started...")
start = time.time()
run_tasks()
end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
# Took 11 sec in the first run
