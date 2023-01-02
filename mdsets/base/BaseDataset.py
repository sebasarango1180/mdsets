from abc import (
    ABC,
    abstractproperty,
    abstractmethod,
    abstractclassmethod,
    abstractstaticmethod,
)


class BaseDataset(ABC):
    """
    Abstract class to outline attributes and methods for mdsets Datasets.
    """

    def __init__(self) -> None:
        pass