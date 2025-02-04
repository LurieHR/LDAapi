# FilingLobbyingActivitiesInnerLobbyistsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lobbyist** | [**FilingLobbyingActivitiesInnerLobbyistsInnerLobbyist**](FilingLobbyingActivitiesInnerLobbyistsInnerLobbyist.md) |  | [optional] 
**covered_position** | **str** |  | [optional] [readonly] 
**new** | **bool** | None indicates no data available. | [optional] [readonly] 

## Example

```python
from openapi_client.models.filing_lobbying_activities_inner_lobbyists_inner import FilingLobbyingActivitiesInnerLobbyistsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilingLobbyingActivitiesInnerLobbyistsInner from a JSON string
filing_lobbying_activities_inner_lobbyists_inner_instance = FilingLobbyingActivitiesInnerLobbyistsInner.from_json(json)
# print the JSON string representation of the object
print(FilingLobbyingActivitiesInnerLobbyistsInner.to_json())

# convert the object into a dict
filing_lobbying_activities_inner_lobbyists_inner_dict = filing_lobbying_activities_inner_lobbyists_inner_instance.to_dict()
# create an instance of FilingLobbyingActivitiesInnerLobbyistsInner from a dict
filing_lobbying_activities_inner_lobbyists_inner_from_dict = FilingLobbyingActivitiesInnerLobbyistsInner.from_dict(filing_lobbying_activities_inner_lobbyists_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


