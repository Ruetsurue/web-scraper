from typing import Optional

import bs4
import requests


def gather_htmls(urls: list[str]) -> list[tuple[str, Optional[dict]]]:
    unparsed_htmls = []
    with requests.Session() as session:
        for url in urls:
            response = session.get(url=url)

            if response.status_code == 404:
                message = f"{url} returned {response.status_code}"
                print(message)
                unparsed_htmls.append((url, None))
                continue

            content = response.text
            unparsed_htmls.append((url, content))
    return unparsed_htmls


def parse_htmls(unparsed_htmls: list[tuple[str, Optional[dict]]]):
    result = []
    for unparsed in unparsed_htmls:
        url, content = unparsed
        if content is None:
            result.append((url, None))
            continue

        soup = bs4.BeautifulSoup(content, 'html.parser')
        anchors = soup.find_all('a', href=True)
        hrefs = [anchor.get('href') for anchor in anchors if anchor.get('href').find('http') != -1]
        result.append((url, hrefs))
    return result
