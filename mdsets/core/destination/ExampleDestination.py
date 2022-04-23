from asyncio import sleep
from mdsets.core.base.BaseDestination import BaseDestination


class ExampleDestination(BaseDestination):
    """
    Example class to show how to implement from base destination
    """
    def __init__(self) -> None:
        super().__init__()

    def upload(self):
        print('Uploading...')
        sleep(3)
        print('Done!')
        return super().upload()