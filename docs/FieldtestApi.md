# openapi_client.FieldtestApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fieldtest**](FieldtestApi.md#create_fieldtest) | **POST** /fieldtests | 
[**get_fieldtest**](FieldtestApi.md#get_fieldtest) | **GET** /fieldtests/{fieldtestId} | 
[**update_fieldtest**](FieldtestApi.md#update_fieldtest) | **PATCH** /fieldtests/{fieldtestId} | 


# **create_fieldtest**
> Fieldtest create_fieldtest(fieldtest)



Create a new fieldtest.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import fieldtest_api
from openapi_client.model.fieldtest import Fieldtest
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
    api_instance = fieldtest_api.FieldtestApi(api_client)
    fieldtest = Fieldtest(
        name="name_example",
        started_at="started_at_example",
        endet_at="endet_at_example",
        note="note_example",
        measurement_db_name="measurement_db_name_example",
    ) # Fieldtest | The new fieldtest, that will be created!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_fieldtest(fieldtest)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FieldtestApi->create_fieldtest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest** | [**Fieldtest**](Fieldtest.md)| The new fieldtest, that will be created! |

### Return type

[**Fieldtest**](Fieldtest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get your user object |  -  |
**400** | Invalid new fieldtest object or fieldtest with that name already exists. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fieldtest**
> get_fieldtest(fieldtest_id)



Get a fieldtest with id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import fieldtest_api
from openapi_client.model.id import ID
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
    api_instance = fieldtest_api.FieldtestApi(api_client)
    fieldtest_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_fieldtest(fieldtest_id)
    except openapi_client.ApiException as e:
        print("Exception when calling FieldtestApi->get_fieldtest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest_id** | **ID**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of fieldtests |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fieldtest**
> Fieldtest update_fieldtest(fieldtest_id, fieldtest)



Update a existing fieldtest.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import fieldtest_api
from openapi_client.model.fieldtest import Fieldtest
from openapi_client.model.id import ID
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
    api_instance = fieldtest_api.FieldtestApi(api_client)
    fieldtest_id = ID(1) # ID | 
    fieldtest = Fieldtest(
        name="name_example",
        started_at="started_at_example",
        endet_at="endet_at_example",
        note="note_example",
        measurement_db_name="measurement_db_name_example",
    ) # Fieldtest | The fieldtest to update the existing.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_fieldtest(fieldtest_id, fieldtest)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FieldtestApi->update_fieldtest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest_id** | **ID**|  |
 **fieldtest** | [**Fieldtest**](Fieldtest.md)| The fieldtest to update the existing. |

### Return type

[**Fieldtest**](Fieldtest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get your user object |  -  |
**400** | Invalid new fieldtest object or fieldtest with that name already exists. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

