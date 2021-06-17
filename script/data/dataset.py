from torch.utils.data import Dataset
import torchvision.transforms as transforms
import glob
import os
from tfrecord.torch.dataset import TFRecordDataset
import cv2
from typing import List, Union, Optional, Tuple


class CustomTFRecordDataset(TFRecordDataset):
    """
    Train B
    """

    def __init__(self, tfrecod_path: str, index_path: Union[str, None], description: dict) -> None:
        super().__init__(tfrecod_path, index_path, description)

    def __getitem__() -> None:
        pass

    def __len__():
        pass


class DicomImageDataset(Dataset):
    def __init__(self):
        pass

    def __getitem__(self, index):
        pass

    def __len__():
        pass


class PngImageDataset(Dataset):
    def __init__(self):
        pass

    def __getitem__(self, index):
        pass

    def __len__():
        pass
