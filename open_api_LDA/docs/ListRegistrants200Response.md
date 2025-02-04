# ListRegistrants200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Registrant]**](Registrant.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_registrants200_response import ListRegistrants200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListRegistrants200Response from a JSON string
list_registrants200_response_instance = ListRegistrants200Response.from_json(json)
# print the JSON string representation of the object
print(ListRegistrants200Response.to_json())

# convert the object into a dict
list_registrants200_response_dict = list_registrants200_response_instance.to_dict()
# create an instance of ListRegistrants200Response from a dict
list_registrants200_response_from_dict = ListRegistrants200Response.from_dict(list_registrants200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


