from mdsets.core.base.BaseConnector import BaseConnector


class ExampleConnector(BaseConnector):
    """
    Example class to show how to implement from base connector, don't use.
    """

    def __init__(self, source, destination):
        super().__init__(source, destination)

    def download(self):
        print("Start download")
        return source.download()

    def upload(self):
        print("Start upload")
        return destination.upload()
