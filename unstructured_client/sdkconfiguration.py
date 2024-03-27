"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple, Callable, Union
from .utils.retries import RetryConfig
from .utils import utils
from unstructured_client.models import shared


SERVER_PROD = 'prod'
r"""Hosted API"""
SERVER_LOCAL = 'local'
r"""Development server"""
SERVERS = {
	SERVER_PROD: 'https://api.unstructured.io',
	SERVER_LOCAL: 'http://localhost:8000',
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: requests.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: str = ''
    server: str = ''
    language: str = 'python'
    openapi_doc_version: str = '0.0.1'
    sdk_version: str = '0.18.0'
    gen_version: str = '2.250.19'
    user_agent: str = 'speakeasy-sdk/python 0.18.0 2.250.19 0.0.1 unstructured-client'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if not self.server:
            self.server = SERVER_PROD

        return SERVERS[self.server], {}