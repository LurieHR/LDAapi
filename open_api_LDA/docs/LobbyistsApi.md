# openapi_client.LobbyistsApi

All URIs are relative to *https://lda.senate.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_lobbyists**](LobbyistsApi.md#list_lobbyists) | **GET** /api/v1/lobbyists/ | 
[**retrieve_lobbyist**](LobbyistsApi.md#retrieve_lobbyist) | **GET** /api/v1/lobbyists/{id}/ | 


# **list_lobbyists**
> ListLobbyists200Response list_lobbyists(page=page, page_size=page_size, ordering=ordering, id=id, lobbyist_name=lobbyist_name, registrant_id=registrant_id, registrant_name=registrant_name)



Returns all lobbyists matching the provided filters. The ID is a unique integer value identifying this Lobbyist Name as reported by this Registrant.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.list_lobbyists200_response import ListLobbyists200Response
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
    api_instance = openapi_client.LobbyistsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    id = 56 # int | ID (optional)
    lobbyist_name = 'lobbyist_name_example' # str | Lobbyist Name (optional)
    registrant_id = 56 # int | Registrant ID (optional)
    registrant_name = 'registrant_name_example' # str | Registrant Name (optional)

    try:
        api_response = api_instance.list_lobbyists(page=page, page_size=page_size, ordering=ordering, id=id, lobbyist_name=lobbyist_name, registrant_id=registrant_id, registrant_name=registrant_name)
        print("The response of LobbyistsApi->list_lobbyists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LobbyistsApi->list_lobbyists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **id** | **int**| ID | [optional] 
 **lobbyist_name** | **str**| Lobbyist Name | [optional] 
 **registrant_id** | **int**| Registrant ID | [optional] 
 **registrant_name** | **str**| Registrant Name | [optional] 

### Return type

[**ListLobbyists200Response**](ListLobbyists200Response.md)

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

# **retrieve_lobbyist**
> LobbyistWithRegistrant retrieve_lobbyist(id)



Returns all lobbyists matching the provided filters. The ID is a unique integer value identifying this Lobbyist Name as reported by this Registrant.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.lobbyist_with_registrant import LobbyistWithRegistrant
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
    api_instance = openapi_client.LobbyistsApi(api_client)
    id = 56 # int | A unique integer value identifying this Lobbyist.

    try:
        api_response = api_instance.retrieve_lobbyist(id)
        print("The response of LobbyistsApi->retrieve_lobbyist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LobbyistsApi->retrieve_lobbyist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Lobbyist. | 

### Return type

[**LobbyistWithRegistrant**](LobbyistWithRegistrant.md)

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

