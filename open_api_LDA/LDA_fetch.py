import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint


# Retrieve the API key from the environment variable
mykeyis = os.getenv("LDA_API_KEY")
# Configure the client
configuration = openapi_client.Configuration(
    host="https://lda.senate.gov"
)
# Set the API key
configuration.api_key['ApiKeyAuth'] = f'Token {mykeyis}'

# Create an instance of the API class
api_instance = openapi_client.FilingsApi(openapi_client.ApiClient(configuration))

try:
    # Get a single page of filings from 2023
    api_response_2023 = api_instance.list_filings(
        filing_year=2023,
        page=1,
        page_size=25  # Maximum allowed
    )
    
    print("Number of results for 2023:", api_response_2023.count)
    print("\nFirst few results for 2023:")
    for filing in api_response_2023.results[:3]:  # Print first 3 results
        print(f"\nFiling ID: {filing.filing_uuid}")
        print(f"Filing Type: {filing.filing_type_display}")
        print(f"Date Posted: {filing.dt_posted}")
        if filing.registrant:
            print(f"Registrant: {filing.registrant.name}")
        if filing.client:
            print(f"Client: {filing.client.name}")

    # Search for filings with the term "potato" in lobbying activities across any year
    api_response_potato = api_instance.list_filings(
        filing_specific_lobbying_issues="potato",  # Assuming this is the correct field
        page=1,
        page_size=25  # Maximum allowed
    )
    
    print("\nNumber of results for 'potato':", api_response_potato.count)
    print("\nFirst few results for 'potato':")
    for filing in api_response_potato.results[:3]:  # Print first 3 results
        print(f"\nFiling ID: {filing.filing_uuid}")
        print(f"Filing Type: {filing.filing_type_display}")
        print(f"Date Posted: {filing.dt_posted}")
        if filing.registrant:
            print(f"Registrant: {filing.registrant.name}")
        if filing.client:
            print(f"Client: {filing.client.name}")

    # Get detailed information about a specific filing
    filing_uuid = "72e7f75e-bd77-4745-b90e-1eb517935cd0"
    detailed_filing = api_instance.retrieve_filing(filing_uuid)  # Use the correct method

    print("\nDetailed information for filing ID:", filing_uuid)
    pprint(detailed_filing)

    # Assuming detailed_filing is the object returned by retrieve_filing
    pdf_url = detailed_filing.filing_document_url
    print("PDF Document URL:", pdf_url)
            
except ApiException as e:
    print(f"Exception when calling FilingsApi: {e}\n")