import asyncio
import logging
from typing import Optional
from aiohttp import ClientSession, ClientResponseError
from bs4 import BeautifulSoup


async def fetch_url(url: str, session: ClientSession):
    try:
        async with session.get(url) as response:
            page_content = await response.text()
            return url, page_content

    except ClientResponseError as e:
        logging.error(f"{url} returned: '{e.status}: {e.message}'")
        return url, None


async def gather_fetched_html(urls: list[str]):
    tasks = []
    async with ClientSession(raise_for_status=True) as session:
        for url in urls:
            task = asyncio.create_task(fetch_url(url=url, session=session))
            tasks.append(task)

        fetched_html: tuple[str, dict] = await asyncio.gather(*tasks)
        return fetched_html


async def parse_html(url, unparsed_html) -> tuple[str, list]:
    try:
        soup = BeautifulSoup(unparsed_html, "html.parser")
        anchors = soup.find_all('a', href=True)
        hrefs = [element.get('href') for element in anchors if element.get('href').find('http') != -1]
        return url, hrefs

    except TypeError as e:
        logging.error(f'Exception while parsing {url} : {e.args}')
        return url, None


async def gather_parse_tasks(unparsed_htmls: list[tuple[str, Optional[dict]]]):
    tasks = [asyncio.create_task(parse_html(*document)) for document in unparsed_htmls if document]
    return await asyncio.gather(*tasks)
