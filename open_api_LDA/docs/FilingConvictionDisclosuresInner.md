# FilingConvictionDisclosuresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lobbyist** | [**FilingLobbyingActivitiesInnerLobbyistsInnerLobbyist**](FilingLobbyingActivitiesInnerLobbyistsInnerLobbyist.md) |  | [optional] 
**var_date** | **date** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.filing_conviction_disclosures_inner import FilingConvictionDisclosuresInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilingConvictionDisclosuresInner from a JSON string
filing_conviction_disclosures_inner_instance = FilingConvictionDisclosuresInner.from_json(json)
# print the JSON string representation of the object
print(FilingConvictionDisclosuresInner.to_json())

# convert the object into a dict
filing_conviction_disclosures_inner_dict = filing_conviction_disclosures_inner_instance.to_dict()
# create an instance of FilingConvictionDisclosuresInner from a dict
filing_conviction_disclosures_inner_from_dict = FilingConvictionDisclosuresInner.from_dict(filing_conviction_disclosures_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


