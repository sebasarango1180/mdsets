from abc import (
    ABCMeta,
    abstractmethod,
    abstractclassmethod,
    abstractstaticmethod,
)

class BaseDataset(object, metaclass=ABCMeta):
    """
    Abstract class to outline attributes and methods for mdsets Datasets.
    """

    def __init__(self) -> None:
        pass