from abc import ABC, abstractmethod


class BaseDestination(ABC):
    """
    Base class to define which methods need to implement every uploader to reach an specific destination
    """


    @abstractmethod
    def upload(self):
        pass
