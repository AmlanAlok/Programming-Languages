""" asynchio library """

import aiohttp
import asyncio
import os
import time
# To work with the .env file
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
URL = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
SYMBOLS = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']*20
results = []


def get_tasks(session):
    tasks = []
    for symbol in SYMBOLS:
        tasks.append(session.get(URL.format(symbol, API_KEY), ssl=False))
    return tasks


async def run_tasks():
    session = aiohttp.ClientSession()
    tasks = get_tasks(session)  # gives the list of all the func you want to call

    """ * operator unpacks the elements in tasks list and passes them as individual arguments to gather func """
    responses = await asyncio.gather(*tasks)    # puts all the tasks on the event loop together
    for response in responses:
        results.append(await response.json())
    await session.close()

print("Timer started...")
start = time.time()
'''Starts an event loop'''
asyncio.run(run_tasks())

end = time.time()
total_time = end - start
print(f"Time to make {len(SYMBOLS)} API calls with tasks, it took: {total_time}")
# Time to make 5 API calls with tasks, it took: 0.21643900871276855
# Time to make 15 API calls with tasks, it took: 0.32050108909606934
# Time to make 100 API calls with tasks, it took: 0.514369010925293
# Time to make 3000 API calls with tasks, it took: 3.0974957942962646
# Time to make 10000 API calls with tasks, it took: 8.341070175170898
# Time to make 25000 API calls with tasks, it took: 22.327913999557495
