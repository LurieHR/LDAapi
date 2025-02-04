# openapi_client.FilingsApi

All URIs are relative to *https://lda.senate.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_filings**](FilingsApi.md#list_filings) | **GET** /api/v1/filings/ | 
[**retrieve_filing**](FilingsApi.md#retrieve_filing) | **GET** /api/v1/filings/{filing_uuid}/ | 


# **list_filings**
> ListFilings200Response list_filings(page=page, page_size=page_size, ordering=ordering, filing_uuid=filing_uuid, registrant_id=registrant_id, registrant_name=registrant_name, registrant_country=registrant_country, registrant_ppb_country=registrant_ppb_country, client_id=client_id, client_name=client_name, client_state=client_state, client_country=client_country, client_ppb_state=client_ppb_state, client_ppb_country=client_ppb_country, lobbyist_id=lobbyist_id, lobbyist_name=lobbyist_name, lobbyist_covered_position=lobbyist_covered_position, lobbyist_covered_position_indicator=lobbyist_covered_position_indicator, lobbyist_conviction_disclosure=lobbyist_conviction_disclosure, lobbyist_conviction_disclosure_indicator=lobbyist_conviction_disclosure_indicator, lobbyist_conviction_date_range_after=lobbyist_conviction_date_range_after, lobbyist_conviction_date_range_before=lobbyist_conviction_date_range_before, filing_type=filing_type, filing_year=filing_year, filing_period=filing_period, filing_dt_posted_after=filing_dt_posted_after, filing_dt_posted_before=filing_dt_posted_before, filing_amount_reported_min=filing_amount_reported_min, filing_amount_reported_max=filing_amount_reported_max, filing_specific_lobbying_issues=filing_specific_lobbying_issues, affiliated_organization_name=affiliated_organization_name, affiliated_organization_country=affiliated_organization_country, affiliated_organization_listed_indicator=affiliated_organization_listed_indicator, foreign_entity_name=foreign_entity_name, foreign_entity_country=foreign_entity_country, foreign_entity_listed_indicator=foreign_entity_listed_indicator, foreign_entity_ppb_country=foreign_entity_ppb_country, foreign_entity_ownership_percentage_min=foreign_entity_ownership_percentage_min, foreign_entity_ownership_percentage_max=foreign_entity_ownership_percentage_max)





### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.list_filings200_response import ListFilings200Response
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
    api_instance = openapi_client.FilingsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    filing_uuid = 'filing_uuid_example' # str | filing_uuid (optional)
    registrant_id = 56 # int | Registrant ID (optional)
    registrant_name = 'registrant_name_example' # str | Registrant Name (optional)
    registrant_country = 'registrant_country_example' # str | Registrant Country (optional)
    registrant_ppb_country = 'registrant_ppb_country_example' # str | Registrant PPB Country (optional)
    client_id = 56 # int | Client ID (optional)
    client_name = 'client_name_example' # str | Client Name (optional)
    client_state = 'client_state_example' # str | Client State (optional)
    client_country = 'client_country_example' # str | Client Country (optional)
    client_ppb_state = 'client_ppb_state_example' # str | Client PPB State (optional)
    client_ppb_country = 'client_ppb_country_example' # str | Client PPB Country (optional)
    lobbyist_id = 56 # int | Lobbyist ID (optional)
    lobbyist_name = 'lobbyist_name_example' # str | Lobbyist Name (optional)
    lobbyist_covered_position = 'lobbyist_covered_position_example' # str | Lobbyist Covered Position (Supports Advanced Text Searching) (optional)
    lobbyist_covered_position_indicator = True # bool | Any Covered Government Position(s) (optional)
    lobbyist_conviction_disclosure = 'lobbyist_conviction_disclosure_example' # str | Lobbyist Conviction Description (Supports Advanced Text Searching) (optional)
    lobbyist_conviction_disclosure_indicator = True # bool | Lobbyist Any Disclosed Conviction(s) (optional)
    lobbyist_conviction_date_range_after = '2013-10-20' # date | Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd (optional)
    lobbyist_conviction_date_range_before = '2013-10-20' # date | Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd (optional)
    filing_type = 'filing_type_example' # str | Filing Type (optional)
    filing_year = 3.4 # float | Filing Year (optional)
    filing_period = 'filing_period_example' # str | Filing Period (optional)
    filing_dt_posted_after = '2013-10-20T19:20:30+01:00' # datetime | Filing Date Posted Range (Before / After): yyyy-mm-dd (optional)
    filing_dt_posted_before = '2013-10-20T19:20:30+01:00' # datetime | Filing Date Posted Range (Before / After): yyyy-mm-dd (optional)
    filing_amount_reported_min = 3.4 # float | Filing Amount Reported Range (Min / Max) (optional)
    filing_amount_reported_max = 3.4 # float | Filing Amount Reported Range (Min / Max) (optional)
    filing_specific_lobbying_issues = 'filing_specific_lobbying_issues_example' # str | Filing Specific Lobbying Issues (Supports Advanced Text Searching) (optional)
    affiliated_organization_name = 'affiliated_organization_name_example' # str | Affiliated Organization Name (optional)
    affiliated_organization_country = 'affiliated_organization_country_example' # str | Affiliated Organization Country (optional)
    affiliated_organization_listed_indicator = True # bool | Any Affiliated Organizations Listed (optional)
    foreign_entity_name = 'foreign_entity_name_example' # str | Foreign Entity Name (optional)
    foreign_entity_country = 'foreign_entity_country_example' # str | Foreign Entity Country (optional)
    foreign_entity_listed_indicator = True # bool | Any Foreign Entities Listed (optional)
    foreign_entity_ppb_country = 'foreign_entity_ppb_country_example' # str | Foreign Entity PPB Country (optional)
    foreign_entity_ownership_percentage_min = 'foreign_entity_ownership_percentage_min_example' # str | Foreign Entity Ownership Percentage (optional)
    foreign_entity_ownership_percentage_max = 'foreign_entity_ownership_percentage_max_example' # str | Foreign Entity Ownership Percentage (optional)

    try:
        api_response = api_instance.list_filings(page=page, page_size=page_size, ordering=ordering, filing_uuid=filing_uuid, registrant_id=registrant_id, registrant_name=registrant_name, registrant_country=registrant_country, registrant_ppb_country=registrant_ppb_country, client_id=client_id, client_name=client_name, client_state=client_state, client_country=client_country, client_ppb_state=client_ppb_state, client_ppb_country=client_ppb_country, lobbyist_id=lobbyist_id, lobbyist_name=lobbyist_name, lobbyist_covered_position=lobbyist_covered_position, lobbyist_covered_position_indicator=lobbyist_covered_position_indicator, lobbyist_conviction_disclosure=lobbyist_conviction_disclosure, lobbyist_conviction_disclosure_indicator=lobbyist_conviction_disclosure_indicator, lobbyist_conviction_date_range_after=lobbyist_conviction_date_range_after, lobbyist_conviction_date_range_before=lobbyist_conviction_date_range_before, filing_type=filing_type, filing_year=filing_year, filing_period=filing_period, filing_dt_posted_after=filing_dt_posted_after, filing_dt_posted_before=filing_dt_posted_before, filing_amount_reported_min=filing_amount_reported_min, filing_amount_reported_max=filing_amount_reported_max, filing_specific_lobbying_issues=filing_specific_lobbying_issues, affiliated_organization_name=affiliated_organization_name, affiliated_organization_country=affiliated_organization_country, affiliated_organization_listed_indicator=affiliated_organization_listed_indicator, foreign_entity_name=foreign_entity_name, foreign_entity_country=foreign_entity_country, foreign_entity_listed_indicator=foreign_entity_listed_indicator, foreign_entity_ppb_country=foreign_entity_ppb_country, foreign_entity_ownership_percentage_min=foreign_entity_ownership_percentage_min, foreign_entity_ownership_percentage_max=foreign_entity_ownership_percentage_max)
        print("The response of FilingsApi->list_filings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingsApi->list_filings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **filing_uuid** | **str**| filing_uuid | [optional] 
 **registrant_id** | **int**| Registrant ID | [optional] 
 **registrant_name** | **str**| Registrant Name | [optional] 
 **registrant_country** | **str**| Registrant Country | [optional] 
 **registrant_ppb_country** | **str**| Registrant PPB Country | [optional] 
 **client_id** | **int**| Client ID | [optional] 
 **client_name** | **str**| Client Name | [optional] 
 **client_state** | **str**| Client State | [optional] 
 **client_country** | **str**| Client Country | [optional] 
 **client_ppb_state** | **str**| Client PPB State | [optional] 
 **client_ppb_country** | **str**| Client PPB Country | [optional] 
 **lobbyist_id** | **int**| Lobbyist ID | [optional] 
 **lobbyist_name** | **str**| Lobbyist Name | [optional] 
 **lobbyist_covered_position** | **str**| Lobbyist Covered Position (Supports Advanced Text Searching) | [optional] 
 **lobbyist_covered_position_indicator** | **bool**| Any Covered Government Position(s) | [optional] 
 **lobbyist_conviction_disclosure** | **str**| Lobbyist Conviction Description (Supports Advanced Text Searching) | [optional] 
 **lobbyist_conviction_disclosure_indicator** | **bool**| Lobbyist Any Disclosed Conviction(s) | [optional] 
 **lobbyist_conviction_date_range_after** | **date**| Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd | [optional] 
 **lobbyist_conviction_date_range_before** | **date**| Lobbyist Conviction Date Range (Before / After): yyyy-mm-dd | [optional] 
 **filing_type** | **str**| Filing Type | [optional] 
 **filing_year** | **float**| Filing Year | [optional] 
 **filing_period** | **str**| Filing Period | [optional] 
 **filing_dt_posted_after** | **datetime**| Filing Date Posted Range (Before / After): yyyy-mm-dd | [optional] 
 **filing_dt_posted_before** | **datetime**| Filing Date Posted Range (Before / After): yyyy-mm-dd | [optional] 
 **filing_amount_reported_min** | **float**| Filing Amount Reported Range (Min / Max) | [optional] 
 **filing_amount_reported_max** | **float**| Filing Amount Reported Range (Min / Max) | [optional] 
 **filing_specific_lobbying_issues** | **str**| Filing Specific Lobbying Issues (Supports Advanced Text Searching) | [optional] 
 **affiliated_organization_name** | **str**| Affiliated Organization Name | [optional] 
 **affiliated_organization_country** | **str**| Affiliated Organization Country | [optional] 
 **affiliated_organization_listed_indicator** | **bool**| Any Affiliated Organizations Listed | [optional] 
 **foreign_entity_name** | **str**| Foreign Entity Name | [optional] 
 **foreign_entity_country** | **str**| Foreign Entity Country | [optional] 
 **foreign_entity_listed_indicator** | **bool**| Any Foreign Entities Listed | [optional] 
 **foreign_entity_ppb_country** | **str**| Foreign Entity PPB Country | [optional] 
 **foreign_entity_ownership_percentage_min** | **str**| Foreign Entity Ownership Percentage | [optional] 
 **foreign_entity_ownership_percentage_max** | **str**| Foreign Entity Ownership Percentage | [optional] 

### Return type

[**ListFilings200Response**](ListFilings200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests - Throttled |  * Retry-After -  Expected available in X seconds. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_filing**
> Filing retrieve_filing(filing_uuid)



Returns all filings matching the provided filters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.filing import Filing
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
    api_instance = openapi_client.FilingsApi(api_client)
    filing_uuid = 'filing_uuid_example' # str | 

    try:
        api_response = api_instance.retrieve_filing(filing_uuid)
        print("The response of FilingsApi->retrieve_filing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilingsApi->retrieve_filing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filing_uuid** | **str**|  | 

### Return type

[**Filing**](Filing.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests - Throttled |  * Retry-After -  Expected available in X seconds. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

