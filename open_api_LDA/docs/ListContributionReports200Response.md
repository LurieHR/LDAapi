# ListContributionReports200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ContributionReport]**](ContributionReport.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_contribution_reports200_response import ListContributionReports200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListContributionReports200Response from a JSON string
list_contribution_reports200_response_instance = ListContributionReports200Response.from_json(json)
# print the JSON string representation of the object
print(ListContributionReports200Response.to_json())

# convert the object into a dict
list_contribution_reports200_response_dict = list_contribution_reports200_response_instance.to_dict()
# create an instance of ListContributionReports200Response from a dict
list_contribution_reports200_response_from_dict = ListContributionReports200Response.from_dict(list_contribution_reports200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


