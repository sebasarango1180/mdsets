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


class BaseOperator(object, metaclass=ABCMeta):
    """
    Abstract class to outline attributes and methods for mdsets Operators.
    """

    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def get_source_hook(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def get_destination_hook(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def transfer(self, *args, **kwargs) -> List[str]:
        pass
