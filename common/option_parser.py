from argparse import ArgumentParser

INPUT_FILE = 'urls.txt'
OUTPUT_FILE = 'found_urls.txt'


def add_parser():
    parser = ArgumentParser()
    parser.add_argument("--input",
                        action="store",
                        default=INPUT_FILE,
                        help="File containing urls to scrape")

    parser.add_argument("--output",
                        action="store",
                        default=OUTPUT_FILE,
                        help="File holding the resulting report")

    return parser.parse_args()
