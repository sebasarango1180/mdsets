from abc import (
    ABCMeta,
    abstractmethod,
    abstractclassmethod,
    abstractstaticmethod,
)
from typing import (
    List,
    Any
)


class BaseHook(object, metaclass=ABCMeta):
    """
    Abstract class to outline attributes and methods for mdsets Hooks.
    """

    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def get_connection(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def list_objects(self, *args, **kwargs) -> List[str]:
        pass

    @abstractmethod
    def download(self, *args, **kwargs) -> List[str]:
        pass

    @abstractmethod
    def upload(self, *args, **kwargs) -> List[str]:
        pass