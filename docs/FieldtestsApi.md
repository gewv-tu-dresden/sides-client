# openapi_client.FieldtestsApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fieltests**](FieldtestsApi.md#get_fieltests) | **GET** /fieldtests | 


# **get_fieltests**
> ArrayOfFieldtests get_fieltests()



Get all fieldtests.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import fieldtests_api
from openapi_client.model.array_of_fieldtests import ArrayOfFieldtests
from pprint import pprint
# Defining the host is optional and defaults to https://tek-ekg.iet.mw.tu-dresden.de/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tek-ekg.iet.mw.tu-dresden.de/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fieldtests_api.FieldtestsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_fieltests()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FieldtestsApi->get_fieltests: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfFieldtests**](ArrayOfFieldtests.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of fieldtests |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

