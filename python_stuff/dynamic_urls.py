"""
Retrieve valid (Accessible) URLs from Google search engine, based on arbitrary generated keywords.
"""

__author__ = 'Shay Elmualem'

import aiohttp
import asyncio
import re


class DynamicUrls:
    def __init__(self, max_urls_per_keyword=2, max_urls_total=4):
        self.max_urls_per_keyword = max_urls_per_keyword
        self.max_urls_total = max_urls_total

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

    async def return_google_htmls(self):
        """
        S
        """
        async with aiohttp.ClientSession(headers={'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; '
                                                                 'rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}) as \
                session:
            tasks = [asyncio.ensure_future(self.fetch_url(session, f'https://www.google.com/search?q={kw}'))
                     for kw in await self.return_kws()]
            return await asyncio.gather(*tasks)

    async def extract_href(self):
        goorex = re.compile(r'(><h3 class=\"r\"><a\s(dir=\"ltr\"\s)?(href=\"\/url\?q=)(.*){1}\">)')
        print(type(goorex))

durls = DynamicUrls()
base_loop = asyncio.get_event_loop()
future = asyncio.ensure_future(durls.return_google_htmls())
print(base_loop.run_until_complete(future))



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
