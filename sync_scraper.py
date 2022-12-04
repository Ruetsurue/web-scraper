import os.path
from common.performance import measure_performance
from common.option_parser import add_parser
from sync_lib.file_io import load_urls_from_file, write_output
from sync_lib.http_io import gather_htmls, parse_htmls

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


@measure_performance
def main():
    args = add_parser()
    input_file = args.input
    output_file = args.output
    urls = load_urls_from_file(dirname=PROJECT_ROOT, filename=input_file)
    content = gather_htmls(urls=urls)
    parsed_content = parse_htmls(unparsed_htmls=content)
    write_output(datas=parsed_content, dirname=PROJECT_ROOT, filename=output_file)


if __name__ == "__main__":
    main()
