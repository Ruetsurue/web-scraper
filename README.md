# web-scraper
## Simple web-scraper done in both classic and async manner

Crawls over the given list of web pages and extracts any hrefs found. Href must contain '**http**' in order to pass the filter.

---
For async run:
> python async_scraper.py --input <%INPUT_FILE%> --output <%OUTPUT_FILE%>
---
For sync version:
> python sync_scraper.py --input <%INPUT_FILE%> --output <%OUTPUT_FILE%>
---
## Input (default='urls.txt'):
> Place urls to scrape into urls.txt, one per line, e.g.:
* https://www.nytimes.com/guides/
* https://www.mediamatters.org/
* https://1.1.1.1/
* https://www.politico.com/tipsheets/morning-money
 
## Output (default="found_urls.txt"):
> Output report will be available in found_urls.txt