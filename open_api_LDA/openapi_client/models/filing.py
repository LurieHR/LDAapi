# coding: utf-8

"""
    Lobbying Disclosure

    # About the REST API  ## Introduction  This document describes the resources that make up the official Lobbying Disclosure REST API v1. If you have any  issues, please contact the Senate Office of Public Records (OPR) at [lobby@sec.senate.gov](mailto:lobby@sec.senate.gov). OPR does not offer development advice and does not provide language specific guides. The REST API is programming  language agnostic. Any programming language can be used to make REST API requests to retrieve data.  The REST API is documented in the **OpenAPI format** which can be found by clicking the \"Download\" button at the top  of the page. In addition to the standard OpenAPI syntax, we use a few  [vendor extensions](https://github.com/Redocly/redoc/blob/master/docs/redoc-vendor-extensions.md). There are a  variety of open source and proprietary tools that can read OpenAPI specifications and interact with the API by reading  the published specification. OPR does not recommend any specific OpenAPI tools.  ## Terms of Service  REST API is governed by a [Terms of Service](https://lda.senate.gov/api/tos/).  ## Changes  | Date | Description | | ------ | ------ | | 05/09/2024 | Clarified documentation on: date format when filtering results (yyyy-mm-dd) and constants information. | | 01/18/2024 | Added limitations / caveats section | | 08/08/2023 | Change request throttle rates from by hour to by minute to reduce burstable requests. New request throttles: unauthenticated (anon): 15/minute (900/hour), API key (registered): 120/minute (7,200/hour) | | 04/05/2023 | Added requirements to use at least one query string parameter value when paginating results for `Filings` and `Contribution Reports`. See warnings in [Pagination](#section/Implementation-Details/Pagination) for more information. | | 04/05/2023 | Removed ordering filters for performance reasons. Filing: `id`; Contribution Report: `id`; Client: `registrant_name`; Lobbyist: all but `id` | | 12/14/2022 | Added registrant address fields as indicated on the latest LD1 / LD2 filing to the filing endpoint. | | 03/28/2022 | Fixed an issue where LD2 filings posted from 2/15/2022 to 3/28/2022 did not display income or expenses. | | 01/24/2022 | Added Advanced Text Searching in Filing endpoint on fields: `filing_specific_lobbying_issues`, `lobbyist_conviction_disclosure`, and `lobbyist_covered_position`. | | 01/13/2022 | Fixed an issue where the list of Contribution Items in Contribution Reports (LD-203) endpoint did not match the filed Contribution Report document. | | 07/30/2021 | Added Lobbyist endpoint | | 03/10/2021 | Decreased pagination to 25. Increased request throttle rates: unauthenticated (anon): 1,000/hour, API key (registered): 20,000/hour |   ## Schema  All REST API access is over HTTPS, and accessed from `https://lda.senate.gov/api/v1/`. All data is sent and received as JSON.  Testing can be done through [human browseable API interface](https://lda.senate.gov/api/v1/) where it is possible to make  requests with filtering/ordering and pagination.  Blank fields are included as `null` instead of being omitted.  All timestamps return in ISO 8601 format:  ```text YYYY-MM-DDTHH:MM:SSZ ```  ## Root Endpoint  Sending a request with `GET` to the root endpoint will return all the endpoint categories that the REST API v1  supports:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/ ```  **Reponse:**  ```http request HTTP 200 OK Allow: GET, HEAD, OPTIONS Content-Type: application/json Vary: Accept  {     \"filings\": \"https://lda.senate.gov/api/v1/filings/\",     \"contributions\": \"https://lda.senate.gov/api/v1/contributions/\",     \"registrants\": \"https://lda.senate.gov/api/v1/registrants/\",     \"clients\": \"https://lda.senate.gov/api/v1/clients/\",     \"lobbyists\": \"https://lda.senate.gov/api/v1/lobbyists/\",     \"constants/filing/filingtypes\": \"https://lda.senate.gov/api/v1/constants/filing/filingtypes/\",     \"constants/filing/lobbyingactivityissues\": \"https://lda.senate.gov/api/v1/constants/filing/lobbyingactivityissues/\",     \"constants/filing/governmententities\": \"https://lda.senate.gov/api/v1/constants/filing/governmententities/\",     \"constants/general/countries\": \"https://lda.senate.gov/api/v1/constants/general/countries/\",     \"constants/general/states\": \"https://lda.senate.gov/api/v1/constants/general/states/\",     \"constants/lobbyist/prefixes\": \"https://lda.senate.gov/api/v1/constants/lobbyist/prefixes/\",     \"constants/lobbyist/suffixes\": \"https://lda.senate.gov/api/v1/constants/lobbyist/suffixes/\" } ```  ## Browsable API  APIs may be for machines to access, but humans have to be able to read APIS as well. We support a human-friendly  HTML output when `HTML` format is requested where it is possible to make requests with filtering/ordering and  pagination.  [View the HTML API output](https://lda.senate.gov/api/v1/).  ## Constants  Lists of key / value constants are published for the following fields:  * Filing Types * Lobbying Activity Issues * Government Entities * Countries * States (US States) * Prefixes (e.g. Mr., Ms., Mx., Dr., etc.) * Suffixes (e.g. Sr., Jr., II, etc.)  These endpoints are periodically updated when new key / values are added. Please see the API [Constants](#tag/Constants) section section of this documenation for more information.  # Authentication   There are two ways to authenticate through the REST API. Our API offers two types of authentication:  * API Key (Registered) * Unauthenticated (Anonymous)  For clients to authenticate using an API Key, the token key must be included in the `Authorization` HTTP header and  **must** be prefixed by the string literal \"Token\", with whitespace separating the two strings. For example:  ```http request Authorization: Token z944b09199c62bcf9418ad846dd0e4bbdfc6ee4b ```  For clients without an API Key, no special authentication is required, however anonymous clients are subject to  more strict request throttling.  <schema-definitions />   ## Register and Obtain an API Key  [Register](https://lda.senate.gov/api/register/) by using our automated system. After registering, you can obtain an API key  using one of these methods:  * Via a [web form](https://lda.senate.gov/api/auth/login/) * Via an API call (Make a `POST` with your `username` and `password` login credentials as form data or JSON.)  The response will contain your API key if properly authenticated.  **Request:**  ```http request POST https://lda.senate.gov/api/auth/login/  {     \"username\": \"your_username\",     \"password\": \"your_password\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"key\": \"z944b09199c62bcf9418ad846dd0e4bbdfc6ee4b\" } ```  ## Reset Forgotten Password  If you have forgotten your password or need to change it, you can reset your password using one of these methods:  * Via a [web form](https://lda.senate.gov/api/auth/password/reset/) * Via an API call (Make a `POST` with your `email` as form data or JSON.)  **Request:**  ```http request POST https://lda.senate.gov/api/auth/password/reset/  {     \"email\": \"your_email_address\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"detail\": \"Password reset e-mail has been sent.\" } ```  If successful, you will receive email with a `uid` and `token` to reset your password which can be done using one of  these methods:  * Via a [web form](https://lda.senate.gov/api/auth/password/reset/confirm/) * Via an API call (Make a `POST` with you `new_password1` and `new_password2` with the `uid`, and `token` from your  email  as form data or JSON.)  **Request:**  ```http request POST https://lda.senate.gov/api/auth/password/reset/confirm/  {     \"new_password1\": \"new_password\",     \"new_password2\": \"new_password\",     \"uid\": \"UID from your email\",     \"token\": \"Token from your email\" } ```  **Response:**  ```http request HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept  {     \"detail\": \"Password reset e-mail has been sent.\" } ```  # Implementation Details  ## Request Throttling  All REST API requests are throttled to prevent abuse and to ensure stability. Our API is  rate limited depending the type of authentication option you choose:  * API Key (Registered): 120/minute * Unauthenticated (Anonymous): 15/minute  Unauthenticated requests are rate limited by the originating IP address and not the user making requests.  Authenticated requests share the same user quota regardless of whether multiple API keys are used.   Requests made for the following items do not count towards rate limits:  * Original HTML and PDF documents at:   * `https://lda.senate.gov/filings/public/filing/{filing_uuid}/print/`   * `https://lda.senate.gov/filings/public/contribution/{filing_uuid}/print/` * Constants at all URLs starting with `https://lda.senate.gov/api/v1/constants/*`  Requests that exceed the throttling rate for your authentication type will received an HTTP 429 `Too Many Requests`  response. The `Retry-After` header in the response will indicate the number of seconds to wait.  **Response:**  ```http request HTTP 429 Too Many Requests Allow: GET Content-Type: application/json Retry-After: 1596 Vary: Accept  {     \"detail\": \"Request was throttled. Expected available in 1596 seconds.\" } ```  ## Pagination  Large result sets are split into individual pages of data. The pagination links are provided as part of the content  of the response via the `next` and `previous` keys in the response. You can control which page to request by using  the `page` query string parameter.  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?page=2 ```  **Response:**  ```http request HTTP 200 OK  {     \"count\": 1023     \"next\": \"https://lda.senate.gov/api/v1/filings/?page=1\",     \"previous\": \"https://lda.senate.gov/api/v1/filings/?page=3\",     \"results\": [        …     ] } ```  By default, each page is limited to 25 results per page. You may set the page size by setting `page_size`  as a query string parameter up to 25.  **Warning**  The `Filings` and `Contribution Reports` endpoints require at least one queryset parameter to be passed in order to paginate results beyond the first page.  This is for performance reasons.  If you would like to paginate through all `Filings`, we recommend paginating through the results by filing year. Below  shows an example of getting page 2 of results for filing year 2023 for `Filings`.  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=2 ```  **Response:**  ```http request HTTP 200 OK  {     \"count\": 1023     \"next\": \"https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=1\",     \"previous\": \"https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=3\",     \"results\": [        …     ] } ```  ## Ordering  Result sets can be ordered by using the `ordering` query string parameter. Each endpoint has its own set of fields you  can order by so see the available ordering in the [browseable API interface](https://lda.senate.gov/api/v1/) under the \"Filters\"  button in the upper right corner of the interface.  For example, to order filings by `dt_posted`:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=dt_posted ```  The client may also specify reverse orderings by prefixing the field name with `-`, like so:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=-dt_posted ```  Multiple orderings may also be specified:  ```http request GET https://lda.senate.gov/api/v1/filings/?ordering=dt_posted,registrant__name ```  ## Advanced Text Searching  - **Unquoted Text** - Text not inside quote marks will not be treated as a phrase. Text separated by a space is treated as an OR operator between them. _Estate Tax_ will match _estate_ OR _tax_ even if they do appear next to each other. - **&quot;Quoted Text&quot;** - Text inside double quote marks will be treated as a phrase. _Estate Tax_ will match the phrase _estate tax_ but will not match the words _estate_ or _tax_ if they appear separately. - **OR** - The word _OR_ will be treated as a true OR operator. _&quot;Estate Tax&quot; OR &quot;Estate Taxes&quot;_ will match the phrases _estate tax_or _estate taxes_ but will not match the words _estate_ or _tax_ if they appear separately. - **-** The dash character _-_ will be treated as a NOT EQUALS operator. _&quot;Estate Tax&quot; -&quot;Payroll Taxes&quot;_ will match the phrase _estate tax_ but not _payroll taxes_ if they appear in the same field.  ## Limitations / Caveats  - **Government Entities** - Filings that posted before 2/14/2021 do not have government entities broken down by each individual lobbying activity area. Instead, the government entities listed on these filings is a list of entities that appear on the filing as a whole. This limitation is due to data imported from a legacy system. Filings that posted after 2/14/2021 will have government entities broken down by each individual lobbying activity area.  # Common Errors  ## Invalid API Key  If you supply an invalid API Key, you will receive an HTTP 401 `Unauthorized` response:  **Response:**  ```http request HTTP 401 UNAUTHORIZED  {     \"detail\": \"Invalid token.\" } ```  ## Request Throttled  If you exceed your rate limit for your authentication type, you will receive an HTTP 429 `Too Many Requests`  response. See the [Request Throttling](#section/Implementation-Details/Request-Throttling) section for more information.  **Response:**  ```http request HTTP 429 Too Many Requests Allow: GET Content-Type: application/json Retry-After: 1596 Vary: Accept  {     \"detail\": \"Request was throttled. Expected available in 1596 seconds.\" } ```  ## Invalid Query String Parameter Values  If you pass invalid query string parameter values, you will likely receive an HTTP 404 `Not Found` or HTTP 400  `Bad Request` response with a detailed error message.  For example, passing a non-integer for the page number:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?page=a ```  **Response:**  ```http request HTTP 404 Not Found Allow: GET Content-Type: application/json Vary: Accept  {     \"detail\": \"Invalid page.\" } ```  For example, passing an invalid value for the Registrant ID:  **Request:**  ```http request GET https://lda.senate.gov/api/v1/filings/?registrant_id=a ```  **Response:**  ```http request HTTP 400 Bad Request Allow: GET Content-Type: application/json Vary: Accept  {     \"registrant_id\": [         \"Enter a number.\"     ] } ```  ## Unsupported HTTP Method  If you use an unsupported HTTP method, you will receive an HTTP 405 `Method Not Allowed` response:  ```http request DELETE https://lda.senate.gov/api/v1/filings/ Accept: application/json ```  **Response:**  ```http request HTTP 405 Method Not Allowed Content-Type: application/json Content-Length: 42  {     \"detail\": \"Method \\\"DELETE\\\" not allowed.\" } ```  ## Query String Filters Required for Pagination  If you use paginated results and do not include at least one query string parameter filter, you will receive an HTTP 400 `Bad Request` response:  ```http request GET https://lda.senate.gov/api/v1/filings/?page=2 ```  **Response:**  ```http request HTTP 400 Bad Request Allow: GET Content-Type: application/json Vary: Accept  {    \"detail\": \"You must pass at least one query string parameter to filter the results and be able to paginate the results.\" } ```  See warnings in [Pagination](#section/Implementation-Details/Pagination) for more information.

    The version of the OpenAPI document: 1.0.0
    Contact: lobby@sec.senate.gov
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.filing_affiliated_organizations_inner import FilingAffiliatedOrganizationsInner
from openapi_client.models.filing_client import FilingClient
from openapi_client.models.filing_conviction_disclosures_inner import FilingConvictionDisclosuresInner
from openapi_client.models.filing_foreign_entities_inner import FilingForeignEntitiesInner
from openapi_client.models.filing_lobbying_activities_inner import FilingLobbyingActivitiesInner
from openapi_client.models.filing_registrant import FilingRegistrant
from typing import Optional, Set
from typing_extensions import Self

class Filing(BaseModel):
    """
    Filing
    """ # noqa: E501
    url: Optional[StrictStr] = None
    filing_uuid: Optional[StrictStr] = None
    filing_type: Optional[StrictStr] = None
    filing_type_display: Optional[StrictStr] = None
    filing_year: Optional[StrictInt] = None
    filing_period: Optional[StrictStr] = Field(default=None, description="Filing Period - Quarter")
    filing_period_display: Optional[StrictStr] = None
    filing_document_url: Optional[StrictStr] = None
    filing_document_content_type: Optional[StrictStr] = None
    income: Optional[Annotated[str, Field(strict=True)]] = None
    expenses: Optional[Annotated[str, Field(strict=True)]] = None
    expenses_method: Optional[StrictStr] = None
    expenses_method_display: Optional[StrictStr] = None
    posted_by_name: Optional[StrictStr] = None
    dt_posted: Optional[datetime] = None
    termination_date: Optional[date] = None
    registrant_country: Optional[StrictStr] = None
    registrant_ppb_country: Optional[StrictStr] = None
    registrant_address_1: Optional[StrictStr] = Field(default=None, description="As listed on filing - Registrant Address 1")
    registrant_address_2: Optional[StrictStr] = Field(default=None, description="As listed on filing - Registrant Address 2")
    registrant_different_address: Optional[StrictBool] = Field(default=None, description="As listed on filing - Registrant Different Address")
    registrant_city: Optional[StrictStr] = Field(default=None, description="As listed on filing - Registrant City")
    registrant_state: Optional[StrictStr] = Field(default=None, description="As listed on filing - Registrant State")
    registrant_zip: Optional[StrictStr] = Field(default=None, description="As listed on filing - Registrant Zip code")
    registrant: FilingRegistrant
    client: FilingClient
    lobbying_activities: List[FilingLobbyingActivitiesInner]
    conviction_disclosures: List[FilingConvictionDisclosuresInner]
    foreign_entities: List[FilingForeignEntitiesInner]
    affiliated_organizations: List[FilingAffiliatedOrganizationsInner]
    __properties: ClassVar[List[str]] = ["url", "filing_uuid", "filing_type", "filing_type_display", "filing_year", "filing_period", "filing_period_display", "filing_document_url", "filing_document_content_type", "income", "expenses", "expenses_method", "expenses_method_display", "posted_by_name", "dt_posted", "termination_date", "registrant_country", "registrant_ppb_country", "registrant_address_1", "registrant_address_2", "registrant_different_address", "registrant_city", "registrant_state", "registrant_zip", "registrant", "client", "lobbying_activities", "conviction_disclosures", "foreign_entities", "affiliated_organizations"]

    @field_validator('filing_type')
    def filing_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RR', 'RA', 'Q1', 'Q1Y', '1T', '1TY', '1A', '1AY', '1@', '1@Y', 'Q2', 'Q2Y', '2T', '2TY', '2A', '2AY', '2@', '2@Y', 'Q3', 'Q3Y', '3T', '3TY', '3A', '3AY', '3@', '3@Y', 'Q4', 'Q4Y', '4T', '4TY', '4A', '4AY', '4@', '4@Y', 'MM', 'MMY', 'MT', 'MTY', 'MA', 'MAY', 'M@', 'M@Y', 'YY', 'YYY', 'YT', 'YTY', 'YA', 'YAY', 'Y@', 'Y@Y']):
            raise ValueError("must be one of enum values ('RR', 'RA', 'Q1', 'Q1Y', '1T', '1TY', '1A', '1AY', '1@', '1@Y', 'Q2', 'Q2Y', '2T', '2TY', '2A', '2AY', '2@', '2@Y', 'Q3', 'Q3Y', '3T', '3TY', '3A', '3AY', '3@', '3@Y', 'Q4', 'Q4Y', '4T', '4TY', '4A', '4AY', '4@', '4@Y', 'MM', 'MMY', 'MT', 'MTY', 'MA', 'MAY', 'M@', 'M@Y', 'YY', 'YYY', 'YT', 'YTY', 'YA', 'YAY', 'Y@', 'Y@Y')")
        return value

    @field_validator('filing_year')
    def filing_year_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999]):
            raise ValueError("must be one of enum values (2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999)")
        return value

    @field_validator('filing_period')
    def filing_period_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['first_quarter', 'second_quarter', 'third_quarter', 'fourth_quarter', 'mid_year', 'year_end']):
            raise ValueError("must be one of enum values ('first_quarter', 'second_quarter', 'third_quarter', 'fourth_quarter', 'mid_year', 'year_end')")
        return value

    @field_validator('expenses_method')
    def expenses_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a', 'b', 'c']):
            raise ValueError("must be one of enum values ('a', 'b', 'c')")
        return value

    @field_validator('registrant_state')
    def registrant_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AL', 'AK', 'AS', 'AZ', 'AR', 'AA', 'AE', 'AP', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY']):
            raise ValueError("must be one of enum values ('AL', 'AK', 'AS', 'AZ', 'AR', 'AA', 'AE', 'AP', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Filing from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "url",
            "filing_uuid",
            "filing_type",
            "filing_year",
            "filing_period",
            "filing_document_url",
            "filing_document_content_type",
            "income",
            "expenses",
            "expenses_method",
            "posted_by_name",
            "dt_posted",
            "termination_date",
            "registrant_address_1",
            "registrant_address_2",
            "registrant_different_address",
            "registrant_city",
            "registrant_state",
            "registrant_zip",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of registrant
        if self.registrant:
            _dict['registrant'] = self.registrant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client
        if self.client:
            _dict['client'] = self.client.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in lobbying_activities (list)
        _items = []
        if self.lobbying_activities:
            for _item_lobbying_activities in self.lobbying_activities:
                if _item_lobbying_activities:
                    _items.append(_item_lobbying_activities.to_dict())
            _dict['lobbying_activities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in conviction_disclosures (list)
        _items = []
        if self.conviction_disclosures:
            for _item_conviction_disclosures in self.conviction_disclosures:
                if _item_conviction_disclosures:
                    _items.append(_item_conviction_disclosures.to_dict())
            _dict['conviction_disclosures'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in foreign_entities (list)
        _items = []
        if self.foreign_entities:
            for _item_foreign_entities in self.foreign_entities:
                if _item_foreign_entities:
                    _items.append(_item_foreign_entities.to_dict())
            _dict['foreign_entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in affiliated_organizations (list)
        _items = []
        if self.affiliated_organizations:
            for _item_affiliated_organizations in self.affiliated_organizations:
                if _item_affiliated_organizations:
                    _items.append(_item_affiliated_organizations.to_dict())
            _dict['affiliated_organizations'] = _items
        # set to None if income (nullable) is None
        # and model_fields_set contains the field
        if self.income is None and "income" in self.model_fields_set:
            _dict['income'] = None

        # set to None if expenses (nullable) is None
        # and model_fields_set contains the field
        if self.expenses is None and "expenses" in self.model_fields_set:
            _dict['expenses'] = None

        # set to None if expenses_method (nullable) is None
        # and model_fields_set contains the field
        if self.expenses_method is None and "expenses_method" in self.model_fields_set:
            _dict['expenses_method'] = None

        # set to None if posted_by_name (nullable) is None
        # and model_fields_set contains the field
        if self.posted_by_name is None and "posted_by_name" in self.model_fields_set:
            _dict['posted_by_name'] = None

        # set to None if termination_date (nullable) is None
        # and model_fields_set contains the field
        if self.termination_date is None and "termination_date" in self.model_fields_set:
            _dict['termination_date'] = None

        # set to None if registrant_address_1 (nullable) is None
        # and model_fields_set contains the field
        if self.registrant_address_1 is None and "registrant_address_1" in self.model_fields_set:
            _dict['registrant_address_1'] = None

        # set to None if registrant_address_2 (nullable) is None
        # and model_fields_set contains the field
        if self.registrant_address_2 is None and "registrant_address_2" in self.model_fields_set:
            _dict['registrant_address_2'] = None

        # set to None if registrant_different_address (nullable) is None
        # and model_fields_set contains the field
        if self.registrant_different_address is None and "registrant_different_address" in self.model_fields_set:
            _dict['registrant_different_address'] = None

        # set to None if registrant_city (nullable) is None
        # and model_fields_set contains the field
        if self.registrant_city is None and "registrant_city" in self.model_fields_set:
            _dict['registrant_city'] = None

        # set to None if registrant_state (nullable) is None
        # and model_fields_set contains the field
        if self.registrant_state is None and "registrant_state" in self.model_fields_set:
            _dict['registrant_state'] = None

        # set to None if registrant_zip (nullable) is None
        # and model_fields_set contains the field
        if self.registrant_zip is None and "registrant_zip" in self.model_fields_set:
            _dict['registrant_zip'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Filing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "filing_uuid": obj.get("filing_uuid"),
            "filing_type": obj.get("filing_type"),
            "filing_type_display": obj.get("filing_type_display"),
            "filing_year": obj.get("filing_year"),
            "filing_period": obj.get("filing_period"),
            "filing_period_display": obj.get("filing_period_display"),
            "filing_document_url": obj.get("filing_document_url"),
            "filing_document_content_type": obj.get("filing_document_content_type"),
            "income": obj.get("income"),
            "expenses": obj.get("expenses"),
            "expenses_method": obj.get("expenses_method"),
            "expenses_method_display": obj.get("expenses_method_display"),
            "posted_by_name": obj.get("posted_by_name"),
            "dt_posted": obj.get("dt_posted"),
            "termination_date": obj.get("termination_date"),
            "registrant_country": obj.get("registrant_country"),
            "registrant_ppb_country": obj.get("registrant_ppb_country"),
            "registrant_address_1": obj.get("registrant_address_1"),
            "registrant_address_2": obj.get("registrant_address_2"),
            "registrant_different_address": obj.get("registrant_different_address"),
            "registrant_city": obj.get("registrant_city"),
            "registrant_state": obj.get("registrant_state"),
            "registrant_zip": obj.get("registrant_zip"),
            "registrant": FilingRegistrant.from_dict(obj["registrant"]) if obj.get("registrant") is not None else None,
            "client": FilingClient.from_dict(obj["client"]) if obj.get("client") is not None else None,
            "lobbying_activities": [FilingLobbyingActivitiesInner.from_dict(_item) for _item in obj["lobbying_activities"]] if obj.get("lobbying_activities") is not None else None,
            "conviction_disclosures": [FilingConvictionDisclosuresInner.from_dict(_item) for _item in obj["conviction_disclosures"]] if obj.get("conviction_disclosures") is not None else None,
            "foreign_entities": [FilingForeignEntitiesInner.from_dict(_item) for _item in obj["foreign_entities"]] if obj.get("foreign_entities") is not None else None,
            "affiliated_organizations": [FilingAffiliatedOrganizationsInner.from_dict(_item) for _item in obj["affiliated_organizations"]] if obj.get("affiliated_organizations") is not None else None
        })
        return _obj


