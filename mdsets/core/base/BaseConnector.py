from abc import ABC, abstractmethod


class BaseConnector(ABC):
    """
    Class intended to define the downloading and uploading mechanisms that
    every source needs to follow to be consistent with the project.
    """

    def __init__(self, source, destination):
        pass

    @abstractmethod
    def download(self):
        pass

    def upload(self):
        pass
