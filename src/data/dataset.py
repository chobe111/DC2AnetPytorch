from torch.utils.data import Dataset, DataLoader
from tfrecord.torch.dataset import TFRecordDataset
import glob
import os
import cv2
from typing import List, Union, Optional, Tuple
from torchvision.io import decode_jpeg, decode_image, image
import torch
from utils import decode_name


class CustomTFRecordDataset(TFRecordDataset):
    """
    Train Brain T1 From Katolic Data

    TFRecords Data Description Must Include

    'image/file_name' : 'string'
    'image/encoded_image' : 'string'

    """
    @staticmethod
    def decode_features(features: dict) -> dict:
        features["image/encoded_image"] = decode_image(
            features["image/encoded_image"], mode=image.ImageReadMode.GRAY)
        features["image/file_name"] = decode_name(features["image/file_name"])

        return features

    def __init__(self, tfrecod_path: str, index_path: Union[str, None], description: dict, transform=decode_features) -> None:
        super(CustomTFRecordDataset, self).__init__(
            tfrecod_path, index_path, description, transform=transform)
