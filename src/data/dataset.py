from torch.utils.data import Dataset
import torchvision.transforms as transforms
import glob
import os
from tfrecord.torch.dataset import TFRecordDataset
import cv2
from typing import List, Union, Optional, Tuple
from utils import decode_image

class CustomTFRecordDataset(TFRecordDataset):
    """
    Train Brain T1 From Katolic Data

    TFRecords Data Description Must Include

    'image/file_name' : 'string'
    'image/encoded_image' : 'string'

    """
    def __init__(self, tfrecod_path: str, index_path: Union[str, None], description: dict, transform=decode_image) -> None:
        super().__init__(tfrecod_path, index_path, description, transform=decode_image)

