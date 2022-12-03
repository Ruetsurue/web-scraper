import os.path
from common.performance import measure_performance
from sync_lib.file_io import load_urls_from_file, write_output
from sync_lib.http_io import gather_htmls, parse_htmls

INPUT_FILE = 'urls.txt'
OUTPUT_FILE = 'found_urls.txt'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


@measure_performance
def main():
    urls = load_urls_from_file(dirname=PROJECT_ROOT, filename=INPUT_FILE)
    content = gather_htmls(urls=urls)
    parsed_content = parse_htmls(unparsed_htmls=content)
    write_output(datas=parsed_content, dirname=PROJECT_ROOT, filename=OUTPUT_FILE)


if __name__ == "__main__":
    main()
