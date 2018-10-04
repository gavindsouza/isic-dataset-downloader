# imports - standard imports
import os
import sys
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
    # first simple downloader
    """
    r = get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    """

    # downloader with loading bar
    with open(local_filename, "wb") as f:
        print("Downloading %s" % local_filename)
        response = get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()

    return local_filename
