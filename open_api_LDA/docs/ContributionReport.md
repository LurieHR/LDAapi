# ContributionReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] [readonly] 
**filing_uuid** | **str** |  | [optional] [readonly] 
**filing_type** | **str** |  | [optional] [readonly] 
**filing_type_display** | **str** |  | [optional] 
**filing_year** | **int** |  | [optional] [readonly] 
**filing_period** | **str** |  | [optional] [readonly] 
**filing_period_display** | **str** |  | [optional] 
**filing_document_url** | **str** |  | [optional] [readonly] 
**filing_document_content_type** | **str** |  | [optional] [readonly] 
**filer_type** | **str** |  | [optional] [readonly] 
**filer_type_display** | **str** |  | [optional] 
**dt_posted** | **datetime** |  | [optional] [readonly] 
**contact_name** | **str** |  | [optional] [readonly] 
**comments** | **str** |  | [optional] [readonly] 
**address_1** | **str** |  | [optional] [readonly] 
**address_2** | **str** |  | [optional] [readonly] 
**city** | **str** |  | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 
**state_display** | **str** |  | [optional] 
**zip** | **str** |  | [optional] [readonly] 
**country** | **str** |  | [optional] [readonly] 
**country_display** | **str** |  | [optional] 
**registrant** | [**ContributionReportRegistrant**](ContributionReportRegistrant.md) |  | [optional] 
**lobbyist** | [**FilingLobbyingActivitiesInnerLobbyistsInnerLobbyist**](FilingLobbyingActivitiesInnerLobbyistsInnerLobbyist.md) |  | [optional] 
**no_contributions** | **bool** |  | [optional] [readonly] 
**pacs** | **List[str]** |  | [optional] [readonly] 
**contribution_items** | [**List[ContributionReportContributionItemsInner]**](ContributionReportContributionItemsInner.md) |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.contribution_report import ContributionReport

# TODO update the JSON string below
json = "{}"
# create an instance of ContributionReport from a JSON string
contribution_report_instance = ContributionReport.from_json(json)
# print the JSON string representation of the object
print(ContributionReport.to_json())

# convert the object into a dict
contribution_report_dict = contribution_report_instance.to_dict()
# create an instance of ContributionReport from a dict
contribution_report_from_dict = ContributionReport.from_dict(contribution_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


