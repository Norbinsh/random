"""
Retrieve valid (Accessible) URLs from popular search engines, based on arbitrary (or user provided) keywords.
"""

__author__ = 'Shay Elmualem'

import aiohttp
import asyncio
from bs4 import BeautifulSoup


class DynamicUrls:
    def __init__(self, search_engine='google', max_urls_per_keyword=2, max_urls_total=4, keywords_source='ai'):
        self.search_engine = search_engine
        self.max_urls_per_keyword = max_urls_per_keyword
        self.max_urls_total = max_urls_total
        self.keywords_source = keywords_source

    @staticmethod
    async def fetch_url(session, url: str) -> object:
        """
        Fetch a resource over HTTP(S) and return the textual response
        """
        async with session.get(url) as response:
            return await response.text()

    async def return_kws(self):
        """
        Creates a single session that will be used for all of the requests, then return all responses at once using
        asyncio.gather
        """
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.ensure_future(self.fetch_url(session, 'http://setgetgo.com/randomword/get.php')) for _ in
                     range(self.max_urls_total // self.max_urls_per_keyword)]
            return await asyncio.gather(*tasks)

    async def return_raw_htmls(self):
        """
        S
        """
        async with aiohttp.ClientSession(headers={'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; '
                                                                 'rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}) as \
                session:
            tasks = [asyncio.ensure_future(self.fetch_url(session, f'https://www.google.com/search?q={kw}'))
                     for kw in await self.return_kws()]
            return await asyncio.gather(*tasks)

    # async def

durls = DynamicUrls()
base_loop = asyncio.get_event_loop()
future = asyncio.ensure_future(durls.return_urls())
base_loop.run_until_complete(future)



# REMINDER[shay.elmualem] google paging goes by start=0, start=10, start=20 and so on

# search_engine = 'https://www.google.com/search?q='
#
# r = requests.get(search_engine+'asdkjlaskdklasjdjkalsdkljklljk')
#
# html = r.text
#
# soup = BeautifulSoup(html, 'html.parser')
#
# divs = soup.findAll('h3', 'r')
#
# print(len(divs))
