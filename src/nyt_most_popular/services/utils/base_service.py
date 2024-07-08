from typing import Any, Dict
from enum import Enum

from .default_headers import DefaultHeaders, DefaultHeadersKeys
from ...net.transport.request import Request
from ...net.request_chain.request_chain import RequestChain
from ...net.request_chain.handlers.hook_handler import HookHandler
from ...net.request_chain.handlers.http_handler import HttpHandler
from ...net.request_chain.handlers.retry_handler import RetryHandler


class BaseService:
    """
    A base class for services providing common functionality.

    :ivar str base_url: The base URL for the service.
    :ivar dict _default_headers: A dictionary of default headers.
    """

    def __init__(self, base_url: str) -> None:
        """
        Initializes a BaseService instance.

        :param str base_url: The base URL for the service. Defaults to None.
        """
        self.base_url = base_url
        self._default_headers = DefaultHeaders()

        self._additional_variables = {}

        self._request_handler = self._get_request_handler()

    def set_additional_variables(self, api_key: str = None):
        """
        Sets the additional variables for the service.
        """
        if api_key is not None:
            self._additional_variables["api_key"] = api_key

        self._request_handler = self._get_request_handler()
        return self

    def set_base_url(self, base_url: str):
        """
        Sets the base URL for the service.

        :param str base_url: The base URL to be set.
        """
        self.base_url = base_url

        return self

    def send_request(self, request: Request) -> dict:
        """
        Sends the given request.

        :param Request request: The request to be sent.
        :return: The response data.
        :rtype: dict
        """
        response = self._request_handler.send(request)
        return response.body

    def get_default_headers(self) -> list:
        """
        Get the default headers.

        :return: A list of the default headers.
        :rtype: list
        """
        return self._default_headers.get_headers()

    def _get_request_handler(self) -> RequestChain:
        """
        Get the request chain.

        :return: The request chain.
        :rtype: RequestChain
        """
        return (
            RequestChain()
            .add_handler(RetryHandler())
            .add_handler(HookHandler(self._additional_variables))
            .add_handler(HttpHandler())
        )
