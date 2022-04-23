from abc import ABC, abstractmethod


class BaseDestination(ABC):
    """
    Base class to define which methods are to be implemented by every uploader
    to write to a specific destination.
    """

    @abstractmethod
    def upload(self):
        pass
