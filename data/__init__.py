import json

from data.cityscapes_loader import cityscapesLoader
from data.voc_dataset import VOCDataSet

def get_loader(name):
    """get_loader
    :param name:
    """
    return {
        "cityscapes": cityscapesLoader,
        "pascal_voc": VOCDataSet
    }[name]

def get_data_path(name):
    """get_data_path
    :param name:
    :param config_file:
    """
    if name == 'cityscapes':
        return '../ssda/data/cityscapes/'

    if name == 'gta5':
        return '../ssda/data/gta5/'
    if name == 'pascal_voc':
        return '../data/VOC2012/'
