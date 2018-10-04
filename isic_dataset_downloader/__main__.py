# imports - standard imports
import argparse
import sys

# imports - module imports
from isic_dataset_downloader.__attr__ import __name__, __description__, __version__

USAGE_INSTR = ("\nIf args are not parsed app will exit"
               "\nThe bare minimum for its usage is as:"
               "\n{} -D -x -s 'DOWNLOAD_PATH'"
               "\nFor further help see --help or -h").format(__name__)


def get_parser():
    parser = argparse.ArgumentParser(
        description=__description__ + USAGE_INSTR

    )
    parser.parse_args()
    parser.add_argument("-D", "--download",
                        action="store_true",
                        help="this option enables downloading"
                        )

    parser.add_argument("-x", "--segregate",
                        action="store_true",
                        help="tell me if you want me to segregate the images after downloading the dataset"
                        )

    parser.add_argument("-s", "--src",
                        action="store_true",
                        help="tell me where you want me to download the dataset to"
                        )

    parser.add_argument("-v", "--version",
                        action="version",
                        version=__version__
                        )

    return parser


if __name__ == "__main__":
    code = 0
    parser = get_parser()
    args, _ = parser.parse_known_args()
    """
    download()
    segregate()
    """
    sys.exit(code)
