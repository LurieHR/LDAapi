# FilingLobbyingActivitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_issue_code** | **str** |  | [optional] [readonly] 
**general_issue_code_display** | **str** |  | [optional] 
**description** | **str** |  | [optional] [readonly] 
**foreign_entity_issues** | **str** |  | [optional] [readonly] 
**lobbyists** | [**List[FilingLobbyingActivitiesInnerLobbyistsInner]**](FilingLobbyingActivitiesInnerLobbyistsInner.md) |  | [optional] [readonly] 
**government_entities** | [**List[FilingLobbyingActivitiesInnerGovernmentEntitiesInner]**](FilingLobbyingActivitiesInnerGovernmentEntitiesInner.md) |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.filing_lobbying_activities_inner import FilingLobbyingActivitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilingLobbyingActivitiesInner from a JSON string
filing_lobbying_activities_inner_instance = FilingLobbyingActivitiesInner.from_json(json)
# print the JSON string representation of the object
print(FilingLobbyingActivitiesInner.to_json())

# convert the object into a dict
filing_lobbying_activities_inner_dict = filing_lobbying_activities_inner_instance.to_dict()
# create an instance of FilingLobbyingActivitiesInner from a dict
filing_lobbying_activities_inner_from_dict = FilingLobbyingActivitiesInner.from_dict(filing_lobbying_activities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


