# openapi_client.ConstantsApi

All URIs are relative to *https://lda.senate.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_contribution_item_types**](ConstantsApi.md#list_contribution_item_types) | **GET** /api/v1/constants/contribution/itemtypes/ | 
[**list_countries**](ConstantsApi.md#list_countries) | **GET** /api/v1/constants/general/countries/ | 
[**list_filing_types**](ConstantsApi.md#list_filing_types) | **GET** /api/v1/constants/filing/filingtypes/ | 
[**list_government_entities**](ConstantsApi.md#list_government_entities) | **GET** /api/v1/constants/filing/governmententities/ | 
[**list_lobbying_activity_general_issues**](ConstantsApi.md#list_lobbying_activity_general_issues) | **GET** /api/v1/constants/filing/lobbyingactivityissues/ | 
[**list_lobbyist_prefixes**](ConstantsApi.md#list_lobbyist_prefixes) | **GET** /api/v1/constants/lobbyist/prefixes/ | 
[**list_lobbyist_suffixes**](ConstantsApi.md#list_lobbyist_suffixes) | **GET** /api/v1/constants/lobbyist/suffixes/ | 
[**list_states**](ConstantsApi.md#list_states) | **GET** /api/v1/constants/general/states/ | 


# **list_contribution_item_types**
> List[ContributionItemTypes] list_contribution_item_types()



Returns all ContributionItemTypes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.contribution_item_types import ContributionItemTypes
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
    api_instance = openapi_client.ConstantsApi(api_client)

    try:
        api_response = api_instance.list_contribution_item_types()
        print("The response of ConstantsApi->list_contribution_item_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstantsApi->list_contribution_item_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ContributionItemTypes]**](ContributionItemTypes.md)

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

# **list_countries**
> List[Countries] list_countries()



Returns all Countries.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.countries import Countries
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
    api_instance = openapi_client.ConstantsApi(api_client)

    try:
        api_response = api_instance.list_countries()
        print("The response of ConstantsApi->list_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstantsApi->list_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Countries]**](Countries.md)

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

# **list_filing_types**
> List[FilingTypes] list_filing_types()



Returns all FilingTypes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.filing_types import FilingTypes
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
    api_instance = openapi_client.ConstantsApi(api_client)

    try:
        api_response = api_instance.list_filing_types()
        print("The response of ConstantsApi->list_filing_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstantsApi->list_filing_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FilingTypes]**](FilingTypes.md)

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

# **list_government_entities**
> List[GovernmentEntities] list_government_entities()



Returns all GovernmentEntities.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.government_entities import GovernmentEntities
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
    api_instance = openapi_client.ConstantsApi(api_client)

    try:
        api_response = api_instance.list_government_entities()
        print("The response of ConstantsApi->list_government_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstantsApi->list_government_entities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GovernmentEntities]**](GovernmentEntities.md)

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

# **list_lobbying_activity_general_issues**
> List[LobbyingActivityGeneralIssues] list_lobbying_activity_general_issues()



Returns all LobbyingActivityGeneralIssues.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.lobbying_activity_general_issues import LobbyingActivityGeneralIssues
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
    api_instance = openapi_client.ConstantsApi(api_client)

    try:
        api_response = api_instance.list_lobbying_activity_general_issues()
        print("The response of ConstantsApi->list_lobbying_activity_general_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstantsApi->list_lobbying_activity_general_issues: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LobbyingActivityGeneralIssues]**](LobbyingActivityGeneralIssues.md)

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

# **list_lobbyist_prefixes**
> List[LobbyistPrefixes] list_lobbyist_prefixes()



Returns all LobbyistPrefixes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.lobbyist_prefixes import LobbyistPrefixes
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
    api_instance = openapi_client.ConstantsApi(api_client)

    try:
        api_response = api_instance.list_lobbyist_prefixes()
        print("The response of ConstantsApi->list_lobbyist_prefixes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstantsApi->list_lobbyist_prefixes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LobbyistPrefixes]**](LobbyistPrefixes.md)

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

# **list_lobbyist_suffixes**
> List[LobbyistSuffixes] list_lobbyist_suffixes()



Returns all LobbyistSuffixes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.lobbyist_suffixes import LobbyistSuffixes
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
    api_instance = openapi_client.ConstantsApi(api_client)

    try:
        api_response = api_instance.list_lobbyist_suffixes()
        print("The response of ConstantsApi->list_lobbyist_suffixes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstantsApi->list_lobbyist_suffixes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LobbyistSuffixes]**](LobbyistSuffixes.md)

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

# **list_states**
> List[States] list_states()



Returns all States.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.states import States
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
    api_instance = openapi_client.ConstantsApi(api_client)

    try:
        api_response = api_instance.list_states()
        print("The response of ConstantsApi->list_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstantsApi->list_states: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[States]**](States.md)

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

