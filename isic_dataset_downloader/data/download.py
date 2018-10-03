# imports - standard imports
import os
from zipfile import ZipFile

# imports - third party imports
from requests import get

img_file_links = {
    "train": {
        "images": r"https://challenge.kitware.com/api/v1/item/5ac20fc456357d4ff856e139/download",
        "truth-table": r"https://challenge.kitware.com/api/v1/item/5ac20eeb56357d4ff856e136/download"
    },
    "test": r"https://challenge.kitware.com/api/v1/item/5b1c200656357d41064da305/download",
    "validate": r"https://challenge.kitware.com/api/v1/item/5b1c1c7256357d41064da302/download"
}


# main function that does basically everything in this sub-module
def data_handler():
    for stage, links in img_file_links.items():
        if stage is "train":
            # do something
            pass
        elif stage is "test":
            # do something
            pass
        elif stage is "validate":
            # do something
            pass


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
