"""
Retrieve valid (Accessible) URLs from Google search engine, based on arbitrary generated keywords.
"""

__author__ = 'Shay Elmualem'

import aiohttp
import asyncio
import re
<<<<<<< HEAD


class DynamicUrls:
    def __init__(self, max_urls_per_keyword=2, max_urls_total=4):
=======


def extract_href(html):
    """
    Grab the relevant a hrefs.
    """
    goorex = re.compile(r'(<h3 class=\"r\"><a dir=\"ltr\" href=\")(.*?)(\">)')  # this may not cover all use cases,
    # depending on the requester, but it's good enough for current need
    regsponse = re.findall(goorex, html)
    return [i[1] for i in regsponse]


class DynamicUrls:
    def __init__(self, max_urls_per_keyword=2, max_urls_total=10):
>>>>>>> 0db2aa690515b1a17af720780666cc67e5540c18
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
        Return raw HTMLs from google
        """
        async with aiohttp.ClientSession(headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; '
                                                                'rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}) as \
                session:
            tasks = [asyncio.ensure_future(self.fetch_url(session, f'https://www.google.com/search?q={kw}'))
                     for kw in await self.return_kws()]
            return await asyncio.gather(*tasks)

<<<<<<< HEAD
    async def extract_href(self):
        goorex = re.compile(r'(><h3 class=\"r\"><a\s(dir=\"ltr\"\s)?(href=\"\/url\?q=)(.*){1}\">)')
        print(type(goorex))

durls = DynamicUrls()
base_loop = asyncio.get_event_loop()
future = asyncio.ensure_future(durls.return_google_htmls())
print(base_loop.run_until_complete(future))
=======

def main() -> set:
    durls = DynamicUrls()
    base_loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(durls.return_google_htmls())
    resp = base_loop.run_until_complete(future)
    unique_urls = [re.match('\/url\?q=([http|https]{4,5}://.*?/)', i)[1]
                   for html in resp for i in extract_href(html)]
    return set(unique_urls)
>>>>>>> 0db2aa690515b1a17af720780666cc67e5540c18


if __name__ == '__main__':
    print(main())

"""
Return example: 
{'https://www.wordaz.com/', 'https://www.collinsdictionary.com/', 
'http://www.thewhitegoddess.co.uk/', 'https://academic.oup.com/', 'http://ian.umces.edu/', 
'https://de.wikipedia.org/', 'https://journeyingtothegoddess.wordpress.com/', 'http://sph.unc.edu/', 
'https://www.merriam-webster.com/', 'https://en.wiktionary.org/', 'https://www.discogs.com/', 
'http://tellspell.com/', 'http://www.yourdictionary.com/', 'https://www.youtube.com/', 'https://www.ancestry.com/', 
'https://www.facebook.com/', 'https://theodora.com/', 'https://www.ncbi.nlm.nih.gov/', 
'http://www.thefreedictionary.com/', 'https://peekaboomoments.com/', 'https://www.peekaboo.co/', 
'http://scholar.google.com/', 'https://eng.ichacha.net/', 'http://www.morfix.co.il/', 'http://www.ijunoon.com/', 
'http://www.dictionary.com/', 'https://www.poetrysoup.com/', 'https://www.britannica.com/', 
'http://aldnoahzero.wikia.com/', 'https://www.wikitree.com/', 'https://en.wikipedia.org/'}
"""