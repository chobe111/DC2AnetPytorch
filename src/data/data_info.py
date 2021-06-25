import numpy as np
from typing import List
from abc import ABCMeta, ABC, abstractmethod
import os
import sys


class BaseData(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __len__():
        """
        return : Dataset Total Length
        """
        return 0

    def check_data_exist(self, file_path: str):
        if not os.path.isfile(file_path):
            sys.exit("[!] Data file Doesn`t Exist Exit Process..")


class TFRecordData(BaseData):
    def __init__(self, name: str, train_data_path: str, test_data_path: str):
        super(TFRecordData, self).__init__()
        self.name = name
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path

    def __len__() -> int:
        pass

    def __call__(self, is_train: bool) -> str:
        data_path = self.train_data_path if is_train else self.test_data_path
        self.check_data_exist(data_path)

        return data_path


class BrainT2Data(TFRecordData):
    def __init__(self):
        name = "Katolic T2 Data"
        train_data_path = "/"
        test_data_path = "/"

        super().__init__(name, train_data_path, test_data_path)


class BrainT1Data(TFRecordData):
    def __init__(self):
        name = "Katolic T1 Data"
        train_data_path = "/"
        test_data_path = "/"

        super().__init__(name, train_data_path, test_data_path)


class BrainGDFData(TFRecordData):
    def __init__(self):
        name = "Katolic GD Focus Data"
        train_data_path = "/"
        test_data_path = "/"

        super().__init__(name, train_data_path, test_data_path)


class BrainGDTData(TFRecordData):
    def __init__(self):
        name = "Katolic GD Total Data"
        train_data_path = "/"
        test_data_path = "/"

        super().__init__(name, train_data_path, test_data_path)
