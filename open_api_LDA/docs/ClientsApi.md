# openapi_client.ClientsApi

All URIs are relative to *https://lda.senate.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_clients**](ClientsApi.md#list_clients) | **GET** /api/v1/clients/ | 
[**retrieve_client**](ClientsApi.md#retrieve_client) | **GET** /api/v1/clients/{id}/ | 


# **list_clients**
> ListClients200Response list_clients(page=page, page_size=page_size, ordering=ordering, id=id, client_name=client_name, client_state=client_state, client_country=client_country, client_ppb_state=client_ppb_state, client_ppb_country=client_ppb_country, registrant_id=registrant_id, registrant_name=registrant_name)



Returns all clients matching the provided filters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.list_clients200_response import ListClients200Response
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
    except Exception as e:
        print("Exception when calling ClientsApi->list_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **id** | **int**| ID | [optional] 
 **client_name** | **str**| Client Name | [optional] 
 **client_state** | **str**| Client State | [optional] 
 **client_country** | **str**| Client Country | [optional] 
 **client_ppb_state** | **str**| Client PPB State | [optional] 
 **client_ppb_country** | **str**| Client PPB Country | [optional] 
 **registrant_id** | **int**| Registrant ID | [optional] 
 **registrant_name** | **str**| Registrant Name | [optional] 

### Return type

[**ListClients200Response**](ListClients200Response.md)

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

# **retrieve_client**
> Client retrieve_client(id)



Returns all clients matching the provided filters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.client import Client
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
    id = 56 # int | A unique integer value identifying this Client.

    try:
        api_response = api_instance.retrieve_client(id)
        print("The response of ClientsApi->retrieve_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->retrieve_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Client. | 

### Return type

[**Client**](Client.md)

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

