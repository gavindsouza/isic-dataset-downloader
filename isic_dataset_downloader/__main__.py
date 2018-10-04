# imports - standard imports
import argparse
import os
import sys

# imports - module imports
from isic_dataset_downloader.__attr__ import __pkgname__, __description__, __version__
from isic_dataset_downloader.data import getDataset
# imports - module imports
from isic_dataset_downloader.data import segregate

USAGE_INSTR = ("\nIf args are not parsed app will exit"
               "\nThe bare minimum for its usage is as:"
               "\n{} -D -x -s 'DOWNLOAD_PATH'"
               "\nFor further help see --help or -h"
               "\n").format(__pkgname__)


if __name__ == "__main__":
    code = 0

    parser = argparse.ArgumentParser(
        description=__description__ + USAGE_INSTR

    )

    parser.add_argument("-D", "--download",
                        action="store_true",
                        default=os.path.dirname(os.path.realpath(__file__)),
                        help="this option enables downloading"
                        )

    parser.add_argument("-x", "--segregate",
                        action="store_true",
                        help="tell me if you want me to segregate the images after downloading the dataset"
                        )

    # this doesn't work, find out why
    parser.add_argument("-s", "--src",
                        action="store_true",
                        help="tell me where you want me to download the dataset to"
                        )

    parser.add_argument("-v", "--version",
                        action="version",
                        version=__version__
                        )
    args = parser.parse_args()

    if args.download:
        getDataset()

    if args.segregate:
        segregate()

    sys.exit(code)
