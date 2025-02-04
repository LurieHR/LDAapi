# ListLobbyists200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[LobbyistWithRegistrant]**](LobbyistWithRegistrant.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_lobbyists200_response import ListLobbyists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListLobbyists200Response from a JSON string
list_lobbyists200_response_instance = ListLobbyists200Response.from_json(json)
# print the JSON string representation of the object
print(ListLobbyists200Response.to_json())

# convert the object into a dict
list_lobbyists200_response_dict = list_lobbyists200_response_instance.to_dict()
# create an instance of ListLobbyists200Response from a dict
list_lobbyists200_response_from_dict = ListLobbyists200Response.from_dict(list_lobbyists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


