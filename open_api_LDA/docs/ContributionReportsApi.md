# openapi_client.ContributionReportsApi

All URIs are relative to *https://lda.senate.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_contribution_reports**](ContributionReportsApi.md#list_contribution_reports) | **GET** /api/v1/contributions/ | 
[**retrieve_contribution_report**](ContributionReportsApi.md#retrieve_contribution_report) | **GET** /api/v1/contributions/{filing_uuid}/ | 


# **list_contribution_reports**
> ListContributionReports200Response list_contribution_reports(page=page, page_size=page_size, ordering=ordering, filing_uuid=filing_uuid, filing_type=filing_type, filing_year=filing_year, filing_period=filing_period, filing_dt_posted_after=filing_dt_posted_after, filing_dt_posted_before=filing_dt_posted_before, registrant_id=registrant_id, registrant_name=registrant_name, lobbyist_id=lobbyist_id, lobbyist_name=lobbyist_name, lobbyist_exclude=lobbyist_exclude, contribution_date_after=contribution_date_after, contribution_date_before=contribution_date_before, contribution_amount_min=contribution_amount_min, contribution_amount_max=contribution_amount_max, contribution_type=contribution_type, contribution_contributor=contribution_contributor, contribution_payee=contribution_payee, contribution_honoree=contribution_honoree)





### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.list_contribution_reports200_response import ListContributionReports200Response
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
    api_instance = openapi_client.ContributionReportsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    filing_uuid = 'filing_uuid_example' # str | filing_uuid (optional)
    filing_type = 'filing_type_example' # str | Filing Type (optional)
    filing_year = 3.4 # float | Filing Year (optional)
    filing_period = 'filing_period_example' # str | Filing Period (optional)
    filing_dt_posted_after = '2013-10-20T19:20:30+01:00' # datetime | Filing Date Posted Range (Before / After): yyyy-mm-dd (optional)
    filing_dt_posted_before = '2013-10-20T19:20:30+01:00' # datetime | Filing Date Posted Range (Before / After): yyyy-mm-dd (optional)
    registrant_id = 56 # int | Registrant ID (optional)
    registrant_name = 'registrant_name_example' # str | Registrant Name (optional)
    lobbyist_id = 56 # int | Lobbyist ID (optional)
    lobbyist_name = 'lobbyist_name_example' # str | Lobbyist Name (optional)
    lobbyist_exclude = True # bool | Exclude reports filed by the lobbyists. (optional)
    contribution_date_after = '2013-10-20' # date | Contribution Date Range (Before / After): yyyy-mm-dd (optional)
    contribution_date_before = '2013-10-20' # date | Contribution Date Range (Before / After): yyyy-mm-dd (optional)
    contribution_amount_min = 3.4 # float | Contribution Amount Range (optional)
    contribution_amount_max = 3.4 # float | Contribution Amount Range (optional)
    contribution_type = 'contribution_type_example' # str | Contribution Type (optional)
    contribution_contributor = 'contribution_contributor_example' # str | Contribution Contributor Name (optional)
    contribution_payee = 'contribution_payee_example' # str | Contribution Payee Name (optional)
    contribution_honoree = 'contribution_honoree_example' # str | Contribution Honoree Name (optional)

    try:
        api_response = api_instance.list_contribution_reports(page=page, page_size=page_size, ordering=ordering, filing_uuid=filing_uuid, filing_type=filing_type, filing_year=filing_year, filing_period=filing_period, filing_dt_posted_after=filing_dt_posted_after, filing_dt_posted_before=filing_dt_posted_before, registrant_id=registrant_id, registrant_name=registrant_name, lobbyist_id=lobbyist_id, lobbyist_name=lobbyist_name, lobbyist_exclude=lobbyist_exclude, contribution_date_after=contribution_date_after, contribution_date_before=contribution_date_before, contribution_amount_min=contribution_amount_min, contribution_amount_max=contribution_amount_max, contribution_type=contribution_type, contribution_contributor=contribution_contributor, contribution_payee=contribution_payee, contribution_honoree=contribution_honoree)
        print("The response of ContributionReportsApi->list_contribution_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContributionReportsApi->list_contribution_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **filing_uuid** | **str**| filing_uuid | [optional] 
 **filing_type** | **str**| Filing Type | [optional] 
 **filing_year** | **float**| Filing Year | [optional] 
 **filing_period** | **str**| Filing Period | [optional] 
 **filing_dt_posted_after** | **datetime**| Filing Date Posted Range (Before / After): yyyy-mm-dd | [optional] 
 **filing_dt_posted_before** | **datetime**| Filing Date Posted Range (Before / After): yyyy-mm-dd | [optional] 
 **registrant_id** | **int**| Registrant ID | [optional] 
 **registrant_name** | **str**| Registrant Name | [optional] 
 **lobbyist_id** | **int**| Lobbyist ID | [optional] 
 **lobbyist_name** | **str**| Lobbyist Name | [optional] 
 **lobbyist_exclude** | **bool**| Exclude reports filed by the lobbyists. | [optional] 
 **contribution_date_after** | **date**| Contribution Date Range (Before / After): yyyy-mm-dd | [optional] 
 **contribution_date_before** | **date**| Contribution Date Range (Before / After): yyyy-mm-dd | [optional] 
 **contribution_amount_min** | **float**| Contribution Amount Range | [optional] 
 **contribution_amount_max** | **float**| Contribution Amount Range | [optional] 
 **contribution_type** | **str**| Contribution Type | [optional] 
 **contribution_contributor** | **str**| Contribution Contributor Name | [optional] 
 **contribution_payee** | **str**| Contribution Payee Name | [optional] 
 **contribution_honoree** | **str**| Contribution Honoree Name | [optional] 

### Return type

[**ListContributionReports200Response**](ListContributionReports200Response.md)

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

# **retrieve_contribution_report**
> ContributionReport retrieve_contribution_report(filing_uuid)



Returns all contributions matching the provided filters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.contribution_report import ContributionReport
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
    api_instance = openapi_client.ContributionReportsApi(api_client)
    filing_uuid = 'filing_uuid_example' # str | 

    try:
        api_response = api_instance.retrieve_contribution_report(filing_uuid)
        print("The response of ContributionReportsApi->retrieve_contribution_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContributionReportsApi->retrieve_contribution_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filing_uuid** | **str**|  | 

### Return type

[**ContributionReport**](ContributionReport.md)

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

