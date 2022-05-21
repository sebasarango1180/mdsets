from base import BaseDestination


class S3Destination(BaseDestination):
    """
    Class to use Amazon S3 as a data destination
    """

    def __init__(
        self, bucket: str = None, prefix: str = None, *args, **kwargs
    ) -> None:
        super().__init__()
