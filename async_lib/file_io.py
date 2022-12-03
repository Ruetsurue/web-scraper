import os.path
from aiofile import async_open


async def get_file_path(filedir, filename):
    return os.path.join(filedir, filename)


async def make_url_list(filedir, urlfile) -> list[str]:
    filepath = await get_file_path(filedir=filedir, filename=urlfile)

    async with async_open(file_specifier=filepath, mode='r') as file:
        file_content: str = await file.read()

    return file_content.splitlines()


async def export_hrefs_to_file(data, filedir, output_file):
    filepath = await get_file_path(filedir=filedir, filename=output_file)

    async with async_open(file_specifier=filepath, mode='w') as file:
        for url, hrefs in data:
            header = f"{'-' * 20}" \
                     f" hrefs found in {url} " \
                     f"{'-' * 20}\n"
            footer = "\n\n\n"

            await file.write(data=header)

            output = ''
            if not hrefs:
                output += "None found\n"
            else:
                for href in hrefs:
                    output += f"{href}\n"

            await file.write(data=output)
            await file.write(data=footer)
