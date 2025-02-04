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
from openapi_client.models.filing import Filing
from openapi_client.models.list_filings200_response import ListFilings200Response

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class FilingsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def list_filings(
        self,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        filing_uuid: Annotated[Optional[StrictStr], Field(description="filing_uuid")] = None,
        registrant_id: Annotated[Optional[StrictInt], Field(description="Registrant ID")] = None,
        registrant_name: Annotated[Optional[StrictStr], Field(description="Registrant Name")] = None,
        registrant_country: Annotated[Optional[StrictStr], Field(description="Registrant Country")] = None,
        registrant_ppb_country: Annotated[Optional[StrictStr], Field(description="Registrant PPB Country")] = None,
        client_id: Annotated[Optional[StrictInt], Field(description="Client ID")] = None,
        client_name: Annotated[Optional[StrictStr], Field(description="Client Name")] = None,
        client_state: Annotated[Optional[StrictStr], Field(description="Client State")] = None,
        client_country: Annotated[Optional[StrictStr], Field(description="Client Country")] = None,
        client_ppb_state: Annotated[Optional[StrictStr], Field(description="Client PPB State")] = None,
        client_ppb_country: Annotated[Optional[StrictStr], Field(description="Client PPB Country")] = None,
        lobbyist_id: Annotated[Optional[StrictInt], Field(description="Lobbyist ID")] = None,
        lobbyist_name: Annotated[Optional[StrictStr], Field(description="Lobbyist Name")] = None,
        lobbyist_covered_position: Annotated[Optional[StrictStr], Field(description="Lobbyist Covered Position (Supports Advanced Text Searching)")] = None,
        lobbyist_covered_position_indicator: Annotated[Optional[StrictBool], Field(description="Any Covered Government Position(s)")] = None,
        lobbyist_conviction_disclosure: Annotated[Optional[StrictStr], Field(description="Lobbyist Conviction Description (Supports Advanced Text Searching)")] = None,
        lobbyist_conviction_disclosure_indicator: Annotated[Optional[StrictBool], Field(description="Lobbyist Any Disclosed Conviction(s)")] = None,
        lobbyist_conviction_date_range_after: Annotated[Optional[date], Field(description="Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd")] = None,
        lobbyist_conviction_date_range_before: Annotated[Optional[date], Field(description="Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd")] = None,
        filing_type: Annotated[Optional[StrictStr], Field(description="Filing Type")] = None,
        filing_year: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filing Year")] = None,
        filing_period: Annotated[Optional[StrictStr], Field(description="Filing Period")] = None,
        filing_dt_posted_after: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_dt_posted_before: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_amount_reported_min: Annotated[Optional[StrictStr], Field(description="Filing Amount Reported Range (Min / Max)")] = None,
        filing_amount_reported_max: Annotated[Optional[StrictStr], Field(description="Filing Amount Reported Range (Min / Max)")] = None,
        filing_specific_lobbying_issues: Annotated[Optional[StrictStr], Field(description="Filing Specific Lobbying Issues (Supports Advanced Text Searching)")] = None,
        affiliated_organization_name: Annotated[Optional[StrictStr], Field(description="Affiliated Organization Name")] = None,
        affiliated_organization_country: Annotated[Optional[StrictStr], Field(description="Affiliated Organization Country")] = None,
        affiliated_organization_listed_indicator: Annotated[Optional[StrictBool], Field(description="Any Affiliated Organizations Listed")] = None,
        foreign_entity_name: Annotated[Optional[StrictStr], Field(description="Foreign Entity Name")] = None,
        foreign_entity_country: Annotated[Optional[StrictStr], Field(description="Foreign Entity Country")] = None,
        foreign_entity_listed_indicator: Annotated[Optional[StrictBool], Field(description="Any Foreign Entities Listed")] = None,
        foreign_entity_ppb_country: Annotated[Optional[StrictStr], Field(description="Foreign Entity PPB Country")] = None,
        foreign_entity_ownership_percentage_min: Annotated[Optional[StrictStr], Field(description="Foreign Entity Ownership Percentage")] = None,
        foreign_entity_ownership_percentage_max: Annotated[Optional[StrictStr], Field(description="Foreign Entity Ownership Percentage")] = None,
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
    ) -> ListFilings200Response:
        """list_filings

        

        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param filing_uuid: filing_uuid
        :type filing_uuid: str
        :param registrant_id: Registrant ID
        :type registrant_id: int
        :param registrant_name: Registrant Name
        :type registrant_name: str
        :param registrant_country: Registrant Country
        :type registrant_country: str
        :param registrant_ppb_country: Registrant PPB Country
        :type registrant_ppb_country: str
        :param client_id: Client ID
        :type client_id: int
        :param client_name: Client Name
        :type client_name: str
        :param client_state: Client State
        :type client_state: str
        :param client_country: Client Country
        :type client_country: str
        :param client_ppb_state: Client PPB State
        :type client_ppb_state: str
        :param client_ppb_country: Client PPB Country
        :type client_ppb_country: str
        :param lobbyist_id: Lobbyist ID
        :type lobbyist_id: int
        :param lobbyist_name: Lobbyist Name
        :type lobbyist_name: str
        :param lobbyist_covered_position: Lobbyist Covered Position (Supports Advanced Text Searching)
        :type lobbyist_covered_position: str
        :param lobbyist_covered_position_indicator: Any Covered Government Position(s)
        :type lobbyist_covered_position_indicator: bool
        :param lobbyist_conviction_disclosure: Lobbyist Conviction Description (Supports Advanced Text Searching)
        :type lobbyist_conviction_disclosure: str
        :param lobbyist_conviction_disclosure_indicator: Lobbyist Any Disclosed Conviction(s)
        :type lobbyist_conviction_disclosure_indicator: bool
        :param lobbyist_conviction_date_range_after: Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd
        :type lobbyist_conviction_date_range_after: date
        :param lobbyist_conviction_date_range_before: Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd
        :type lobbyist_conviction_date_range_before: date
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
        :param filing_amount_reported_min: Filing Amount Reported Range (Min / Max)
        :type filing_amount_reported_min: float
        :param filing_amount_reported_max: Filing Amount Reported Range (Min / Max)
        :type filing_amount_reported_max: float
        :param filing_specific_lobbying_issues: Filing Specific Lobbying Issues (Supports Advanced Text Searching)
        :type filing_specific_lobbying_issues: str
        :param affiliated_organization_name: Affiliated Organization Name
        :type affiliated_organization_name: str
        :param affiliated_organization_country: Affiliated Organization Country
        :type affiliated_organization_country: str
        :param affiliated_organization_listed_indicator: Any Affiliated Organizations Listed
        :type affiliated_organization_listed_indicator: bool
        :param foreign_entity_name: Foreign Entity Name
        :type foreign_entity_name: str
        :param foreign_entity_country: Foreign Entity Country
        :type foreign_entity_country: str
        :param foreign_entity_listed_indicator: Any Foreign Entities Listed
        :type foreign_entity_listed_indicator: bool
        :param foreign_entity_ppb_country: Foreign Entity PPB Country
        :type foreign_entity_ppb_country: str
        :param foreign_entity_ownership_percentage_min: Foreign Entity Ownership Percentage
        :type foreign_entity_ownership_percentage_min: str
        :param foreign_entity_ownership_percentage_max: Foreign Entity Ownership Percentage
        :type foreign_entity_ownership_percentage_max: str
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

        _param = self._list_filings_serialize(
            page=page,
            page_size=page_size,
            ordering=ordering,
            filing_uuid=filing_uuid,
            registrant_id=registrant_id,
            registrant_name=registrant_name,
            registrant_country=registrant_country,
            registrant_ppb_country=registrant_ppb_country,
            client_id=client_id,
            client_name=client_name,
            client_state=client_state,
            client_country=client_country,
            client_ppb_state=client_ppb_state,
            client_ppb_country=client_ppb_country,
            lobbyist_id=lobbyist_id,
            lobbyist_name=lobbyist_name,
            lobbyist_covered_position=lobbyist_covered_position,
            lobbyist_covered_position_indicator=lobbyist_covered_position_indicator,
            lobbyist_conviction_disclosure=lobbyist_conviction_disclosure,
            lobbyist_conviction_disclosure_indicator=lobbyist_conviction_disclosure_indicator,
            lobbyist_conviction_date_range_after=lobbyist_conviction_date_range_after,
            lobbyist_conviction_date_range_before=lobbyist_conviction_date_range_before,
            filing_type=filing_type,
            filing_year=filing_year,
            filing_period=filing_period,
            filing_dt_posted_after=filing_dt_posted_after,
            filing_dt_posted_before=filing_dt_posted_before,
            filing_amount_reported_min=filing_amount_reported_min,
            filing_amount_reported_max=filing_amount_reported_max,
            filing_specific_lobbying_issues=filing_specific_lobbying_issues,
            affiliated_organization_name=affiliated_organization_name,
            affiliated_organization_country=affiliated_organization_country,
            affiliated_organization_listed_indicator=affiliated_organization_listed_indicator,
            foreign_entity_name=foreign_entity_name,
            foreign_entity_country=foreign_entity_country,
            foreign_entity_listed_indicator=foreign_entity_listed_indicator,
            foreign_entity_ppb_country=foreign_entity_ppb_country,
            foreign_entity_ownership_percentage_min=foreign_entity_ownership_percentage_min,
            foreign_entity_ownership_percentage_max=foreign_entity_ownership_percentage_max,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListFilings200Response",
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
    def list_filings_with_http_info(
        self,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        filing_uuid: Annotated[Optional[StrictStr], Field(description="filing_uuid")] = None,
        registrant_id: Annotated[Optional[StrictInt], Field(description="Registrant ID")] = None,
        registrant_name: Annotated[Optional[StrictStr], Field(description="Registrant Name")] = None,
        registrant_country: Annotated[Optional[StrictStr], Field(description="Registrant Country")] = None,
        registrant_ppb_country: Annotated[Optional[StrictStr], Field(description="Registrant PPB Country")] = None,
        client_id: Annotated[Optional[StrictInt], Field(description="Client ID")] = None,
        client_name: Annotated[Optional[StrictStr], Field(description="Client Name")] = None,
        client_state: Annotated[Optional[StrictStr], Field(description="Client State")] = None,
        client_country: Annotated[Optional[StrictStr], Field(description="Client Country")] = None,
        client_ppb_state: Annotated[Optional[StrictStr], Field(description="Client PPB State")] = None,
        client_ppb_country: Annotated[Optional[StrictStr], Field(description="Client PPB Country")] = None,
        lobbyist_id: Annotated[Optional[StrictInt], Field(description="Lobbyist ID")] = None,
        lobbyist_name: Annotated[Optional[StrictStr], Field(description="Lobbyist Name")] = None,
        lobbyist_covered_position: Annotated[Optional[StrictStr], Field(description="Lobbyist Covered Position (Supports Advanced Text Searching)")] = None,
        lobbyist_covered_position_indicator: Annotated[Optional[StrictBool], Field(description="Any Covered Government Position(s)")] = None,
        lobbyist_conviction_disclosure: Annotated[Optional[StrictStr], Field(description="Lobbyist Conviction Description (Supports Advanced Text Searching)")] = None,
        lobbyist_conviction_disclosure_indicator: Annotated[Optional[StrictBool], Field(description="Lobbyist Any Disclosed Conviction(s)")] = None,
        lobbyist_conviction_date_range_after: Annotated[Optional[date], Field(description="Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd")] = None,
        lobbyist_conviction_date_range_before: Annotated[Optional[date], Field(description="Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd")] = None,
        filing_type: Annotated[Optional[StrictStr], Field(description="Filing Type")] = None,
        filing_year: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filing Year")] = None,
        filing_period: Annotated[Optional[StrictStr], Field(description="Filing Period")] = None,
        filing_dt_posted_after: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_dt_posted_before: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_amount_reported_min: Annotated[Optional[StrictStr], Field(description="Filing Amount Reported Range (Min / Max)")] = None,
        filing_amount_reported_max: Annotated[Optional[StrictStr], Field(description="Filing Amount Reported Range (Min / Max)")] = None,
        filing_specific_lobbying_issues: Annotated[Optional[StrictStr], Field(description="Filing Specific Lobbying Issues (Supports Advanced Text Searching)")] = None,
        affiliated_organization_name: Annotated[Optional[StrictStr], Field(description="Affiliated Organization Name")] = None,
        affiliated_organization_country: Annotated[Optional[StrictStr], Field(description="Affiliated Organization Country")] = None,
        affiliated_organization_listed_indicator: Annotated[Optional[StrictBool], Field(description="Any Affiliated Organizations Listed")] = None,
        foreign_entity_name: Annotated[Optional[StrictStr], Field(description="Foreign Entity Name")] = None,
        foreign_entity_country: Annotated[Optional[StrictStr], Field(description="Foreign Entity Country")] = None,
        foreign_entity_listed_indicator: Annotated[Optional[StrictBool], Field(description="Any Foreign Entities Listed")] = None,
        foreign_entity_ppb_country: Annotated[Optional[StrictStr], Field(description="Foreign Entity PPB Country")] = None,
        foreign_entity_ownership_percentage_min: Annotated[Optional[StrictStr], Field(description="Foreign Entity Ownership Percentage")] = None,
        foreign_entity_ownership_percentage_max: Annotated[Optional[StrictStr], Field(description="Foreign Entity Ownership Percentage")] = None,
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
    ) -> ApiResponse[ListFilings200Response]:
        """list_filings

        

        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param filing_uuid: filing_uuid
        :type filing_uuid: str
        :param registrant_id: Registrant ID
        :type registrant_id: int
        :param registrant_name: Registrant Name
        :type registrant_name: str
        :param registrant_country: Registrant Country
        :type registrant_country: str
        :param registrant_ppb_country: Registrant PPB Country
        :type registrant_ppb_country: str
        :param client_id: Client ID
        :type client_id: int
        :param client_name: Client Name
        :type client_name: str
        :param client_state: Client State
        :type client_state: str
        :param client_country: Client Country
        :type client_country: str
        :param client_ppb_state: Client PPB State
        :type client_ppb_state: str
        :param client_ppb_country: Client PPB Country
        :type client_ppb_country: str
        :param lobbyist_id: Lobbyist ID
        :type lobbyist_id: int
        :param lobbyist_name: Lobbyist Name
        :type lobbyist_name: str
        :param lobbyist_covered_position: Lobbyist Covered Position (Supports Advanced Text Searching)
        :type lobbyist_covered_position: str
        :param lobbyist_covered_position_indicator: Any Covered Government Position(s)
        :type lobbyist_covered_position_indicator: bool
        :param lobbyist_conviction_disclosure: Lobbyist Conviction Description (Supports Advanced Text Searching)
        :type lobbyist_conviction_disclosure: str
        :param lobbyist_conviction_disclosure_indicator: Lobbyist Any Disclosed Conviction(s)
        :type lobbyist_conviction_disclosure_indicator: bool
        :param lobbyist_conviction_date_range_after: Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd
        :type lobbyist_conviction_date_range_after: date
        :param lobbyist_conviction_date_range_before: Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd
        :type lobbyist_conviction_date_range_before: date
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
        :param filing_amount_reported_min: Filing Amount Reported Range (Min / Max)
        :type filing_amount_reported_min: float
        :param filing_amount_reported_max: Filing Amount Reported Range (Min / Max)
        :type filing_amount_reported_max: float
        :param filing_specific_lobbying_issues: Filing Specific Lobbying Issues (Supports Advanced Text Searching)
        :type filing_specific_lobbying_issues: str
        :param affiliated_organization_name: Affiliated Organization Name
        :type affiliated_organization_name: str
        :param affiliated_organization_country: Affiliated Organization Country
        :type affiliated_organization_country: str
        :param affiliated_organization_listed_indicator: Any Affiliated Organizations Listed
        :type affiliated_organization_listed_indicator: bool
        :param foreign_entity_name: Foreign Entity Name
        :type foreign_entity_name: str
        :param foreign_entity_country: Foreign Entity Country
        :type foreign_entity_country: str
        :param foreign_entity_listed_indicator: Any Foreign Entities Listed
        :type foreign_entity_listed_indicator: bool
        :param foreign_entity_ppb_country: Foreign Entity PPB Country
        :type foreign_entity_ppb_country: str
        :param foreign_entity_ownership_percentage_min: Foreign Entity Ownership Percentage
        :type foreign_entity_ownership_percentage_min: str
        :param foreign_entity_ownership_percentage_max: Foreign Entity Ownership Percentage
        :type foreign_entity_ownership_percentage_max: str
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

        _param = self._list_filings_serialize(
            page=page,
            page_size=page_size,
            ordering=ordering,
            filing_uuid=filing_uuid,
            registrant_id=registrant_id,
            registrant_name=registrant_name,
            registrant_country=registrant_country,
            registrant_ppb_country=registrant_ppb_country,
            client_id=client_id,
            client_name=client_name,
            client_state=client_state,
            client_country=client_country,
            client_ppb_state=client_ppb_state,
            client_ppb_country=client_ppb_country,
            lobbyist_id=lobbyist_id,
            lobbyist_name=lobbyist_name,
            lobbyist_covered_position=lobbyist_covered_position,
            lobbyist_covered_position_indicator=lobbyist_covered_position_indicator,
            lobbyist_conviction_disclosure=lobbyist_conviction_disclosure,
            lobbyist_conviction_disclosure_indicator=lobbyist_conviction_disclosure_indicator,
            lobbyist_conviction_date_range_after=lobbyist_conviction_date_range_after,
            lobbyist_conviction_date_range_before=lobbyist_conviction_date_range_before,
            filing_type=filing_type,
            filing_year=filing_year,
            filing_period=filing_period,
            filing_dt_posted_after=filing_dt_posted_after,
            filing_dt_posted_before=filing_dt_posted_before,
            filing_amount_reported_min=filing_amount_reported_min,
            filing_amount_reported_max=filing_amount_reported_max,
            filing_specific_lobbying_issues=filing_specific_lobbying_issues,
            affiliated_organization_name=affiliated_organization_name,
            affiliated_organization_country=affiliated_organization_country,
            affiliated_organization_listed_indicator=affiliated_organization_listed_indicator,
            foreign_entity_name=foreign_entity_name,
            foreign_entity_country=foreign_entity_country,
            foreign_entity_listed_indicator=foreign_entity_listed_indicator,
            foreign_entity_ppb_country=foreign_entity_ppb_country,
            foreign_entity_ownership_percentage_min=foreign_entity_ownership_percentage_min,
            foreign_entity_ownership_percentage_max=foreign_entity_ownership_percentage_max,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListFilings200Response",
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
    def list_filings_without_preload_content(
        self,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        ordering: Annotated[Optional[StrictStr], Field(description="Which field to use when ordering the results.")] = None,
        filing_uuid: Annotated[Optional[StrictStr], Field(description="filing_uuid")] = None,
        registrant_id: Annotated[Optional[StrictInt], Field(description="Registrant ID")] = None,
        registrant_name: Annotated[Optional[StrictStr], Field(description="Registrant Name")] = None,
        registrant_country: Annotated[Optional[StrictStr], Field(description="Registrant Country")] = None,
        registrant_ppb_country: Annotated[Optional[StrictStr], Field(description="Registrant PPB Country")] = None,
        client_id: Annotated[Optional[StrictInt], Field(description="Client ID")] = None,
        client_name: Annotated[Optional[StrictStr], Field(description="Client Name")] = None,
        client_state: Annotated[Optional[StrictStr], Field(description="Client State")] = None,
        client_country: Annotated[Optional[StrictStr], Field(description="Client Country")] = None,
        client_ppb_state: Annotated[Optional[StrictStr], Field(description="Client PPB State")] = None,
        client_ppb_country: Annotated[Optional[StrictStr], Field(description="Client PPB Country")] = None,
        lobbyist_id: Annotated[Optional[StrictInt], Field(description="Lobbyist ID")] = None,
        lobbyist_name: Annotated[Optional[StrictStr], Field(description="Lobbyist Name")] = None,
        lobbyist_covered_position: Annotated[Optional[StrictStr], Field(description="Lobbyist Covered Position (Supports Advanced Text Searching)")] = None,
        lobbyist_covered_position_indicator: Annotated[Optional[StrictBool], Field(description="Any Covered Government Position(s)")] = None,
        lobbyist_conviction_disclosure: Annotated[Optional[StrictStr], Field(description="Lobbyist Conviction Description (Supports Advanced Text Searching)")] = None,
        lobbyist_conviction_disclosure_indicator: Annotated[Optional[StrictBool], Field(description="Lobbyist Any Disclosed Conviction(s)")] = None,
        lobbyist_conviction_date_range_after: Annotated[Optional[date], Field(description="Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd")] = None,
        lobbyist_conviction_date_range_before: Annotated[Optional[date], Field(description="Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd")] = None,
        filing_type: Annotated[Optional[StrictStr], Field(description="Filing Type")] = None,
        filing_year: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filing Year")] = None,
        filing_period: Annotated[Optional[StrictStr], Field(description="Filing Period")] = None,
        filing_dt_posted_after: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_dt_posted_before: Annotated[Optional[datetime], Field(description="Filing Date Posted Range (Before / After): yyyy-mm-dd")] = None,
        filing_amount_reported_min: Annotated[Optional[StrictStr], Field(description="Filing Amount Reported Range (Min / Max)")] = None,
        filing_amount_reported_max: Annotated[Optional[StrictStr], Field(description="Filing Amount Reported Range (Min / Max)")] = None,
        filing_specific_lobbying_issues: Annotated[Optional[StrictStr], Field(description="Filing Specific Lobbying Issues (Supports Advanced Text Searching)")] = None,
        affiliated_organization_name: Annotated[Optional[StrictStr], Field(description="Affiliated Organization Name")] = None,
        affiliated_organization_country: Annotated[Optional[StrictStr], Field(description="Affiliated Organization Country")] = None,
        affiliated_organization_listed_indicator: Annotated[Optional[StrictBool], Field(description="Any Affiliated Organizations Listed")] = None,
        foreign_entity_name: Annotated[Optional[StrictStr], Field(description="Foreign Entity Name")] = None,
        foreign_entity_country: Annotated[Optional[StrictStr], Field(description="Foreign Entity Country")] = None,
        foreign_entity_listed_indicator: Annotated[Optional[StrictBool], Field(description="Any Foreign Entities Listed")] = None,
        foreign_entity_ppb_country: Annotated[Optional[StrictStr], Field(description="Foreign Entity PPB Country")] = None,
        foreign_entity_ownership_percentage_min: Annotated[Optional[StrictStr], Field(description="Foreign Entity Ownership Percentage")] = None,
        foreign_entity_ownership_percentage_max: Annotated[Optional[StrictStr], Field(description="Foreign Entity Ownership Percentage")] = None,
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
        """list_filings

        

        :param page: A page number within the paginated result set.
        :type page: int
        :param page_size: Number of results to return per page.
        :type page_size: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param filing_uuid: filing_uuid
        :type filing_uuid: str
        :param registrant_id: Registrant ID
        :type registrant_id: int
        :param registrant_name: Registrant Name
        :type registrant_name: str
        :param registrant_country: Registrant Country
        :type registrant_country: str
        :param registrant_ppb_country: Registrant PPB Country
        :type registrant_ppb_country: str
        :param client_id: Client ID
        :type client_id: int
        :param client_name: Client Name
        :type client_name: str
        :param client_state: Client State
        :type client_state: str
        :param client_country: Client Country
        :type client_country: str
        :param client_ppb_state: Client PPB State
        :type client_ppb_state: str
        :param client_ppb_country: Client PPB Country
        :type client_ppb_country: str
        :param lobbyist_id: Lobbyist ID
        :type lobbyist_id: int
        :param lobbyist_name: Lobbyist Name
        :type lobbyist_name: str
        :param lobbyist_covered_position: Lobbyist Covered Position (Supports Advanced Text Searching)
        :type lobbyist_covered_position: str
        :param lobbyist_covered_position_indicator: Any Covered Government Position(s)
        :type lobbyist_covered_position_indicator: bool
        :param lobbyist_conviction_disclosure: Lobbyist Conviction Description (Supports Advanced Text Searching)
        :type lobbyist_conviction_disclosure: str
        :param lobbyist_conviction_disclosure_indicator: Lobbyist Any Disclosed Conviction(s)
        :type lobbyist_conviction_disclosure_indicator: bool
        :param lobbyist_conviction_date_range_after: Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd
        :type lobbyist_conviction_date_range_after: date
        :param lobbyist_conviction_date_range_before: Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd
        :type lobbyist_conviction_date_range_before: date
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
        :param filing_amount_reported_min: Filing Amount Reported Range (Min / Max)
        :type filing_amount_reported_min: float
        :param filing_amount_reported_max: Filing Amount Reported Range (Min / Max)
        :type filing_amount_reported_max: float
        :param filing_specific_lobbying_issues: Filing Specific Lobbying Issues (Supports Advanced Text Searching)
        :type filing_specific_lobbying_issues: str
        :param affiliated_organization_name: Affiliated Organization Name
        :type affiliated_organization_name: str
        :param affiliated_organization_country: Affiliated Organization Country
        :type affiliated_organization_country: str
        :param affiliated_organization_listed_indicator: Any Affiliated Organizations Listed
        :type affiliated_organization_listed_indicator: bool
        :param foreign_entity_name: Foreign Entity Name
        :type foreign_entity_name: str
        :param foreign_entity_country: Foreign Entity Country
        :type foreign_entity_country: str
        :param foreign_entity_listed_indicator: Any Foreign Entities Listed
        :type foreign_entity_listed_indicator: bool
        :param foreign_entity_ppb_country: Foreign Entity PPB Country
        :type foreign_entity_ppb_country: str
        :param foreign_entity_ownership_percentage_min: Foreign Entity Ownership Percentage
        :type foreign_entity_ownership_percentage_min: str
        :param foreign_entity_ownership_percentage_max: Foreign Entity Ownership Percentage
        :type foreign_entity_ownership_percentage_max: str
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

        _param = self._list_filings_serialize(
            page=page,
            page_size=page_size,
            ordering=ordering,
            filing_uuid=filing_uuid,
            registrant_id=registrant_id,
            registrant_name=registrant_name,
            registrant_country=registrant_country,
            registrant_ppb_country=registrant_ppb_country,
            client_id=client_id,
            client_name=client_name,
            client_state=client_state,
            client_country=client_country,
            client_ppb_state=client_ppb_state,
            client_ppb_country=client_ppb_country,
            lobbyist_id=lobbyist_id,
            lobbyist_name=lobbyist_name,
            lobbyist_covered_position=lobbyist_covered_position,
            lobbyist_covered_position_indicator=lobbyist_covered_position_indicator,
            lobbyist_conviction_disclosure=lobbyist_conviction_disclosure,
            lobbyist_conviction_disclosure_indicator=lobbyist_conviction_disclosure_indicator,
            lobbyist_conviction_date_range_after=lobbyist_conviction_date_range_after,
            lobbyist_conviction_date_range_before=lobbyist_conviction_date_range_before,
            filing_type=filing_type,
            filing_year=filing_year,
            filing_period=filing_period,
            filing_dt_posted_after=filing_dt_posted_after,
            filing_dt_posted_before=filing_dt_posted_before,
            filing_amount_reported_min=filing_amount_reported_min,
            filing_amount_reported_max=filing_amount_reported_max,
            filing_specific_lobbying_issues=filing_specific_lobbying_issues,
            affiliated_organization_name=affiliated_organization_name,
            affiliated_organization_country=affiliated_organization_country,
            affiliated_organization_listed_indicator=affiliated_organization_listed_indicator,
            foreign_entity_name=foreign_entity_name,
            foreign_entity_country=foreign_entity_country,
            foreign_entity_listed_indicator=foreign_entity_listed_indicator,
            foreign_entity_ppb_country=foreign_entity_ppb_country,
            foreign_entity_ownership_percentage_min=foreign_entity_ownership_percentage_min,
            foreign_entity_ownership_percentage_max=foreign_entity_ownership_percentage_max,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListFilings200Response",
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


    def _list_filings_serialize(
        self,
        page,
        page_size,
        ordering,
        filing_uuid,
        registrant_id,
        registrant_name,
        registrant_country,
        registrant_ppb_country,
        client_id,
        client_name,
        client_state,
        client_country,
        client_ppb_state,
        client_ppb_country,
        lobbyist_id,
        lobbyist_name,
        lobbyist_covered_position,
        lobbyist_covered_position_indicator,
        lobbyist_conviction_disclosure,
        lobbyist_conviction_disclosure_indicator,
        lobbyist_conviction_date_range_after,
        lobbyist_conviction_date_range_before,
        filing_type,
        filing_year,
        filing_period,
        filing_dt_posted_after,
        filing_dt_posted_before,
        filing_amount_reported_min,
        filing_amount_reported_max,
        filing_specific_lobbying_issues,
        affiliated_organization_name,
        affiliated_organization_country,
        affiliated_organization_listed_indicator,
        foreign_entity_name,
        foreign_entity_country,
        foreign_entity_listed_indicator,
        foreign_entity_ppb_country,
        foreign_entity_ownership_percentage_min,
        foreign_entity_ownership_percentage_max,
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
            
        if registrant_id is not None:
            
            _query_params.append(('registrant_id', registrant_id))
            
        if registrant_name is not None:
            
            _query_params.append(('registrant_name', registrant_name))
            
        if registrant_country is not None:
            
            _query_params.append(('registrant_country', registrant_country))
            
        if registrant_ppb_country is not None:
            
            _query_params.append(('registrant_ppb_country', registrant_ppb_country))
            
        if client_id is not None:
            
            _query_params.append(('client_id', client_id))
            
        if client_name is not None:
            
            _query_params.append(('client_name', client_name))
            
        if client_state is not None:
            
            _query_params.append(('client_state', client_state))
            
        if client_country is not None:
            
            _query_params.append(('client_country', client_country))
            
        if client_ppb_state is not None:
            
            _query_params.append(('client_ppb_state', client_ppb_state))
            
        if client_ppb_country is not None:
            
            _query_params.append(('client_ppb_country', client_ppb_country))
            
        if lobbyist_id is not None:
            
            _query_params.append(('lobbyist_id', lobbyist_id))
            
        if lobbyist_name is not None:
            
            _query_params.append(('lobbyist_name', lobbyist_name))
            
        if lobbyist_covered_position is not None:
            
            _query_params.append(('lobbyist_covered_position', lobbyist_covered_position))
            
        if lobbyist_covered_position_indicator is not None:
            
            _query_params.append(('lobbyist_covered_position_indicator', lobbyist_covered_position_indicator))
            
        if lobbyist_conviction_disclosure is not None:
            
            _query_params.append(('lobbyist_conviction_disclosure', lobbyist_conviction_disclosure))
            
        if lobbyist_conviction_disclosure_indicator is not None:
            
            _query_params.append(('lobbyist_conviction_disclosure_indicator', lobbyist_conviction_disclosure_indicator))
            
        if lobbyist_conviction_date_range_after is not None:
            if isinstance(lobbyist_conviction_date_range_after, date):
                _query_params.append(
                    (
                        'lobbyist_conviction_date_range_after',
                        lobbyist_conviction_date_range_after.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('lobbyist_conviction_date_range_after', lobbyist_conviction_date_range_after))
            
        if lobbyist_conviction_date_range_before is not None:
            if isinstance(lobbyist_conviction_date_range_before, date):
                _query_params.append(
                    (
                        'lobbyist_conviction_date_range_before',
                        lobbyist_conviction_date_range_before.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('lobbyist_conviction_date_range_before', lobbyist_conviction_date_range_before))
            
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
            
        if filing_amount_reported_min is not None:
            
            _query_params.append(('filing_amount_reported_min', filing_amount_reported_min))
            
        if filing_amount_reported_max is not None:
            
            _query_params.append(('filing_amount_reported_max', filing_amount_reported_max))
            
        if filing_specific_lobbying_issues is not None:
            
            _query_params.append(('filing_specific_lobbying_issues', filing_specific_lobbying_issues))
            
        if affiliated_organization_name is not None:
            
            _query_params.append(('affiliated_organization_name', affiliated_organization_name))
            
        if affiliated_organization_country is not None:
            
            _query_params.append(('affiliated_organization_country', affiliated_organization_country))
            
        if affiliated_organization_listed_indicator is not None:
            
            _query_params.append(('affiliated_organization_listed_indicator', affiliated_organization_listed_indicator))
            
        if foreign_entity_name is not None:
            
            _query_params.append(('foreign_entity_name', foreign_entity_name))
            
        if foreign_entity_country is not None:
            
            _query_params.append(('foreign_entity_country', foreign_entity_country))
            
        if foreign_entity_listed_indicator is not None:
            
            _query_params.append(('foreign_entity_listed_indicator', foreign_entity_listed_indicator))
            
        if foreign_entity_ppb_country is not None:
            
            _query_params.append(('foreign_entity_ppb_country', foreign_entity_ppb_country))
            
        if foreign_entity_ownership_percentage_min is not None:
            
            _query_params.append(('foreign_entity_ownership_percentage_min', foreign_entity_ownership_percentage_min))
            
        if foreign_entity_ownership_percentage_max is not None:
            
            _query_params.append(('foreign_entity_ownership_percentage_max', foreign_entity_ownership_percentage_max))
            
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
            resource_path='/api/v1/filings/',
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
    def retrieve_filing(
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
    ) -> Filing:
        """retrieve_filing

        Returns all filings matching the provided filters.

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

        _param = self._retrieve_filing_serialize(
            filing_uuid=filing_uuid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Filing",
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
    def retrieve_filing_with_http_info(
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
    ) -> ApiResponse[Filing]:
        """retrieve_filing

        Returns all filings matching the provided filters.

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

        _param = self._retrieve_filing_serialize(
            filing_uuid=filing_uuid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Filing",
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
    def retrieve_filing_without_preload_content(
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
        """retrieve_filing

        Returns all filings matching the provided filters.

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

        _param = self._retrieve_filing_serialize(
            filing_uuid=filing_uuid,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Filing",
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


    def _retrieve_filing_serialize(
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
            resource_path='/api/v1/filings/{filing_uuid}/',
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

    def get_filing(self, filing_uuid):
        """Retrieve detailed information about a specific filing by its UUID."""
        endpoint = f"/api/v1/filings/{filing_uuid}/"
        response = self.api_client.call_api(endpoint, 'GET')
        return response


