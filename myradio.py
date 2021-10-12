"""
    URY Mixclouder2

    Module for methods relating to the MyRadio API
"""
import enum
import typing as T

import requests

import config
from utils import MixclouderException


class HTTPMethod(enum.Enum):
    """HTTP Methods we can call on the MyRadio API"""
    GET = requests.get
    POST = requests.post


def myradio_api_request(
    url: str,
    payload: T.Optional[T.Dict[str, T.Any]] = None,
    retry: bool = True,
    method: HTTPMethod = HTTPMethod.GET
) -> T.Dict[str, T.Any]:
    """
    Make a request to the MyRadio API

    Params:
        - url: str: The endpoint we're going to call
        - payload: str: The additional parameters to pass in the URL
        - retry: bool: Whether to retry the API call if it fails
        - method: HTTPMethod: Whether to be a Get or a Post request

    Returns:
        Dict[str, Any] - The response from the API

    Raises:
        - MixclouderException if the API call is unsuccessful
    """
    if payload is None:
        payload = {}

    payload["api_key"] = config.MYRADIO_API_KEY

    req_func: T.Callable = method.value

    res = req_func(config.MYRADIO_URL + url, params=payload).json()

    if res["status"] == "OK":
        return res["payload"]

    if res["status"] == 403:
        raise MixclouderException(
            "Unauthorised", f"API Key doesn't have access to {url}")
    if res["status"] == 401:
        raise MixclouderException("Missing API Key", "API Key Not Provided")

    if retry:
        myradio_api_request(url, payload, False, method)

    raise MixclouderException("Unexpected MyRadio Response", f"{res}")


if __name__ == "__main__":
    print("Run mixclouder.py")
