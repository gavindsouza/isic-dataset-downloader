# imports - module imports
from isic_dataset_downloader.data.download import __download_file__, __extract__
from isic_dataset_downloader.data.segregate import segregate

img_file_links = {
    "train": {
        "images": r"https://challenge.kitware.com/api/v1/item/5ac20fc456357d4ff856e139/download",
        "truth-table": r"https://challenge.kitware.com/api/v1/item/5ac20eeb56357d4ff856e136/download"
    },
    "test": r"https://challenge.kitware.com/api/v1/item/5b1c200656357d41064da305/download",
    "validate": r"https://challenge.kitware.com/api/v1/item/5b1c1c7256357d41064da302/download"
}


def getDataset():
    for dataset in img_file_links.keys():
        if dataset is "train":
            print("Downloading {}".format(dataset))
            for train in img_file_links[dataset]:
                print("Downloading {}".format(train))
                __download_file__(img_file_links[dataset][train])
                __extract__(img_file_links[dataset][train])
        else:
            print("Downloading {}".format(dataset))
            __download_file__(img_file_links[dataset])
            __extract__(img_file_links[dataset])
