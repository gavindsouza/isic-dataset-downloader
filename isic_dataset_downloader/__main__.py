# imports - standard imports
import sys

# imports - module imports
from isic_dataset_downloader.data import data_handler as download
from isic_dataset_downloader.data import segregate

if __name__ == "__main__":
    code = 0
    download()
    segregate()
    sys.exit(code)
