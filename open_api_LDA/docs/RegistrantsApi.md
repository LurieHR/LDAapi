# openapi_client.RegistrantsApi

All URIs are relative to *https://lda.senate.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_registrants**](RegistrantsApi.md#list_registrants) | **GET** /api/v1/registrants/ | 
[**retrieve_registrant**](RegistrantsApi.md#retrieve_registrant) | **GET** /api/v1/registrants/{id}/ | 


# **list_registrants**
> ListRegistrants200Response list_registrants(page=page, page_size=page_size, ordering=ordering, id=id, registrant_name=registrant_name, state=state, country=country, ppb_country=ppb_country, dt_updated_after=dt_updated_after, dt_updated_before=dt_updated_before)



Returns all registrants matching the provided filters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.list_registrants200_response import ListRegistrants200Response
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
    api_instance = openapi_client.RegistrantsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    id = 56 # int | ID (optional)
    registrant_name = 'registrant_name_example' # str | Name (optional)
    state = 'state_example' # str | State (optional)
    country = 'country_example' # str | Country (optional)
    ppb_country = 'ppb_country_example' # str | PPB Country (optional)
    dt_updated_after = '2013-10-20T19:20:30+01:00' # datetime | Date Update Range (Before / After): yyyy-mm-dd (optional)
    dt_updated_before = '2013-10-20T19:20:30+01:00' # datetime | Date Update Range (Before / After): yyyy-mm-dd (optional)

    try:
        api_response = api_instance.list_registrants(page=page, page_size=page_size, ordering=ordering, id=id, registrant_name=registrant_name, state=state, country=country, ppb_country=ppb_country, dt_updated_after=dt_updated_after, dt_updated_before=dt_updated_before)
        print("The response of RegistrantsApi->list_registrants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrantsApi->list_registrants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **id** | **int**| ID | [optional] 
 **registrant_name** | **str**| Name | [optional] 
 **state** | **str**| State | [optional] 
 **country** | **str**| Country | [optional] 
 **ppb_country** | **str**| PPB Country | [optional] 
 **dt_updated_after** | **datetime**| Date Update Range (Before / After): yyyy-mm-dd | [optional] 
 **dt_updated_before** | **datetime**| Date Update Range (Before / After): yyyy-mm-dd | [optional] 

### Return type

[**ListRegistrants200Response**](ListRegistrants200Response.md)

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

# **retrieve_registrant**
> Registrant retrieve_registrant(id)



Returns all registrants matching the provided filters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.registrant import Registrant
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
    api_instance = openapi_client.RegistrantsApi(api_client)
    id = 56 # int | A unique integer value identifying this Registrant.

    try:
        api_response = api_instance.retrieve_registrant(id)
        print("The response of RegistrantsApi->retrieve_registrant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistrantsApi->retrieve_registrant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Registrant. | 

### Return type

[**Registrant**](Registrant.md)

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

