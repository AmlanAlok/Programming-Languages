import asyncio
import aiohttp
import os
import time
# To work with the .env file
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']
results = []

start = time.time()


def get_tasks(session):
    tasks = []
    for symbol in symbols:
        '''create_task would put the task on the event loop'''
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)

        """ * operator unpacks the elements in tasks list and passes them as individual arguments to gather func """
        responses = await asyncio.gather(*tasks)
        """
        gather will put the tasks on event loop if not already there 
        gather will wait for all the tasks to come back
        """
        for response in responses:
            results.append(await response.json())

asyncio.run(get_symbols())

end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
print('You did it!')
# It took 0.23641705513000488 seconds to make 15 API calls
