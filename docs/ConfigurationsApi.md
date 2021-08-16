# gewv_sides_client.ConfigurationsApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_file**](ConfigurationsApi.md#create_configuration_file) | **POST** /applications/{applicationName}/configs/{configurationFilename} | 
[**get_configuration_file**](ConfigurationsApi.md#get_configuration_file) | **GET** /applications/{applicationName}/configs/{configurationFilename} | 
[**update_configuration_file**](ConfigurationsApi.md#update_configuration_file) | **PUT** /applications/{applicationName}/configs/{configurationFilename} | 


# **create_configuration_file**
> create_configuration_file(application_name, configuration_filename)



Create a new configuration file.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import configurations_api
from pprint import pprint
# Defining the host is optional and defaults to https://tek-ekg.iet.mw.tu-dresden.de/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gewv_sides_client.Configuration(
    host = "https://tek-ekg.iet.mw.tu-dresden.de/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = gewv_sides_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with gewv_sides_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurations_api.ConfigurationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    configuration_filename = "mqtt.yml" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_configuration_file(application_name, configuration_filename)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->create_configuration_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **configuration_filename** | **str**|  |

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
**200** | Created a new configuration file. |  -  |
**400** | Invalid application or application dont exists. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_file**
> get_configuration_file(application_name, configuration_filename)



Get configuration file of the application.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import configurations_api
from pprint import pprint
# Defining the host is optional and defaults to https://tek-ekg.iet.mw.tu-dresden.de/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gewv_sides_client.Configuration(
    host = "https://tek-ekg.iet.mw.tu-dresden.de/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = gewv_sides_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with gewv_sides_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurations_api.ConfigurationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    configuration_filename = "mqtt.yml" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_configuration_file(application_name, configuration_filename)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->get_configuration_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **configuration_filename** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration file |  -  |
**404** | Application has no file or dont exist. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration_file**
> update_configuration_file(application_name, configuration_filename)



Update a configuration.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import configurations_api
from pprint import pprint
# Defining the host is optional and defaults to https://tek-ekg.iet.mw.tu-dresden.de/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gewv_sides_client.Configuration(
    host = "https://tek-ekg.iet.mw.tu-dresden.de/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = gewv_sides_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with gewv_sides_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurations_api.ConfigurationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    configuration_filename = "mqtt.yml" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_configuration_file(application_name, configuration_filename)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->update_configuration_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **configuration_filename** | **str**|  |

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
**200** | Updated the configuration. |  -  |
**404** | Invalid application or application dont exists. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

