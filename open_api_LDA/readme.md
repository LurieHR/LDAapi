# openapi-client
# About the REST API

## Introduction

This document describes the resources that make up the official Lobbying Disclosure REST API v1. If you have any 
issues, please contact the Senate Office of Public Records (OPR) at [lobby@sec.senate.gov](mailto:lobby@sec.senate.gov).
OPR does not offer development advice and does not provide language specific guides. The REST API is programming 
language agnostic. Any programming language can be used to make REST API requests to retrieve data.

The REST API is documented in the **OpenAPI format** which can be found by clicking the \"Download\" button at the top 
of the page. In addition to the standard OpenAPI syntax, we use a few 
[vendor extensions](https://github.com/Redocly/redoc/blob/master/docs/redoc-vendor-extensions.md). There are a 
variety of open source and proprietary tools that can read OpenAPI specifications and interact with the API by reading 
the published specification. OPR does not recommend any specific OpenAPI tools.

## Terms of Service

REST API is governed by a [Terms of Service](https://lda.senate.gov/api/tos/).

## Changes

| Date | Description |
| ------ | ------ |
| 05/09/2024 | Clarified documentation on: date format when filtering results (yyyy-mm-dd) and constants information. |
| 01/18/2024 | Added limitations / caveats section |
| 08/08/2023 | Change request throttle rates from by hour to by minute to reduce burstable requests. New request throttles: unauthenticated (anon): 15/minute (900/hour), API key (registered): 120/minute (7,200/hour) |
| 04/05/2023 | Added requirements to use at least one query string parameter value when paginating results for `Filings` and `Contribution Reports`. See warnings in [Pagination](#section/Implementation-Details/Pagination) for more information. |
| 04/05/2023 | Removed ordering filters for performance reasons. Filing: `id`; Contribution Report: `id`; Client: `registrant_name`; Lobbyist: all but `id` |
| 12/14/2022 | Added registrant address fields as indicated on the latest LD1 / LD2 filing to the filing endpoint. |
| 03/28/2022 | Fixed an issue where LD2 filings posted from 2/15/2022 to 3/28/2022 did not display income or expenses. |
| 01/24/2022 | Added Advanced Text Searching in Filing endpoint on fields: `filing_specific_lobbying_issues`, `lobbyist_conviction_disclosure`, and `lobbyist_covered_position`. |
| 01/13/2022 | Fixed an issue where the list of Contribution Items in Contribution Reports (LD-203) endpoint did not match the filed Contribution Report document. |
| 07/30/2021 | Added Lobbyist endpoint |
| 03/10/2021 | Decreased pagination to 25. Increased request throttle rates: unauthenticated (anon): 1,000/hour, API key (registered): 20,000/hour |


## Schema

All REST API access is over HTTPS, and accessed from `https://lda.senate.gov/api/v1/`. All data is sent and received as JSON. 
Testing can be done through [human browseable API interface](https://lda.senate.gov/api/v1/) where it is possible to make 
requests with filtering/ordering and pagination.

Blank fields are included as `null` instead of being omitted.

All timestamps return in ISO 8601 format:

```text
YYYY-MM-DDTHH:MM:SSZ
```

## Root Endpoint

Sending a request with `GET` to the root endpoint will return all the endpoint categories that the REST API v1 
supports:

**Request:**

```http request
GET https://lda.senate.gov/api/v1/
```

**Reponse:**

```http request
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    \"filings\": \"https://lda.senate.gov/api/v1/filings/\",
    \"contributions\": \"https://lda.senate.gov/api/v1/contributions/\",
    \"registrants\": \"https://lda.senate.gov/api/v1/registrants/\",
    \"clients\": \"https://lda.senate.gov/api/v1/clients/\",
    \"lobbyists\": \"https://lda.senate.gov/api/v1/lobbyists/\",
    \"constants/filing/filingtypes\": \"https://lda.senate.gov/api/v1/constants/filing/filingtypes/\",
    \"constants/filing/lobbyingactivityissues\": \"https://lda.senate.gov/api/v1/constants/filing/lobbyingactivityissues/\",
    \"constants/filing/governmententities\": \"https://lda.senate.gov/api/v1/constants/filing/governmententities/\",
    \"constants/general/countries\": \"https://lda.senate.gov/api/v1/constants/general/countries/\",
    \"constants/general/states\": \"https://lda.senate.gov/api/v1/constants/general/states/\",
    \"constants/lobbyist/prefixes\": \"https://lda.senate.gov/api/v1/constants/lobbyist/prefixes/\",
    \"constants/lobbyist/suffixes\": \"https://lda.senate.gov/api/v1/constants/lobbyist/suffixes/\"
}
```

## Browsable API

APIs may be for machines to access, but humans have to be able to read APIS as well. We support a human-friendly 
HTML output when `HTML` format is requested where it is possible to make requests with filtering/ordering and 
pagination.

[View the HTML API output](https://lda.senate.gov/api/v1/).

## Constants

Lists of key / value constants are published for the following fields:

* Filing Types
* Lobbying Activity Issues
* Government Entities
* Countries
* States (US States)
* Prefixes (e.g. Mr., Ms., Mx., Dr., etc.)
* Suffixes (e.g. Sr., Jr., II, etc.)

These endpoints are periodically updated when new key / values are added. Please see the API [Constants](#tag/Constants) section section of this documenation for more information.

# Authentication 

There are two ways to authenticate through the REST API. Our API offers two types of authentication:

* API Key (Registered)
* Unauthenticated (Anonymous)

For clients to authenticate using an API Key, the token key must be included in the `Authorization` HTTP header and 
**must** be prefixed by the string literal \"Token\", with whitespace separating the two strings. For example:

```http request
Authorization: Token z944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

For clients without an API Key, no special authentication is required, however anonymous clients are subject to 
more strict request throttling.

<schema-definitions />


## Register and Obtain an API Key

[Register](https://lda.senate.gov/api/register/) by using our automated system. After registering, you can obtain an API key 
using one of these methods:

* Via a [web form](https://lda.senate.gov/api/auth/login/)
* Via an API call (Make a `POST` with your `username` and `password` login credentials as form data or JSON.)

The response will contain your API key if properly authenticated.

**Request:**

```http request
POST https://lda.senate.gov/api/auth/login/

{
    \"username\": \"your_username\",
    \"password\": \"your_password\"
}
```

**Response:**

```http request
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    \"key\": \"z944b09199c62bcf9418ad846dd0e4bbdfc6ee4b\"
}
```

## Reset Forgotten Password

If you have forgotten your password or need to change it, you can reset your password using one of these methods:

* Via a [web form](https://lda.senate.gov/api/auth/password/reset/)
* Via an API call (Make a `POST` with your `email` as form data or JSON.)

**Request:**

```http request
POST https://lda.senate.gov/api/auth/password/reset/

{
    \"email\": \"your_email_address\"
}
```

**Response:**

```http request
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    \"detail\": \"Password reset e-mail has been sent.\"
}
```

If successful, you will receive email with a `uid` and `token` to reset your password which can be done using one of 
these methods:

* Via a [web form](https://lda.senate.gov/api/auth/password/reset/confirm/)
* Via an API call (Make a `POST` with you `new_password1` and `new_password2` with the `uid`, and `token` from your 
email  as form data or JSON.)

**Request:**

```http request
POST https://lda.senate.gov/api/auth/password/reset/confirm/

{
    \"new_password1\": \"new_password\",
    \"new_password2\": \"new_password\",
    \"uid\": \"UID from your email\",
    \"token\": \"Token from your email\"
}
```

**Response:**

```http request
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    \"detail\": \"Password reset e-mail has been sent.\"
}
```

# Implementation Details

## Request Throttling

All REST API requests are throttled to prevent abuse and to ensure stability. Our API is 
rate limited depending the type of authentication option you choose:

* API Key (Registered): 120/minute
* Unauthenticated (Anonymous): 15/minute

Unauthenticated requests are rate limited by the originating IP address and not the user making requests. 
Authenticated requests share the same user quota regardless of whether multiple API keys are used. 

Requests made for the following items do not count towards rate limits:

* Original HTML and PDF documents at:
  * `https://lda.senate.gov/filings/public/filing/{filing_uuid}/print/`
  * `https://lda.senate.gov/filings/public/contribution/{filing_uuid}/print/`
* Constants at all URLs starting with `https://lda.senate.gov/api/v1/constants/*`

Requests that exceed the throttling rate for your authentication type will received an HTTP 429 `Too Many Requests` 
response. The `Retry-After` header in the response will indicate the number of seconds to wait.

**Response:**

```http request
HTTP 429 Too Many Requests
Allow: GET
Content-Type: application/json
Retry-After: 1596
Vary: Accept

{
    \"detail\": \"Request was throttled. Expected available in 1596 seconds.\"
}
```

## Pagination

Large result sets are split into individual pages of data. The pagination links are provided as part of the content 
of the response via the `next` and `previous` keys in the response. You can control which page to request by using 
the `page` query string parameter.

**Request:**

```http request
GET https://lda.senate.gov/api/v1/filings/?page=2
```

**Response:**

```http request
HTTP 200 OK

{
    \"count\": 1023
    \"next\": \"https://lda.senate.gov/api/v1/filings/?page=1\",
    \"previous\": \"https://lda.senate.gov/api/v1/filings/?page=3\",
    \"results\": [
       …
    ]
}
```

By default, each page is limited to 25 results per page. You may set the page size by setting `page_size` 
as a query string parameter up to 25.

**Warning**

The `Filings` and `Contribution Reports` endpoints require at least one queryset parameter to be passed in order to paginate
results beyond the first page.  This is for performance reasons.

If you would like to paginate through all `Filings`, we recommend paginating through the results by filing year. Below 
shows an example of getting page 2 of results for filing year 2023 for `Filings`.

**Request:**

```http request
GET https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=2
```

**Response:**

```http request
HTTP 200 OK

{
    \"count\": 1023
    \"next\": \"https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=1\",
    \"previous\": \"https://lda.senate.gov/api/v1/filings/?filing_year=2023&page=3\",
    \"results\": [
       …
    ]
}
```

## Ordering

Result sets can be ordered by using the `ordering` query string parameter. Each endpoint has its own set of fields you 
can order by so see the available ordering in the [browseable API interface](https://lda.senate.gov/api/v1/) under the \"Filters\" 
button in the upper right corner of the interface.

For example, to order filings by `dt_posted`:

```http request
GET https://lda.senate.gov/api/v1/filings/?ordering=dt_posted
```

The client may also specify reverse orderings by prefixing the field name with `-`, like so:

```http request
GET https://lda.senate.gov/api/v1/filings/?ordering=-dt_posted
```

Multiple orderings may also be specified:

```http request
GET https://lda.senate.gov/api/v1/filings/?ordering=dt_posted,registrant__name
```

## Advanced Text Searching

- **Unquoted Text** - Text not inside quote marks will not be treated as a phrase. Text separated by a space is treated as an OR operator between them. _Estate Tax_ will match _estate_ OR _tax_ even if they do appear next to each other.
- **&quot;Quoted Text&quot;** - Text inside double quote marks will be treated as a phrase. _Estate Tax_ will match the phrase _estate tax_ but will not match the words _estate_ or _tax_ if they appear separately.
- **OR** - The word _OR_ will be treated as a true OR operator. _&quot;Estate Tax&quot; OR &quot;Estate Taxes&quot;_ will match the phrases _estate tax_or _estate taxes_ but will not match the words _estate_ or _tax_ if they appear separately.
- **-** The dash character _-_ will be treated as a NOT EQUALS operator. _&quot;Estate Tax&quot; -&quot;Payroll Taxes&quot;_ will match the phrase _estate tax_ but not _payroll taxes_ if they appear in the same field.

## Limitations / Caveats

- **Government Entities** - Filings that posted before 2/14/2021 do not have government entities broken down by each individual lobbying activity area. Instead, the government entities listed on these filings is a list of entities that appear on the filing as a whole. This limitation is due to data imported from a legacy system. Filings that posted after 2/14/2021 will have government entities broken down by each individual lobbying activity area.

# Common Errors

## Invalid API Key

If you supply an invalid API Key, you will receive an HTTP 401 `Unauthorized` response:

**Response:**

```http request
HTTP 401 UNAUTHORIZED

{
    \"detail\": \"Invalid token.\"
}
```

## Request Throttled

If you exceed your rate limit for your authentication type, you will receive an HTTP 429 `Too Many Requests` 
response. See the [Request Throttling](#section/Implementation-Details/Request-Throttling) section for more information.

**Response:**

```http request
HTTP 429 Too Many Requests
Allow: GET
Content-Type: application/json
Retry-After: 1596
Vary: Accept

{
    \"detail\": \"Request was throttled. Expected available in 1596 seconds.\"
}
```

## Invalid Query String Parameter Values

If you pass invalid query string parameter values, you will likely receive an HTTP 404 `Not Found` or HTTP 400 
`Bad Request` response with a detailed error message.

For example, passing a non-integer for the page number:

**Request:**

```http request
GET https://lda.senate.gov/api/v1/filings/?page=a
```

**Response:**

```http request
HTTP 404 Not Found
Allow: GET
Content-Type: application/json
Vary: Accept

{
    \"detail\": \"Invalid page.\"
}
```

For example, passing an invalid value for the Registrant ID:

**Request:**

```http request
GET https://lda.senate.gov/api/v1/filings/?registrant_id=a
```

**Response:**

```http request
HTTP 400 Bad Request
Allow: GET
Content-Type: application/json
Vary: Accept

{
    \"registrant_id\": [
        \"Enter a number.\"
    ]
}
```

## Unsupported HTTP Method

If you use an unsupported HTTP method, you will receive an HTTP 405 `Method Not Allowed` response:

```http request
DELETE https://lda.senate.gov/api/v1/filings/
Accept: application/json
```

**Response:**

```http request
HTTP 405 Method Not Allowed
Content-Type: application/json
Content-Length: 42

{
    \"detail\": \"Method \\\"DELETE\\\" not allowed.\"
}
```

## Query String Filters Required for Pagination

If you use paginated results and do not include at least one query string parameter filter, you will receive an HTTP 400 `Bad Request` response:

```http request
GET https://lda.senate.gov/api/v1/filings/?page=2
```

**Response:**

```http request
HTTP 400 Bad Request
Allow: GET
Content-Type: application/json
Vary: Accept

{
   \"detail\": \"You must pass at least one query string parameter to filter the results and be able to paginate the results.\"
}
```

See warnings in [Pagination](#section/Implementation-Details/Pagination) for more information.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.senate.gov/legislative/opr.htm](https://www.senate.gov/legislative/opr.htm)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lda.senate.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://lda.senate.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClientsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    id = 56 # int | ID (optional)
    client_name = 'client_name_example' # str | Client Name (optional)
    client_state = 'client_state_example' # str | Client State (optional)
    client_country = 'client_country_example' # str | Client Country (optional)
    client_ppb_state = 'client_ppb_state_example' # str | Client PPB State (optional)
    client_ppb_country = 'client_ppb_country_example' # str | Client PPB Country (optional)
    registrant_id = 56 # int | Registrant ID (optional)
    registrant_name = 'registrant_name_example' # str | Registrant Name (optional)

    try:
        api_response = api_instance.list_clients(page=page, page_size=page_size, ordering=ordering, id=id, client_name=client_name, client_state=client_state, client_country=client_country, client_ppb_state=client_ppb_state, client_ppb_country=client_ppb_country, registrant_id=registrant_id, registrant_name=registrant_name)
        print("The response of ClientsApi->list_clients:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientsApi->list_clients: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://lda.senate.gov*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClientsApi* | [**list_clients**](docs/ClientsApi.md#list_clients) | **GET** /api/v1/clients/ | 
*ClientsApi* | [**retrieve_client**](docs/ClientsApi.md#retrieve_client) | **GET** /api/v1/clients/{id}/ | 
*ConstantsApi* | [**list_contribution_item_types**](docs/ConstantsApi.md#list_contribution_item_types) | **GET** /api/v1/constants/contribution/itemtypes/ | 
*ConstantsApi* | [**list_countries**](docs/ConstantsApi.md#list_countries) | **GET** /api/v1/constants/general/countries/ | 
*ConstantsApi* | [**list_filing_types**](docs/ConstantsApi.md#list_filing_types) | **GET** /api/v1/constants/filing/filingtypes/ | 
*ConstantsApi* | [**list_government_entities**](docs/ConstantsApi.md#list_government_entities) | **GET** /api/v1/constants/filing/governmententities/ | 
*ConstantsApi* | [**list_lobbying_activity_general_issues**](docs/ConstantsApi.md#list_lobbying_activity_general_issues) | **GET** /api/v1/constants/filing/lobbyingactivityissues/ | 
*ConstantsApi* | [**list_lobbyist_prefixes**](docs/ConstantsApi.md#list_lobbyist_prefixes) | **GET** /api/v1/constants/lobbyist/prefixes/ | 
*ConstantsApi* | [**list_lobbyist_suffixes**](docs/ConstantsApi.md#list_lobbyist_suffixes) | **GET** /api/v1/constants/lobbyist/suffixes/ | 
*ConstantsApi* | [**list_states**](docs/ConstantsApi.md#list_states) | **GET** /api/v1/constants/general/states/ | 
*ContributionReportsApi* | [**list_contribution_reports**](docs/ContributionReportsApi.md#list_contribution_reports) | **GET** /api/v1/contributions/ | 
*ContributionReportsApi* | [**retrieve_contribution_report**](docs/ContributionReportsApi.md#retrieve_contribution_report) | **GET** /api/v1/contributions/{filing_uuid}/ | 
*FilingsApi* | [**list_filings**](docs/FilingsApi.md#list_filings) | **GET** /api/v1/filings/ | 
*FilingsApi* | [**retrieve_filing**](docs/FilingsApi.md#retrieve_filing) | **GET** /api/v1/filings/{filing_uuid}/ | 
*LobbyistsApi* | [**list_lobbyists**](docs/LobbyistsApi.md#list_lobbyists) | **GET** /api/v1/lobbyists/ | 
*LobbyistsApi* | [**retrieve_lobbyist**](docs/LobbyistsApi.md#retrieve_lobbyist) | **GET** /api/v1/lobbyists/{id}/ | 
*RegistrantsApi* | [**list_registrants**](docs/RegistrantsApi.md#list_registrants) | **GET** /api/v1/registrants/ | 
*RegistrantsApi* | [**retrieve_registrant**](docs/RegistrantsApi.md#retrieve_registrant) | **GET** /api/v1/registrants/{id}/ | 


## Documentation For Models

 - [Client](docs/Client.md)
 - [ContributionItemTypes](docs/ContributionItemTypes.md)
 - [ContributionReport](docs/ContributionReport.md)
 - [ContributionReportContributionItemsInner](docs/ContributionReportContributionItemsInner.md)
 - [ContributionReportRegistrant](docs/ContributionReportRegistrant.md)
 - [Countries](docs/Countries.md)
 - [Error](docs/Error.md)
 - [Filing](docs/Filing.md)
 - [FilingAffiliatedOrganizationsInner](docs/FilingAffiliatedOrganizationsInner.md)
 - [FilingClient](docs/FilingClient.md)
 - [FilingConvictionDisclosuresInner](docs/FilingConvictionDisclosuresInner.md)
 - [FilingForeignEntitiesInner](docs/FilingForeignEntitiesInner.md)
 - [FilingLobbyingActivitiesInner](docs/FilingLobbyingActivitiesInner.md)
 - [FilingLobbyingActivitiesInnerGovernmentEntitiesInner](docs/FilingLobbyingActivitiesInnerGovernmentEntitiesInner.md)
 - [FilingLobbyingActivitiesInnerLobbyistsInner](docs/FilingLobbyingActivitiesInnerLobbyistsInner.md)
 - [FilingLobbyingActivitiesInnerLobbyistsInnerLobbyist](docs/FilingLobbyingActivitiesInnerLobbyistsInnerLobbyist.md)
 - [FilingRegistrant](docs/FilingRegistrant.md)
 - [FilingTypes](docs/FilingTypes.md)
 - [GovernmentEntities](docs/GovernmentEntities.md)
 - [ListClients200Response](docs/ListClients200Response.md)
 - [ListContributionReports200Response](docs/ListContributionReports200Response.md)
 - [ListFilings200Response](docs/ListFilings200Response.md)
 - [ListLobbyists200Response](docs/ListLobbyists200Response.md)
 - [ListRegistrants200Response](docs/ListRegistrants200Response.md)
 - [LobbyingActivityGeneralIssues](docs/LobbyingActivityGeneralIssues.md)
 - [LobbyistPrefixes](docs/LobbyistPrefixes.md)
 - [LobbyistSuffixes](docs/LobbyistSuffixes.md)
 - [LobbyistWithRegistrant](docs/LobbyistWithRegistrant.md)
 - [Registrant](docs/Registrant.md)
 - [States](docs/States.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

lobby@sec.senate.gov


