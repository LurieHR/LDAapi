# Registrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**url** | **str** |  | [optional] [readonly] 
**house_registrant_id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**address_1** | **str** |  | [optional] [readonly] 
**address_2** | **str** |  | [optional] [readonly] 
**address_3** | **str** |  | [optional] [readonly] 
**address_4** | **str** |  | [optional] [readonly] 
**city** | **str** |  | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 
**state_display** | **str** |  | [optional] 
**zip** | **str** |  | [optional] [readonly] 
**country** | **str** |  | [optional] [readonly] 
**country_display** | **str** |  | [optional] 
**ppb_country** | **str** |  | [optional] [readonly] 
**ppb_country_display** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] [readonly] 
**contact_telephone** | **str** |  | [optional] [readonly] 
**dt_updated** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.registrant import Registrant

# TODO update the JSON string below
json = "{}"
# create an instance of Registrant from a JSON string
registrant_instance = Registrant.from_json(json)
# print the JSON string representation of the object
print(Registrant.to_json())

# convert the object into a dict
registrant_dict = registrant_instance.to_dict()
# create an instance of Registrant from a dict
registrant_from_dict = Registrant.from_dict(registrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


