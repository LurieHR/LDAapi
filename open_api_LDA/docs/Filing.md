# Filing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] [readonly] 
**filing_uuid** | **str** |  | [optional] [readonly] 
**filing_type** | **str** |  | [optional] [readonly] 
**filing_type_display** | **str** |  | [optional] 
**filing_year** | **int** |  | [optional] [readonly] 
**filing_period** | **str** | Filing Period - Quarter | [optional] [readonly] 
**filing_period_display** | **str** |  | [optional] 
**filing_document_url** | **str** |  | [optional] [readonly] 
**filing_document_content_type** | **str** |  | [optional] [readonly] 
**income** | **decimal.Decimal** |  | [optional] [readonly] 
**expenses** | **decimal.Decimal** |  | [optional] [readonly] 
**expenses_method** | **str** |  | [optional] [readonly] 
**expenses_method_display** | **str** |  | [optional] 
**posted_by_name** | **str** |  | [optional] [readonly] 
**dt_posted** | **datetime** |  | [optional] [readonly] 
**termination_date** | **date** |  | [optional] [readonly] 
**registrant_country** | **str** |  | [optional] 
**registrant_ppb_country** | **str** |  | [optional] 
**registrant_address_1** | **str** | As listed on filing - Registrant Address 1 | [optional] [readonly] 
**registrant_address_2** | **str** | As listed on filing - Registrant Address 2 | [optional] [readonly] 
**registrant_different_address** | **bool** | As listed on filing - Registrant Different Address | [optional] [readonly] 
**registrant_city** | **str** | As listed on filing - Registrant City | [optional] [readonly] 
**registrant_state** | **str** | As listed on filing - Registrant State | [optional] [readonly] 
**registrant_zip** | **str** | As listed on filing - Registrant Zip code | [optional] [readonly] 
**registrant** | [**FilingRegistrant**](FilingRegistrant.md) |  | 
**client** | [**FilingClient**](FilingClient.md) |  | 
**lobbying_activities** | [**List[FilingLobbyingActivitiesInner]**](FilingLobbyingActivitiesInner.md) |  | 
**conviction_disclosures** | [**List[FilingConvictionDisclosuresInner]**](FilingConvictionDisclosuresInner.md) |  | 
**foreign_entities** | [**List[FilingForeignEntitiesInner]**](FilingForeignEntitiesInner.md) |  | 
**affiliated_organizations** | [**List[FilingAffiliatedOrganizationsInner]**](FilingAffiliatedOrganizationsInner.md) |  | 

## Example

```python
from openapi_client.models.filing import Filing

# TODO update the JSON string below
json = "{}"
# create an instance of Filing from a JSON string
filing_instance = Filing.from_json(json)
# print the JSON string representation of the object
print(Filing.to_json())

# convert the object into a dict
filing_dict = filing_instance.to_dict()
# create an instance of Filing from a dict
filing_from_dict = Filing.from_dict(filing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


