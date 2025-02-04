# FilingTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.filing_types import FilingTypes

# TODO update the JSON string below
json = "{}"
# create an instance of FilingTypes from a JSON string
filing_types_instance = FilingTypes.from_json(json)
# print the JSON string representation of the object
print(FilingTypes.to_json())

# convert the object into a dict
filing_types_dict = filing_types_instance.to_dict()
# create an instance of FilingTypes from a dict
filing_types_from_dict = FilingTypes.from_dict(filing_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


