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
    def execute(self, *args, **kwargs) -> List[str]:
        pass
