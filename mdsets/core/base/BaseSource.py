from abc import ABC, abstractmethod


class BaseSource(ABC):
    """
    Base class to define which methods need to implement every downloader to
    retrieve data from an specific source.
    """

    @abstractmethod
    def download(self):
        pass
