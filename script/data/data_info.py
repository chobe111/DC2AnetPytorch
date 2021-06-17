import numpy as np

class BaseData:
    pass


class BrainT2Data(BaseData):
    def __init__(self) -> None:
        self.name = "Katolic T2 Data"
        self.train_data_path = "/"
        self.test_data_path = "/"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass


class BrainT1Data(BaseData):
    def __init__(self) -> None:
        self.name = "Katolic T1 Data"
        self.train_data_path = "/"
        self.test_data_path = "/"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
