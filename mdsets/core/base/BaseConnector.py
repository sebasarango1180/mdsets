from abc import ABC, abstractmethod


class BaseConnector(ABC):
    """
    Class intended to define the downloading and uploading mechanisms that
    every connector needs to follow to be consistent with the project.
    """

    def __init__(self):
        pass

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def upload(self):
        pass

    @abstractmethod
    def _authenticate(self):
        pass

    @abstractmethod
    def _get_connection(self):
        pass
