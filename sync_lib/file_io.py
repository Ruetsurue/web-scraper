import os.path


def join_paths(dirname, filename):
    return os.path.join(dirname, filename)


def load_urls_from_file(dirname, filename):
    filepath = join_paths(dirname=dirname, filename=filename)
    with open(file=filepath, mode='r') as file:
        file_content = file.read()
        return file_content.splitlines()


def write_output(datas, dirname, filename):
    filepath = join_paths(dirname, filename)
    with open(file=filepath, mode='w') as file:

        for data in datas:
            url, hrefs = data
            header = f"{'-' * 20}" \
                     f" hrefs found in {url} " \
                     f"{'-' * 20}\n"
            footer = "\n\n\n"

            file.write(header)

            output = ''
            if not hrefs:
                output += "None found"
            else:
                for href in hrefs:
                    output += f'{href}\n'

            file.write(output)
            file.write(footer)
