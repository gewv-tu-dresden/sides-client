# openapi_client.AnalyticsApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_datalosses**](AnalyticsApi.md#get_datalosses) | **GET** /analytics/datalosses | 
[**get_standard_performance**](AnalyticsApi.md#get_standard_performance) | **GET** /analytics/standard_performance | 


# **get_datalosses**
> get_datalosses(inline_object1)



Get datalosses in percent of a time.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import analytics_api
from openapi_client.model.inline_object1 import InlineObject1
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    inline_object1 = InlineObject1(
        fieldtest_id=1,
        device_id=1,
        datapoint_name="datapoint_name_example",
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_datalosses(inline_object1)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalyticsApi->get_datalosses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Datalosses in percent per hour |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standard_performance**
> get_standard_performance(inline_object)



Get the standard performance for a device.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import analytics_api
from openapi_client.model.inline_object import InlineObject
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    inline_object = InlineObject(
        fieldtest_id=1,
        device_id=1,
        datapoint_name="datapoint_name_example",
        ref_datapoint_name="ref_datapoint_name_example",
        ref_limit="ref_limit_example",
        start_time="start_time_example",
        end_time="end_time_example",
        aggregator_method="aggregator_method_example",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_standard_performance(inline_object)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalyticsApi->get_standard_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calculated standard performance. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

