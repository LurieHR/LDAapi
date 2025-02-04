# ContributionItemTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.contribution_item_types import ContributionItemTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ContributionItemTypes from a JSON string
contribution_item_types_instance = ContributionItemTypes.from_json(json)
# print the JSON string representation of the object
print(ContributionItemTypes.to_json())

# convert the object into a dict
contribution_item_types_dict = contribution_item_types_instance.to_dict()
# create an instance of ContributionItemTypes from a dict
contribution_item_types_from_dict = ContributionItemTypes.from_dict(contribution_item_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


