# imports - standard imports
import sys

# imports - module imports
from isic_dataset_downloader.data import data_handler as main

if __name__ == "__main__":
    code = main()
    sys.exit(code)
