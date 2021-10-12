"""
    URY Mixclouder2

    Additional helpful functions, classes and exceptions
"""


class MixclouderException(BaseException):
    """
    Base MixclouderException. Other exceptions can extend from here.
    """

    def __init__(self, err_type: str, data: str):
        super().__init__(f"Mixclouder Exception: {err_type} - {data}")
