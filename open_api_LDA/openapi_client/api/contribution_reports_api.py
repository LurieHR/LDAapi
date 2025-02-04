# coding: utf-8

"""
    Lobbying Disclosure

    # About the REST API  ## Introduction  This document describes the resources that make up the official Lobbying Disclosure REST API v1. If you have any  issues, please contact the Senate Office of Public Records (OPR) at [lobby@sec.senate.gov](mailto:lobby@sec.senate.gov). OPR does not offer development advice and does not provide language specific guides. The REST API is programming  language agnostic. Any programming language can be used to make REST API requests to retrieve data.  The REST API is documented in the **OpenAPI format** which can be found by clicking the \"Download\" button at the top  of the page. In addition to the standard OpenAPI syntax, we use a few  [vendor extensions](https://github.com/Redocly/redoc/blob/master/docs/redoc-vendor-extensions.md). There are a  variety of open source and proprietary tools that can read OpenAPI specifications and interact with the API by reading  the published specification. OPR does not recommend any specific OpenAPI tools.  ## Terms of Service  REST API is governed by a [Terms of Service](https://lda.senate.gov/api/tos/).  ## Changes  | Date | Description | | ------ | ------ | | 05/09/2024 | Clarified documentation on: date format when filtering results (yyyy-mm-dd) and constants information. | | 01/18/2024 | Added limitations / caveats section | | 08/08/2023 | Change request throttle rates from by hour to by minute to reduce burstable requests. New request throttles: unauthenticated (anon): 15/minute (900/hour), API key (registered): 120/minute (7,200/hour) | | 04/05/2023 | Added requirements to use at least one query string parameter value when paginating results for `Filings` and `Contribution Reports`. See warnings in [Pagination](#section/Implementation-Details/Pagination) for more information. | | 04/05/2023 | Removed ordering filters for performance reasons. Filing: `id`; Contribution Report: `id`; Client: `registrant_name`; Lobbyist: all but `id` | | 12/14/2022 | Added registrant address fields as indicated on the latest LD1 / LD2 filing to the filing endpoint. | | 03/28/2022 | Fixed an issue where LD2 filings posted from 2/15/2022 to 3/28/2022 did not display income or expenses. | | 01/24/2022 | Added Advanced Text Searching in Filing endpoint on fields: `filing_specific_lobbying_issues`, `lobbyist_conviction_disclosure`, and `lobbyist_covered_position`. | | 01/13/2022 | Fixed an issue where the list of Contribution Items in Contribution Reports (LD-203) endpoint did not match the filed Contribution Report document. | | 07/30/2021 | Added Lobbyist endpoint | | 03/10/2021 | Decreased pagination to 25. Increased request throttle rates: unauthenticated (anon): 1,000/hour, API key (registered): 20,000/hour |   ## Schema  All REST API access is over HTTPS, and accessed from `https://lda.senate.gov/api/v1/`. All data is sent and received as JSON.  Testing can be done through [human browseable API interface](https://lda.senate.gov/api/v1/) where it is possible to make  requests with filtering/ordering and pagination.  Blank fields are included as `null` instead of being omitted.  All timestamps return in ISO 8601 format:  ```text YYYY-MM-DDTHH:MM:SSZ ```  ## Root Endpoint  Sending a request with `GET` to the root endpoint will return all the endpoint categories that the REST API v1  supports:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/ ```  **Reponse:**  ```http request HTTP 200 OK Allow: GET, HEAD, OPTIONS Content-Type: application/json Vary: Accept  {     \"filings\": \"https://lda.senate.gov/api/v1/filings/\",     \"contributions\": \"https://lda.senate.gov/api/v1/contributions/\",     \"registrants\": \"https://lda.senate.gov/api/v1/registrants/\",     \"clients\": \"https://lda.senate.gov/api/v1/clients/\",     \"lobbyists\": \"https://lda.senate.gov/api/v1/lobbyists/\",     \"constants/filing/filingtypes\": \"https://lda.senate.gov/api/v1/constants/filing/filingtypes/\",     \"constants/filing/lobbyingactivityissues\": \"https://lda.senate.gov/api/v1/constants/filing/lobbyingactivityissues/\",     \"constants/filing/governmententities\": \"https://lda.senate.gov/api/v1/constants/filing/governmententities/\",     \"constants/general/countries\": \"https://lda.senate.gov/api/v1/constants/general/countries/\",     \"constants/general/states\": \"https://lda.senate.gov/api/v1/constants/general/states/\",     \"constants/lobbyist/prefixes\": \"https://lda.senate.gov/api/v1/constants/lobbyist/prefixes/\",     \"constants/lobbyist/suffixes\": \"https://lda.senate.gov/api/v1/constants/lobbyist/suffixes/\" } ```  ## Browsable API  APIs may be for machines to access, but humans have to be able to read APIS as well. We support a human-friendly  HTML output when `HTML` format is requested where it is possible to make requests with filtering/ordering and  pagination.  [View the HTML API output](https://lda.senate.gov/api/v1/).  ## Constants  Lists of key / value constants are published for the following fields:  * Filing Types * Lobbying Activity Issues * Government Entities * Countries * States (US States) * Prefixes (e.g. Mr., Ms., Mx., Dr., etc.) * Suffixes (e.g. Sr., Jr., II, etc.)  These endpoints are periodically updated when new key / values are added. Please see the API [Constants](#tag/Constants) section section of this documenation for more information.  # Authentication   There are two ways to authenticate through the REST API. Our API offers two types of authentication:  * API Key (Registered) * Unauthenticated (Anonymous)  For clients to authenticate using an API Key, the token key must be included in the `Authorization` HTTP header and  **must** be prefixed by the string literal \"Token\", with whitespace separating the two strings. For example:  ```http request Authorization: Token z944b09199c62bcf9418ad846dd0e4bbdfc6ee4b ```  For clients without an API Key, no special authentication is required, however anonymous clients are subject to  more strict request throttling.  <schema-definitions />   ## Register and Obtain an API Key  [Register](https://lda.senate.gov/api/register/) by using our automated system. After registering, you can obtain an API key  using one of these methods:  * Via a [web form](https://lda.senate.gov/api/auth/login/) * Via an API call (Make a `POST` with your `username` and `password` login credentials as form data or JSON.)  The response will contain your API key if properly authenticated.  **Request:**  ```http request POST https://lda.senate.gov/api/auth/login/  {     \"username\": \"your_username\",     \"password\": \"your_password\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"key\": \"z944b09199c62bcf9418ad846dd0e4bbdfc6ee4b\" } ```  ## Reset Forgotten Password  If you have forgotten your password or need to change it, you can reset your password using one of these methods:  * Via a [web form](https://lda.senate.gov/api/auth/password/reset/) * Via an API call (Make a `POST` with your `email` as form data or JSON.)  **Request:**  ```http request POST https://lda.senate.gov/api/auth/password/reset/  {     \"email\": \"your_email_address\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"detail\": \"Password reset e-mail has been sent.\" } ```  If successful, you will receive email with a `uid` and `token` to reset your password which can be done using one of  these methods:  * Via a [web form](https://lda.senate.gov/api/auth/password/reset/confirm/) * Via an API call (Make a `POST` with you `new_password1` and `new_password2` with the `uid`, and `token` from your  email  as form data or JSON.)  **Request:**  ```http request POST https://lda.senate.gov/api/auth/password/reset/confirm/  {     \"new_password1\": \"new_password\",     \"new_password2\": \"new_password\",     \"uid\": \"UID from your email\",     \"token\": \"Token from your email\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"detail\": \"Password reset e-mail has been sent.\" } ```  # Implementation Details  ## Request Throttling  All REST API requests are throttled to prevent abuse and to ensure stability. Our API is  rate limited depending the type of authentication option you choose:  * API Key (Registered): 120/minute * Unauthenticated (Anonymous): 15/minute  Unauthenticated requests are rate limited by the originating IP address and not the user making requests.  Authenticated requests share the same user quota regardless of whether multiple API keys are used.   Requests made for the following items do not count towards rate limits:  * Original HTML and PDF documents at:   * `https://lda.senate.gov/filings/public/filing/{filing_uuid}/print/`   * `https://lda.senate.gov/filings/public/contribution/{filing_uuid}/print/` * Constants at all URLs starting with `https://lda.senate.gov/api/v1/constants/*`  Requests that exceed the throttling rate for your authentication type will received an HTTP 429 `Too Many Requests`  response. The `Retry-After` header in the response will indicate the number of seconds to wait.  **Response:**  ```http request HTTP 429 Too Many Requests Allow: GET Content-Type: application/json Retry-After: 1596 Vary: Accept  {     \"detail\": \"Request was throttled. Expected available in 1596 seconds.\" } ```  ## Pagination  Large result sets are split into individual pages of data. The pagination links are provided as part of the content  of the response via the `next` and `previous` keys in the response. You can control which page to request by using  the `page` query string parameter.  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?page=2 ```  **Response:**  ```http request HTTP 200 OK  {     \"count\": 1023     \"next\": \"https://lda.senate.gov/api/v1/filings/?page=1\",     \"previous\": \"https://lda.senate.gov/api/v1/filings/?page=3\",     \"results\": [        …     ] } ```  By default, each page is limited to 25 results per page. You may set the page size by setting `page_size`  as a query string parameter up to 25.  **Warning**  The `Filings` and `Contribution Reports` endpoints require at least one queryset parameter to be passed in order to paginate results beyond the first page.  This is for performance reasons.  If you would like to paginate through all `Filings`, we recommend paginating through the results by filing year. Below  shows an example of getting page 2 of results for filing year 2023 for `Filings`.  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=2 ```  **Response:**  ```http request HTTP 200 OK  {     \"count\": 1023     \"next\": \"https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=1\",     \"previous\": \"https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=3\",     \"results\": [        …     ] } ```  ## Ordering  Result sets can be ordered by using the `ordering` query string parameter. Each endpoint has its own set of fields you  can order by so see the available ordering in the [browseable API interface](https://lda.senate.gov/api/v1/) under the \"Filters\"  button in the upper right corner of the interface.  For example, to order filings by `dt_posted`:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=dt_posted ```  The client may also specify reverse orderings by prefixing the field name with `-`, like so:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=-dt_posted ```  Multiple orderings may also be specified:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=dt_posted,registrant__name ```  ## Advanced Text Searching  - **Unquoted Text** - Text not inside quote marks will not be treated as a phrase. Text separated by a space is treated as an OR operator between them. _Estate Tax_ will match _estate_ OR _tax_ even if they do appear next to each other. - **&quot;Quoted Text&quot;** - Text inside double quote marks will be treated as a phrase. _Estate Tax_ will match the phrase _estate tax_ but will not match the words _estate_ or _tax_ if they appear separately. - **OR** - The word _OR_ will be treated as a true OR operator. _&quot;Estate Tax&quot; OR &quot;Estate Taxes&quot;_ will match the phrases _estate tax_or _estate taxes_ but will not match the words _estate_ or _tax_ if they appear separately. - **-** The dash character _-_ will be treated as a NOT EQUALS operator. _&quot;Estate Tax&quot; -&quot;Payroll Taxes&quot;_ will match the phrase _estate tax_ but not _payroll taxes_ if they appear in the same field.  ## Limitations / Caveats  - **Government Entities** - Filings that posted before 2/14/2021 do not have government entities broken down by each individual lobbying activity area. Instead, the government entities listed on these filings is a list of entities that appear on the filing as a whole. This limitation is due to data imported from a legacy system. Filings that posted after 2/14/2021 will have government entities broken down by each individual lobbying activity area.  # Common Errors  ## Invalid API Key  If you supply an invalid API Key, you will receive an HTTP 401 `Unauthorized` response:  **Response:**  ```http request HTTP 401 UNAUTHORIZED  {     \"detail\": \"Invalid token.\" } ```  ## Request Throttled  If you exceed your rate limit for your authentication type, you will receive an HTTP 429 `Too Many Requests`  response. See the [Request Throttling](#section/Implementation-Details/Request-Throttling) section for more information.  **Response:**  ```http request HTTP 429 Too Many Requests Allow: GET Content-Type: application/json Retry-After: 1596 Vary: Accept  {     \"detail\": \"Request was throttled. Expected available in 1596 seconds.\" } ```  ## Invalid Query String Parameter Values  If you pass invalid query string parameter values, you will likely receive an HTTP 404 `Not Found` or HTTP 400  `Bad Request` response with a detailed error message.  For example, passing a non-integer for the page number:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?page=a ```  **Response:**  ```http request HTTP 404 Not Found Allow: GET Content-Type: application/json Vary: Accept  {     \"detail\": \"Invalid page.\" } ```  For example, passing an invalid value for the Registrant ID:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?registrant_id=a ```  **Response:**  ```http request HTTP 400 Bad Request Allow: GET Content-Type: application/json Vary: Accept  {     \"registrant_id\": [         \"Enter a number.\"     ] } ```  ## Unsupported HTTP Method  If you use an unsupported HTTP method, you will receive an HTTP 405 `Method Not Allowed` response:  ```http request DELETE https://lda.senate.gov/api/v1/filings/ Accept: application/json ```  **Response:**  ```http request HTTP 405 Method Not Allowed Content-Type: application/json Content-Length: 42  {     \"detail\": \"Method \\\"DELETE\\\" not allowed.\" } ```  ## Query String Filters Required for Pagination  If you use paginated results and do not include at least one query string parameter filter, you will receive an HTTP 400 `Bad Request` response:  ```http request GET https://lda.senate.gov/api/v1/filings/?page=2 ```  **Response:**  ```http request HTTP 400 Bad Request Allow: GET Content-Type: application/json Vary: Accept  {    \"detail\": \"You must pass at least one query string parameter to filter the results and be able to paginate the results.\" } ```  See warnings in [Pagination](#section/Implementation-Details/Pagination) for more information.

    The version of the OpenAPI document: 1.0.0
    Contact: lobby@sec.senate.gov
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Optional, Union
from typing_extensions import Annotated
from openapi_client.models.contribution_report import ContributionReport
from openapi_client.models.list_contribution_reports200_response import ListContributionReports200Response

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class ContributionReportsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def list_contribution_reports(
        self,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        filing_uuid: Annotated[Optional[StrictStr], Field(description="filing_uuid")] = None,
        filing_type: Annotated[Optional[StrictStr], Field(description="Filing Type")] = None,
        filing_year: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filing Year")] = None,
        filing_period: Annotated[Optional[StrictStr], Field(description="Filing Period")] = None,
        filing_dt_posted_after: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_dt_posted_before: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        registrant_id: Annotated[Optional[StrictInt], Field(description="Registrant ID")] = None,
        registrant_name: Annotated[Optional[StrictStr], Field(description="Registrant Name")] = None,
        lobbyist_id: Annotated[Optional[StrictInt], Field(description="Lobbyist ID")] = None,
        lobbyist_name: Annotated[Optional[StrictStr], Field(description="Lobbyist Name")] = None,
        lobbyist_exclude: Annotated[Optional[StrictBool], Field(description="Exclude reports filed by the lobbyists.")] = None,
        contribution_date_after: Annotated[Optional[date], Field(description="Contribution Date Range (Before / After): yyyy-mm-dd")] = None,
        contribution_date_before: Annotated[Optional[date], Field(description="Contribution Date Range (Before / After): yyyy-mm-dd")] = None,
        contribution_amount_min: Annotated[Optional[StrictStr], Field(description="Contribution Amount Range")] = None,
        contribution_amount_max: Annotated[Optional[StrictStr], Field(description="Contribution Amount Range")] = None,
        contribution_type: Annotated[Optional[StrictStr], Field(description="Contribution Type")] = None,
        contribution_contributor: Annotated[Optional[StrictStr], Field(description="Contribution Contributor Name")] = None,
        contribution_payee: Annotated[Optional[StrictStr], Field(description="Contribution Payee Name")] = None,
        contribution_honoree: Annotated[Optional[StrictStr], Field(description="Contribution Honoree Name")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ListContributionReports200Response:
        """list_contribution_reports

        

        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param filing_uuid: filing_uuid
        :type filing_uuid: str
        :param filing_type: Filing Type
        :type filing_type: str
        :param filing_year: Filing Year
        :type filing_year: float
        :param filing_period: Filing Period
        :type filing_period: str
        :param filing_dt_posted_after: Filing Date Posted Range (Before / After): yyyy-mm-dd
        :type filing_dt_posted_after: datetime
        :param filing_dt_posted_before: Filing Date Posted Range (Before / After): yyyy-mm-dd
        :type filing_dt_posted_before: datetime
        :param registrant_id: Registrant ID
        :type registrant_id: int
        :param registrant_name: Registrant Name
        :type registrant_name: str
        :param lobbyist_id: Lobbyist ID
        :type lobbyist_id: int
        :param lobbyist_name: Lobbyist Name
        :type lobbyist_name: str
        :param lobbyist_exclude: Exclude reports filed by the lobbyists.
        :type lobbyist_exclude: bool
        :param contribution_date_after: Contribution Date Range (Before / After): yyyy-mm-dd
        :type contribution_date_after: date
        :param contribution_date_before: Contribution Date Range (Before / After): yyyy-mm-dd
        :type contribution_date_before: date
        :param contribution_amount_min: Contribution Amount Range
        :type contribution_amount_min: float
        :param contribution_amount_max: Contribution Amount Range
        :type contribution_amount_max: float
        :param contribution_type: Contribution Type
        :type contribution_type: str
        :param contribution_contributor: Contribution Contributor Name
        :type contribution_contributor: str
        :param contribution_payee: Contribution Payee Name
        :type contribution_payee: str
        :param contribution_honoree: Contribution Honoree Name
        :type contribution_honoree: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_contribution_reports_serialize(
            page=page,
            page_size=page_size,
            ordering=ordering,
            filing_uuid=filing_uuid,
            filing_type=filing_type,
            filing_year=filing_year,
            filing_period=filing_period,
            filing_dt_posted_after=filing_dt_posted_after,
            filing_dt_posted_before=filing_dt_posted_before,
            registrant_id=registrant_id,
            registrant_name=registrant_name,
            lobbyist_id=lobbyist_id,
            lobbyist_name=lobbyist_name,
            lobbyist_exclude=lobbyist_exclude,
            contribution_date_after=contribution_date_after,
            contribution_date_before=contribution_date_before,
            contribution_amount_min=contribution_amount_min,
            contribution_amount_max=contribution_amount_max,
            contribution_type=contribution_type,
            contribution_contributor=contribution_contributor,
            contribution_payee=contribution_payee,
            contribution_honoree=contribution_honoree,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListContributionReports200Response",
            '400': "Error",
            '401': "Error",
            '404': "Error",
            '405': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_contribution_reports_with_http_info(
        self,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        filing_uuid: Annotated[Optional[StrictStr], Field(description="filing_uuid")] = None,
        filing_type: Annotated[Optional[StrictStr], Field(description="Filing Type")] = None,
        filing_year: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filing Year")] = None,
        filing_period: Annotated[Optional[StrictStr], Field(description="Filing Period")] = None,
        filing_dt_posted_after: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_dt_posted_before: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        registrant_id: Annotated[Optional[StrictInt], Field(description="Registrant ID")] = None,
        registrant_name: Annotated[Optional[StrictStr], Field(description="Registrant Name")] = None,
        lobbyist_id: Annotated[Optional[StrictInt], Field(description="Lobbyist ID")] = None,
        lobbyist_name: Annotated[Optional[StrictStr], Field(description="Lobbyist Name")] = None,
        lobbyist_exclude: Annotated[Optional[StrictBool], Field(description="Exclude reports filed by the lobbyists.")] = None,
        contribution_date_after: Annotated[Optional[date], Field(description="Contribution Date Range (Before / After): yyyy-mm-dd")] = None,
        contribution_date_before: Annotated[Optional[date], Field(description="Contribution Date Range (Before / After): yyyy-mm-dd")] = None,
        contribution_amount_min: Annotated[Optional[StrictStr], Field(description="Contribution Amount Range")] = None,
        contribution_amount_max: Annotated[Optional[StrictStr], Field(description="Contribution Amount Range")] = None,
        contribution_type: Annotated[Optional[StrictStr], Field(description="Contribution Type")] = None,
        contribution_contributor: Annotated[Optional[StrictStr], Field(description="Contribution Contributor Name")] = None,
        contribution_payee: Annotated[Optional[StrictStr], Field(description="Contribution Payee Name")] = None,
        contribution_honoree: Annotated[Optional[StrictStr], Field(description="Contribution Honoree Name")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ListContributionReports200Response]:
        """list_contribution_reports

        

        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param filing_uuid: filing_uuid
        :type filing_uuid: str
        :param filing_type: Filing Type
        :type filing_type: str
        :param filing_year: Filing Year
        :type filing_year: float
        :param filing_period: Filing Period
        :type filing_period: str
        :param filing_dt_posted_after: Filing Date Posted Range (Before / After): yyyy-mm-dd
        :type filing_dt_posted_after: datetime
        :param filing_dt_posted_before: Filing Date Posted Range (Before / After): yyyy-mm-dd
        :type filing_dt_posted_before: datetime
        :param registrant_id: Registrant ID
        :type registrant_id: int
        :param registrant_name: Registrant Name
        :type registrant_name: str
        :param lobbyist_id: Lobbyist ID
        :type lobbyist_id: int
        :param lobbyist_name: Lobbyist Name
        :type lobbyist_name: str
        :param lobbyist_exclude: Exclude reports filed by the lobbyists.
        :type lobbyist_exclude: bool
        :param contribution_date_after: Contribution Date Range (Before / After): yyyy-mm-dd
        :type contribution_date_after: date
        :param contribution_date_before: Contribution Date Range (Before / After): yyyy-mm-dd
        :type contribution_date_before: date
        :param contribution_amount_min: Contribution Amount Range
        :type contribution_amount_min: float
        :param contribution_amount_max: Contribution Amount Range
        :type contribution_amount_max: float
        :param contribution_type: Contribution Type
        :type contribution_type: str
        :param contribution_contributor: Contribution Contributor Name
        :type contribution_contributor: str
        :param contribution_payee: Contribution Payee Name
        :type contribution_payee: str
        :param contribution_honoree: Contribution Honoree Name
        :type contribution_honoree: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_contribution_reports_serialize(
            page=page,
            page_size=page_size,
            ordering=ordering,
            filing_uuid=filing_uuid,
            filing_type=filing_type,
            filing_year=filing_year,
            filing_period=filing_period,
            filing_dt_posted_after=filing_dt_posted_after,
            filing_dt_posted_before=filing_dt_posted_before,
            registrant_id=registrant_id,
            registrant_name=registrant_name,
            lobbyist_id=lobbyist_id,
            lobbyist_name=lobbyist_name,
            lobbyist_exclude=lobbyist_exclude,
            contribution_date_after=contribution_date_after,
            contribution_date_before=contribution_date_before,
            contribution_amount_min=contribution_amount_min,
            contribution_amount_max=contribution_amount_max,
            contribution_type=contribution_type,
            contribution_contributor=contribution_contributor,
            contribution_payee=contribution_payee,
            contribution_honoree=contribution_honoree,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListContributionReports200Response",
            '400': "Error",
            '401': "Error",
            '404': "Error",
            '405': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_contribution_reports_without_preload_content(
        self,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        filing_uuid: Annotated[Optional[StrictStr], Field(description="filing_uuid")] = None,
        filing_type: Annotated[Optional[StrictStr], Field(description="Filing Type")] = None,
        filing_year: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filing Year")] = None,
        filing_period: Annotated[Optional[StrictStr], Field(description="Filing Period")] = None,
        filing_dt_posted_after: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_dt_posted_before: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        registrant_id: Annotated[Optional[StrictInt], Field(description="Registrant ID")] = None,
        registrant_name: Annotated[Optional[StrictStr], Field(description="Registrant Name")] = None,
        lobbyist_id: Annotated[Optional[StrictInt], Field(description="Lobbyist ID")] = None,
        lobbyist_name: Annotated[Optional[StrictStr], Field(description="Lobbyist Name")] = None,
        lobbyist_exclude: Annotated[Optional[StrictBool], Field(description="Exclude reports filed by the lobbyists.")] = None,
        contribution_date_after: Annotated[Optional[date], Field(description="Contribution Date Range (Before / After): yyyy-mm-dd")] = None,
        contribution_date_before: Annotated[Optional[date], Field(description="Contribution Date Range (Before / After): yyyy-mm-dd")] = None,
        contribution_amount_min: Annotated[Optional[StrictStr], Field(description="Contribution Amount Range")] = None,
        contribution_amount_max: Annotated[Optional[StrictStr], Field(description="Contribution Amount Range")] = None,
        contribution_type: Annotated[Optional[StrictStr], Field(description="Contribution Type")] = None,
        contribution_contributor: Annotated[Optional[StrictStr], Field(description="Contribution Contributor Name")] = None,
        contribution_payee: Annotated[Optional[StrictStr], Field(description="Contribution Payee Name")] = None,
        contribution_honoree: Annotated[Optional[StrictStr], Field(description="Contribution Honoree Name")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """list_contribution_reports

        

        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param filing_uuid: filing_uuid
        :type filing_uuid: str
        :param filing_type: Filing Type
        :type filing_type: str
        :param filing_year: Filing Year
        :type filing_year: float
        :param filing_period: Filing Period
        :type filing_period: str
        :param filing_dt_posted_after: Filing Date Posted Range (Before / After): yyyy-mm-dd
        :type filing_dt_posted_after: datetime
        :param filing_dt_posted_before: Filing Date Posted Range (Before / After): yyyy-mm-dd
        :type filing_dt_posted_before: datetime
        :param registrant_id: Registrant ID
        :type registrant_id: int
        :param registrant_name: Registrant Name
        :type registrant_name: str
        :param lobbyist_id: Lobbyist ID
        :type lobbyist_id: int
        :param lobbyist_name: Lobbyist Name
        :type lobbyist_name: str
        :param lobbyist_exclude: Exclude reports filed by the lobbyists.
        :type lobbyist_exclude: bool
        :param contribution_date_after: Contribution Date Range (Before / After): yyyy-mm-dd
        :type contribution_date_after: date
        :param contribution_date_before: Contribution Date Range (Before / After): yyyy-mm-dd
        :type contribution_date_before: date
        :param contribution_amount_min: Contribution Amount Range
        :type contribution_amount_min: float
        :param contribution_amount_max: Contribution Amount Range
        :type contribution_amount_max: float
        :param contribution_type: Contribution Type
        :type contribution_type: str
        :param contribution_contributor: Contribution Contributor Name
        :type contribution_contributor: str
        :param contribution_payee: Contribution Payee Name
        :type contribution_payee: str
        :param contribution_honoree: Contribution Honoree Name
        :type contribution_honoree: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_contribution_reports_serialize(
            page=page,
            page_size=page_size,
            ordering=ordering,
            filing_uuid=filing_uuid,
            filing_type=filing_type,
            filing_year=filing_year,
            filing_period=filing_period,
            filing_dt_posted_after=filing_dt_posted_after,
            filing_dt_posted_before=filing_dt_posted_before,
            registrant_id=registrant_id,
            registrant_name=registrant_name,
            lobbyist_id=lobbyist_id,
            lobbyist_name=lobbyist_name,
            lobbyist_exclude=lobbyist_exclude,
            contribution_date_after=contribution_date_after,
            contribution_date_before=contribution_date_before,
            contribution_amount_min=contribution_amount_min,
            contribution_amount_max=contribution_amount_max,
            contribution_type=contribution_type,
            contribution_contributor=contribution_contributor,
            contribution_payee=contribution_payee,
            contribution_honoree=contribution_honoree,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListContributionReports200Response",
            '400': "Error",
            '401': "Error",
            '404': "Error",
            '405': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_contribution_reports_serialize(
        self,
        page,
        page_size,
        ordering,
        filing_uuid,
        filing_type,
        filing_year,
        filing_period,
        filing_dt_posted_after,
        filing_dt_posted_before,
        registrant_id,
        registrant_name,
        lobbyist_id,
        lobbyist_name,
        lobbyist_exclude,
        contribution_date_after,
        contribution_date_before,
        contribution_amount_min,
        contribution_amount_max,
        contribution_type,
        contribution_contributor,
        contribution_payee,
        contribution_honoree,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('page_size', page_size))
            
        if ordering is not None:
            
            _query_params.append(('ordering', ordering))
            
        if filing_uuid is not None:
            
            _query_params.append(('filing_uuid', filing_uuid))
            
        if filing_type is not None:
            
            _query_params.append(('filing_type', filing_type))
            
        if filing_year is not None:
            
            _query_params.append(('filing_year', filing_year))
            
        if filing_period is not None:
            
            _query_params.append(('filing_period', filing_period))
            
        if filing_dt_posted_after is not None:
            if isinstance(filing_dt_posted_after, datetime):
                _query_params.append(
                    (
                        'filing_dt_posted_after',
                        filing_dt_posted_after.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('filing_dt_posted_after', filing_dt_posted_after))
            
        if filing_dt_posted_before is not None:
            if isinstance(filing_dt_posted_before, datetime):
                _query_params.append(
                    (
                        'filing_dt_posted_before',
                        filing_dt_posted_before.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('filing_dt_posted_before', filing_dt_posted_before))
            
        if registrant_id is not None:
            
            _query_params.append(('registrant_id', registrant_id))
            
        if registrant_name is not None:
            
            _query_params.append(('registrant_name', registrant_name))
            
        if lobbyist_id is not None:
            
            _query_params.append(('lobbyist_id', lobbyist_id))
            
        if lobbyist_name is not None:
            
            _query_params.append(('lobbyist_name', lobbyist_name))
            
        if lobbyist_exclude is not None:
            
            _query_params.append(('lobbyist_exclude', lobbyist_exclude))
            
        if contribution_date_after is not None:
            if isinstance(contribution_date_after, date):
                _query_params.append(
                    (
                        'contribution_date_after',
                        contribution_date_after.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('contribution_date_after', contribution_date_after))
            
        if contribution_date_before is not None:
            if isinstance(contribution_date_before, date):
                _query_params.append(
                    (
                        'contribution_date_before',
                        contribution_date_before.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('contribution_date_before', contribution_date_before))
            
        if contribution_amount_min is not None:
            
            _query_params.append(('contribution_amount_min', contribution_amount_min))
            
        if contribution_amount_max is not None:
            
            _query_params.append(('contribution_amount_max', contribution_amount_max))
            
        if contribution_type is not None:
            
            _query_params.append(('contribution_type', contribution_type))
            
        if contribution_contributor is not None:
            
            _query_params.append(('contribution_contributor', contribution_contributor))
            
        if contribution_payee is not None:
            
            _query_params.append(('contribution_payee', contribution_payee))
            
        if contribution_honoree is not None:
            
            _query_params.append(('contribution_honoree', contribution_honoree))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/contributions/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def retrieve_contribution_report(
        self,
        filing_uuid: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ContributionReport:
        """retrieve_contribution_report

        Returns all contributions matching the provided filters.

        :param filing_uuid:  (required)
        :type filing_uuid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._retrieve_contribution_report_serialize(
            filing_uuid=filing_uuid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContributionReport",
            '400': "Error",
            '401': "Error",
            '404': "Error",
            '405': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def retrieve_contribution_report_with_http_info(
        self,
        filing_uuid: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ContributionReport]:
        """retrieve_contribution_report

        Returns all contributions matching the provided filters.

        :param filing_uuid:  (required)
        :type filing_uuid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._retrieve_contribution_report_serialize(
            filing_uuid=filing_uuid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContributionReport",
            '400': "Error",
            '401': "Error",
            '404': "Error",
            '405': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def retrieve_contribution_report_without_preload_content(
        self,
        filing_uuid: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """retrieve_contribution_report

        Returns all contributions matching the provided filters.

        :param filing_uuid:  (required)
        :type filing_uuid: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._retrieve_contribution_report_serialize(
            filing_uuid=filing_uuid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContributionReport",
            '400': "Error",
            '401': "Error",
            '404': "Error",
            '405': "Error",
            '429': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _retrieve_contribution_report_serialize(
        self,
        filing_uuid,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if filing_uuid is not None:
            _path_params['filing_uuid'] = filing_uuid
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/contributions/{filing_uuid}/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


