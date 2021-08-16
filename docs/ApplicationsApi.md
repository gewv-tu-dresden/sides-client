# gewv_sides_client.ApplicationsApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_file**](ApplicationsApi.md#create_configuration_file) | **POST** /applications/{applicationName}/configs/{configurationFilename} | 
[**get_application**](ApplicationsApi.md#get_application) | **GET** /applications/{applicationName} | 
[**get_application_configs**](ApplicationsApi.md#get_application_configs) | **GET** /applications/{applicationName}/configs | 
[**get_application_variables**](ApplicationsApi.md#get_application_variables) | **GET** /applications/{applicationName}/variables | 
[**get_applications**](ApplicationsApi.md#get_applications) | **GET** /applications | 
[**get_configuration_file**](ApplicationsApi.md#get_configuration_file) | **GET** /applications/{applicationName}/configs/{configurationFilename} | 
[**trigger_application_action**](ApplicationsApi.md#trigger_application_action) | **POST** /applications/{applicationName}/actions | 
[**update_application_variable**](ApplicationsApi.md#update_application_variable) | **POST** /applications/{applicationName}/variables | 
[**update_configuration_file**](ApplicationsApi.md#update_configuration_file) | **PUT** /applications/{applicationName}/configs/{configurationFilename} | 


# **create_configuration_file**
> create_configuration_file(application_name, configuration_filename)



Create a new configuration file.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    configuration_filename = "mqtt.yml" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_configuration_file(application_name, configuration_filename)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->create_configuration_file: %s\n" % e)
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

# **get_application**
> get_application(application_name)



Get a application per name.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_application(application_name)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |

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
**200** | The requested application. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_configs**
> get_application_configs(application_name)



Get the list of configs of the application.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_application_configs(application_name)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_application_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configs of the application |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_variables**
> get_application_variables(application_name)



Get variables of a application.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_application_variables(application_name)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_application_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |

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
**200** | the variables |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> get_applications()



Get applications.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_applications()
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_applications: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of applications |  -  |
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
from gewv_sides_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    configuration_filename = "mqtt.yml" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_configuration_file(application_name, configuration_filename)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_configuration_file: %s\n" % e)
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

# **trigger_application_action**
> trigger_application_action(application_name, inline_object6)



Trigger a action for the application.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import applications_api
from gewv_sides_client.model.inline_object6 import InlineObject6
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    inline_object6 = InlineObject6(
        action="action_example",
    ) # InlineObject6 | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.trigger_application_action(application_name, inline_object6)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->trigger_application_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  |

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
**200** | Action was successful! |  -  |
**400** | Invalid application or application dont exists. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_variable**
> update_application_variable(application_name, inline_object4)



Update a variable of application.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import applications_api
from gewv_sides_client.model.inline_object4 import InlineObject4
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    inline_object4 = InlineObject4(
        type="tags",
        key="key_example",
        value="value_example",
    ) # InlineObject4 | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_application_variable(application_name, inline_object4)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->update_application_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  |

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
**200** | Variable updated |  -  |
**400** | Invalid parameters. |  -  |
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
from gewv_sides_client.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    configuration_filename = "mqtt.yml" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_configuration_file(application_name, configuration_filename)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling ApplicationsApi->update_configuration_file: %s\n" % e)
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

