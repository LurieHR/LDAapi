# GovernmentEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.government_entities import GovernmentEntities

# TODO update the JSON string below
json = "{}"
# create an instance of GovernmentEntities from a JSON string
government_entities_instance = GovernmentEntities.from_json(json)
# print the JSON string representation of the object
print(GovernmentEntities.to_json())

# convert the object into a dict
government_entities_dict = government_entities_instance.to_dict()
# create an instance of GovernmentEntities from a dict
government_entities_from_dict = GovernmentEntities.from_dict(government_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


