# imports - standard imports
import os
from zipfile import ZipFile

# imports - third party imports
from requests import get


def __extract__(dataset_name):
    # ZIP FILES ONLY!!!
    # fix the next line
    os.rename('{}'.format(dataset_name), '{}.zip'.format(dataset_name))
    down = ZipFile('{}.zip'.format(dataset_name))
    down.extractall()
    down.close()


def __download_file__(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    return local_filename
