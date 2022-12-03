import asyncio
import os.path
from async_lib.file_io import make_url_list, export_hrefs_to_file
from async_lib.http_io import gather_fetched_html, gather_parse_tasks
from common.performance import measure_performance

INPUT_FILE = "urls.txt"
OUTPUT_FILE = "found_urls.txt"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


async def main():
    make_urls_task = asyncio.create_task(make_url_list(filedir=PROJECT_ROOT, urlfile=INPUT_FILE))
    urls = await make_urls_task
    unparsed_htmls = await gather_fetched_html(urls=urls)
    scraped_hrefs = await gather_parse_tasks(unparsed_htmls=unparsed_htmls)
    await export_hrefs_to_file(data=scraped_hrefs, filedir=PROJECT_ROOT, output_file=OUTPUT_FILE)


@measure_performance
def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
