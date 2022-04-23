from asyncio import sleep
from mdsets.core.base.BaseSource import BaseSource


class ExampleSource(BaseSource):
    """
    Example class to show how to implement from base source, don't use.
    """

    def __init__(self) -> None:
        super().__init__()

    def download():
        print('Downloading...')
        sleep(2)
        print('Done!')
        return super.download()