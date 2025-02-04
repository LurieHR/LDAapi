# ContributionReportContributionItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contribution_type** | **str** |  | [optional] [readonly] 
**contribution_type_display** | **str** |  | [optional] 
**contributor_name** | **str** |  | [optional] [readonly] 
**payee_name** | **str** |  | [optional] [readonly] 
**honoree_name** | **str** |  | [optional] [readonly] 
**amount** | **decimal.Decimal** |  | [optional] [readonly] 
**var_date** | **date** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.contribution_report_contribution_items_inner import ContributionReportContributionItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContributionReportContributionItemsInner from a JSON string
contribution_report_contribution_items_inner_instance = ContributionReportContributionItemsInner.from_json(json)
# print the JSON string representation of the object
print(ContributionReportContributionItemsInner.to_json())

# convert the object into a dict
contribution_report_contribution_items_inner_dict = contribution_report_contribution_items_inner_instance.to_dict()
# create an instance of ContributionReportContributionItemsInner from a dict
contribution_report_contribution_items_inner_from_dict = ContributionReportContributionItemsInner.from_dict(contribution_report_contribution_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


