from abc import ABC, abstractmethod


class BaseConnector(ABC):
    """
    Class intended to define the downloading and uploading mechanisms that every source need to follow up to be consistent in the project.
    """

    def __init__(self, source, destination):
        pass

    @abstractmethod
    def download(self):
        pass

    def upload(self):
        pass
