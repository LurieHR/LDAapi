# coding: utf-8

"""
    Lobbying Disclosure

    # About the REST API  ## Introduction  This document describes the resources that make up the official Lobbying Disclosure REST API v1. If you have any  issues, please contact the Senate Office of Public Records (OPR) at [lobby@sec.senate.gov](mailto:lobby@sec.senate.gov). OPR does not offer development advice and does not provide language specific guides. The REST API is programming  language agnostic. Any programming language can be used to make REST API requests to retrieve data.  The REST API is documented in the **OpenAPI format** which can be found by clicking the \"Download\" button at the top  of the page. In addition to the standard OpenAPI syntax, we use a few  [vendor extensions](https://github.com/Redocly/redoc/blob/master/docs/redoc-vendor-extensions.md). There are a  variety of open source and proprietary tools that can read OpenAPI specifications and interact with the API by reading  the published specification. OPR does not recommend any specific OpenAPI tools.  ## Terms of Service  REST API is governed by a [Terms of Service](https://lda.senate.gov/api/tos/).  ## Changes  | Date | Description | | ------ | ------ | | 05/09/2024 | Clarified documentation on: date format when filtering results (yyyy-mm-dd) and constants information. | | 01/18/2024 | Added limitations / caveats section | | 08/08/2023 | Change request throttle rates from by hour to by minute to reduce burstable requests. New request throttles: unauthenticated (anon): 15/minute (900/hour), API key (registered): 120/minute (7,200/hour) | | 04/05/2023 | Added requirements to use at least one query string parameter value when paginating results for `Filings` and `Contribution Reports`. See warnings in [Pagination](#section/Implementation-Details/Pagination) for more information. | | 04/05/2023 | Removed ordering filters for performance reasons. Filing: `id`; Contribution Report: `id`; Client: `registrant_name`; Lobbyist: all but `id` | | 12/14/2022 | Added registrant address fields as indicated on the latest LD1 / LD2 filing to the filing endpoint. | | 03/28/2022 | Fixed an issue where LD2 filings posted from 2/15/2022 to 3/28/2022 did not display income or expenses. | | 01/24/2022 | Added Advanced Text Searching in Filing endpoint on fields: `filing_specific_lobbying_issues`, `lobbyist_conviction_disclosure`, and `lobbyist_covered_position`. | | 01/13/2022 | Fixed an issue where the list of Contribution Items in Contribution Reports (LD-203) endpoint did not match the filed Contribution Report document. | | 07/30/2021 | Added Lobbyist endpoint | | 03/10/2021 | Decreased pagination to 25. Increased request throttle rates: unauthenticated (anon): 1,000/hour, API key (registered): 20,000/hour |   ## Schema  All REST API access is over HTTPS, and accessed from `https://lda.senate.gov/api/v1/`. All data is sent and received as JSON.  Testing can be done through [human browseable API interface](https://lda.senate.gov/api/v1/) where it is possible to make  requests with filtering/ordering and pagination.  Blank fields are included as `null` instead of being omitted.  All timestamps return in ISO 8601 format:  ```text YYYY-MM-DDTHH:MM:SSZ ```  ## Root Endpoint  Sending a request with `GET` to the root endpoint will return all the endpoint categories that the REST API v1  supports:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/ ```  **Reponse:**  ```http request HTTP 200 OK Allow: GET, HEAD, OPTIONS Content-Type: application/json Vary: Accept  {     \"filings\": \"https://lda.senate.gov/api/v1/filings/\",     \"contributions\": \"https://lda.senate.gov/api/v1/contributions/\",     \"registrants\": \"https://lda.senate.gov/api/v1/registrants/\",     \"clients\": \"https://lda.senate.gov/api/v1/clients/\",     \"lobbyists\": \"https://lda.senate.gov/api/v1/lobbyists/\",     \"constants/filing/filingtypes\": \"https://lda.senate.gov/api/v1/constants/filing/filingtypes/\",     \"constants/filing/lobbyingactivityissues\": \"https://lda.senate.gov/api/v1/constants/filing/lobbyingactivityissues/\",     \"constants/filing/governmententities\": \"https://lda.senate.gov/api/v1/constants/filing/governmententities/\",     \"constants/general/countries\": \"https://lda.senate.gov/api/v1/constants/general/countries/\",     \"constants/general/states\": \"https://lda.senate.gov/api/v1/constants/general/states/\",     \"constants/lobbyist/prefixes\": \"https://lda.senate.gov/api/v1/constants/lobbyist/prefixes/\",     \"constants/lobbyist/suffixes\": \"https://lda.senate.gov/api/v1/constants/lobbyist/suffixes/\" } ```  ## Browsable API  APIs may be for machines to access, but humans have to be able to read APIS as well. We support a human-friendly  HTML output when `HTML` format is requested where it is possible to make requests with filtering/ordering and  pagination.  [View the HTML API output](https://lda.senate.gov/api/v1/).  ## Constants  Lists of key / value constants are published for the following fields:  * Filing Types * Lobbying Activity Issues * Government Entities * Countries * States (US States) * Prefixes (e.g. Mr., Ms., Mx., Dr., etc.) * Suffixes (e.g. Sr., Jr., II, etc.)  These endpoints are periodically updated when new key / values are added. Please see the API [Constants](#tag/Constants) section section of this documenation for more information.  # Authentication   There are two ways to authenticate through the REST API. Our API offers two types of authentication:  * API Key (Registered) * Unauthenticated (Anonymous)  For clients to authenticate using an API Key, the token key must be included in the `Authorization` HTTP header and  **must** be prefixed by the string literal \"Token\", with whitespace separating the two strings. For example:  ```http request Authorization: Token z944b09199c62bcf9418ad846dd0e4bbdfc6ee4b ```  For clients without an API Key, no special authentication is required, however anonymous clients are subject to  more strict request throttling.  <schema-definitions />   ## Register and Obtain an API Key  [Register](https://lda.senate.gov/api/register/) by using our automated system. After registering, you can obtain an API key  using one of these methods:  * Via a [web form](https://lda.senate.gov/api/auth/login/) * Via an API call (Make a `POST` with your `username` and `password` login credentials as form data or JSON.)  The response will contain your API key if properly authenticated.  **Request:**  ```http request POST https://lda.senate.gov/api/auth/login/  {     \"username\": \"your_username\",     \"password\": \"your_password\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"key\": \"z944b09199c62bcf9418ad846dd0e4bbdfc6ee4b\" } ```  ## Reset Forgotten Password  If you have forgotten your password or need to change it, you can reset your password using one of these methods:  * Via a [web form](https://lda.senate.gov/api/auth/password/reset/) * Via an API call (Make a `POST` with your `email` as form data or JSON.)  **Request:**  ```http request POST https://lda.senate.gov/api/auth/password/reset/  {     \"email\": \"your_email_address\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"detail\": \"Password reset e-mail has been sent.\" } ```  If successful, you will receive email with a `uid` and `token` to reset your password which can be done using one of  these methods:  * Via a [web form](https://lda.senate.gov/api/auth/password/reset/confirm/) * Via an API call (Make a `POST` with you `new_password1` and `new_password2` with the `uid`, and `token` from your  email  as form data or JSON.)  **Request:**  ```http request POST https://lda.senate.gov/api/auth/password/reset/confirm/  {     \"new_password1\": \"new_password\",     \"new_password2\": \"new_password\",     \"uid\": \"UID from your email\",     \"token\": \"Token from your email\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"detail\": \"Password reset e-mail has been sent.\" } ```  # Implementation Details  ## Request Throttling  All REST API requests are throttled to prevent abuse and to ensure stability. Our API is  rate limited depending the type of authentication option you choose:  * API Key (Registered): 120/minute * Unauthenticated (Anonymous): 15/minute  Unauthenticated requests are rate limited by the originating IP address and not the user making requests.  Authenticated requests share the same user quota regardless of whether multiple API keys are used.   Requests made for the following items do not count towards rate limits:  * Original HTML and PDF documents at:   * `https://lda.senate.gov/filings/public/filing/{filing_uuid}/print/`   * `https://lda.senate.gov/filings/public/contribution/{filing_uuid}/print/` * Constants at all URLs starting with `https://lda.senate.gov/api/v1/constants/*`  Requests that exceed the throttling rate for your authentication type will received an HTTP 429 `Too Many Requests`  response. The `Retry-After` header in the response will indicate the number of seconds to wait.  **Response:**  ```http request HTTP 429 Too Many Requests Allow: GET Content-Type: application/json Retry-After: 1596 Vary: Accept  {     \"detail\": \"Request was throttled. Expected available in 1596 seconds.\" } ```  ## Pagination  Large result sets are split into individual pages of data. The pagination links are provided as part of the content  of the response via the `next` and `previous` keys in the response. You can control which page to request by using  the `page` query string parameter.  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?page=2 ```  **Response:**  ```http request HTTP 200 OK  {     \"count\": 1023     \"next\": \"https://lda.senate.gov/api/v1/filings/?page=1\",     \"previous\": \"https://lda.senate.gov/api/v1/filings/?page=3\",     \"results\": [        …     ] } ```  By default, each page is limited to 25 results per page. You may set the page size by setting `page_size`  as a query string parameter up to 25.  **Warning**  The `Filings` and `Contribution Reports` endpoints require at least one queryset parameter to be passed in order to paginate results beyond the first page.  This is for performance reasons.  If you would like to paginate through all `Filings`, we recommend paginating through the results by filing year. Below  shows an example of getting page 2 of results for filing year 2023 for `Filings`.  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=2 ```  **Response:**  ```http request HTTP 200 OK  {     \"count\": 1023     \"next\": \"https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=1\",     \"previous\": \"https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=3\",     \"results\": [        …     ] } ```  ## Ordering  Result sets can be ordered by using the `ordering` query string parameter. Each endpoint has its own set of fields you  can order by so see the available ordering in the [browseable API interface](https://lda.senate.gov/api/v1/) under the \"Filters\"  button in the upper right corner of the interface.  For example, to order filings by `dt_posted`:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=dt_posted ```  The client may also specify reverse orderings by prefixing the field name with `-`, like so:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=-dt_posted ```  Multiple orderings may also be specified:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=dt_posted,registrant__name ```  ## Advanced Text Searching  - **Unquoted Text** - Text not inside quote marks will not be treated as a phrase. Text separated by a space is treated as an OR operator between them. _Estate Tax_ will match _estate_ OR _tax_ even if they do appear next to each other. - **&quot;Quoted Text&quot;** - Text inside double quote marks will be treated as a phrase. _Estate Tax_ will match the phrase _estate tax_ but will not match the words _estate_ or _tax_ if they appear separately. - **OR** - The word _OR_ will be treated as a true OR operator. _&quot;Estate Tax&quot; OR &quot;Estate Taxes&quot;_ will match the phrases _estate tax_or _estate taxes_ but will not match the words _estate_ or _tax_ if they appear separately. - **-** The dash character _-_ will be treated as a NOT EQUALS operator. _&quot;Estate Tax&quot; -&quot;Payroll Taxes&quot;_ will match the phrase _estate tax_ but not _payroll taxes_ if they appear in the same field.  ## Limitations / Caveats  - **Government Entities** - Filings that posted before 2/14/2021 do not have government entities broken down by each individual lobbying activity area. Instead, the government entities listed on these filings is a list of entities that appear on the filing as a whole. This limitation is due to data imported from a legacy system. Filings that posted after 2/14/2021 will have government entities broken down by each individual lobbying activity area.  # Common Errors  ## Invalid API Key  If you supply an invalid API Key, you will receive an HTTP 401 `Unauthorized` response:  **Response:**  ```http request HTTP 401 UNAUTHORIZED  {     \"detail\": \"Invalid token.\" } ```  ## Request Throttled  If you exceed your rate limit for your authentication type, you will receive an HTTP 429 `Too Many Requests`  response. See the [Request Throttling](#section/Implementation-Details/Request-Throttling) section for more information.  **Response:**  ```http request HTTP 429 Too Many Requests Allow: GET Content-Type: application/json Retry-After: 1596 Vary: Accept  {     \"detail\": \"Request was throttled. Expected available in 1596 seconds.\" } ```  ## Invalid Query String Parameter Values  If you pass invalid query string parameter values, you will likely receive an HTTP 404 `Not Found` or HTTP 400  `Bad Request` response with a detailed error message.  For example, passing a non-integer for the page number:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?page=a ```  **Response:**  ```http request HTTP 404 Not Found Allow: GET Content-Type: application/json Vary: Accept  {     \"detail\": \"Invalid page.\" } ```  For example, passing an invalid value for the Registrant ID:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?registrant_id=a ```  **Response:**  ```http request HTTP 400 Bad Request Allow: GET Content-Type: application/json Vary: Accept  {     \"registrant_id\": [         \"Enter a number.\"     ] } ```  ## Unsupported HTTP Method  If you use an unsupported HTTP method, you will receive an HTTP 405 `Method Not Allowed` response:  ```http request DELETE https://lda.senate.gov/api/v1/filings/ Accept: application/json ```  **Response:**  ```http request HTTP 405 Method Not Allowed Content-Type: application/json Content-Length: 42  {     \"detail\": \"Method \\\"DELETE\\\" not allowed.\" } ```  ## Query String Filters Required for Pagination  If you use paginated results and do not include at least one query string parameter filter, you will receive an HTTP 400 `Bad Request` response:  ```http request GET https://lda.senate.gov/api/v1/filings/?page=2 ```  **Response:**  ```http request HTTP 400 Bad Request Allow: GET Content-Type: application/json Vary: Accept  {    \"detail\": \"You must pass at least one query string parameter to filter the results and be able to paginate the results.\" } ```  See warnings in [Pagination](#section/Implementation-Details/Pagination) for more information.

    The version of the OpenAPI document: 1.0.0
    Contact: lobby@sec.senate.gov
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import copy
import http.client as httplib
import logging
from logging import FileHandler
import multiprocessing
import sys
from typing import Any, ClassVar, Dict, List, Literal, Optional, TypedDict
from typing_extensions import NotRequired, Self

import urllib3


JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}

ServerVariablesT = Dict[str, str]

GenericAuthSetting = TypedDict(
    "GenericAuthSetting",
    {
        "type": str,
        "in": str,
        "key": str,
        "value": str,
    },
)


OAuth2AuthSetting = TypedDict(
    "OAuth2AuthSetting",
    {
        "type": Literal["oauth2"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


APIKeyAuthSetting = TypedDict(
    "APIKeyAuthSetting",
    {
        "type": Literal["api_key"],
        "in": str,
        "key": str,
        "value": Optional[str],
    },
)


BasicAuthSetting = TypedDict(
    "BasicAuthSetting",
    {
        "type": Literal["basic"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": Optional[str],
    },
)


BearerFormatAuthSetting = TypedDict(
    "BearerFormatAuthSetting",
    {
        "type": Literal["bearer"],
        "in": Literal["header"],
        "format": Literal["JWT"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


BearerAuthSetting = TypedDict(
    "BearerAuthSetting",
    {
        "type": Literal["bearer"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


HTTPSignatureAuthSetting = TypedDict(
    "HTTPSignatureAuthSetting",
    {
        "type": Literal["http-signature"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": None,
    },
)


AuthSettings = TypedDict(
    "AuthSettings",
    {
        "ApiKeyAuth": APIKeyAuthSetting,
    },
    total=False,
)


class HostSettingVariable(TypedDict):
    description: str
    default_value: str
    enum_values: List[str]


class HostSetting(TypedDict):
    url: str
    description: str
    variables: NotRequired[Dict[str, HostSettingVariable]]


class Configuration:
    """This class contains various settings of the API client.

    :param host: Base url.
    :param ignore_operation_servers
      Boolean to ignore operation servers for the API client.
      Config will use `host` as the base url regardless of the operation servers.
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer).
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param access_token: Access token.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.
    :param retries: Number of retries for API requests.

    :Example:

    API Key Authentication Example.
    Given the following security scheme in the OpenAPI specification:
      components:
        securitySchemes:
          cookieAuth:         # name for the security scheme
            type: apiKey
            in: cookie
            name: JSESSIONID  # cookie name

    You can programmatically set the cookie:

conf = openapi_client.Configuration(
    api_key={'cookieAuth': 'abc123'}
    api_key_prefix={'cookieAuth': 'JSESSIONID'}
)

    The following cookie will be added to the HTTP request:
       Cookie: JSESSIONID abc123
    """

    _default: ClassVar[Optional[Self]] = None

    def __init__(
        self,
        host: Optional[str]=None,
        api_key: Optional[Dict[str, str]]=None,
        api_key_prefix: Optional[Dict[str, str]]=None,
        username: Optional[str]=None,
        password: Optional[str]=None,
        access_token: Optional[str]=None,
        server_index: Optional[int]=None, 
        server_variables: Optional[ServerVariablesT]=None,
        server_operation_index: Optional[Dict[int, int]]=None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]]=None,
        ignore_operation_servers: bool=False,
        ssl_ca_cert: Optional[str]=None,
        retries: Optional[int] = None,
        *,
        debug: Optional[bool] = None,
    ) -> None:
        """Constructor
        """
        self._base_path = "https://lda.senate.gov" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.ignore_operation_servers = ignore_operation_servers
        """Ignore operation servers
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.access_token = access_token
        """Access token
        """
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("openapi_client")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler: Optional[FileHandler] = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        if debug is not None:
            self.debug = debug
        else:
            self.__debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy: Optional[str] = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = retries
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    def __deepcopy__(self, memo:  Dict[int, Any]) -> Self:
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default: Optional[Self]) -> None:
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    @classmethod
    def get_default_copy(cls) -> Self:
        """Deprecated. Please use `get_default` instead.

        Deprecated. Please use `get_default` instead.

        :return: The configuration object.
        """
        return cls.get_default()

    @classmethod
    def get_default(cls) -> Self:
        """Return the default configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = cls()
        return cls._default

    @property
    def logger_file(self) -> Optional[str]:
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value: Optional[str]) -> None:
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self) -> bool:
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value: bool) -> None:
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self) -> str:
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value: str) -> None:
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier: str, alias: Optional[str]=None) -> Optional[str]:
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

        return None

    def get_basic_auth_token(self) -> Optional[str]:
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self)-> AuthSettings:
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth: AuthSettings = {}
        if 'ApiKeyAuth' in self.api_key:
            auth['ApiKeyAuth'] = {
                'type': 'api_key',
                'in': 'header',
                'key': 'Authorization',
                'value': self.get_api_key_with_prefix(
                    'ApiKeyAuth',
                ),
            }
        return auth

    def to_debug_report(self) -> str:
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self) -> List[HostSetting]:
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://lda.senate.gov",
                'description': "No description provided",
            }
        ]

    def get_host_from_settings(
        self,
        index: Optional[int],
        variables: Optional[ServerVariablesT]=None,
        servers: Optional[List[HostSetting]]=None,
    ) -> str:
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self) -> str:
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value: str) -> None:
        """Fix base path."""
        self._base_path = value
        self.server_index = None
