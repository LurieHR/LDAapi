# LobbyistWithRegistrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**prefix** | **str** |  | [optional] [readonly] 
**prefix_display** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] [readonly] 
**nickname** | **str** |  | [optional] [readonly] 
**middle_name** | **str** |  | [optional] [readonly] 
**last_name** | **str** |  | [optional] [readonly] 
**suffix** | **str** |  | [optional] [readonly] 
**suffix_display** | **str** |  | [optional] 
**registrant** | [**ContributionReportRegistrant**](ContributionReportRegistrant.md) |  | [optional] 

## Example

```python
from openapi_client.models.lobbyist_with_registrant import LobbyistWithRegistrant

# TODO update the JSON string below
json = "{}"
# create an instance of LobbyistWithRegistrant from a JSON string
lobbyist_with_registrant_instance = LobbyistWithRegistrant.from_json(json)
# print the JSON string representation of the object
print(LobbyistWithRegistrant.to_json())

# convert the object into a dict
lobbyist_with_registrant_dict = lobbyist_with_registrant_instance.to_dict()
# create an instance of LobbyistWithRegistrant from a dict
lobbyist_with_registrant_from_dict = LobbyistWithRegistrant.from_dict(lobbyist_with_registrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


