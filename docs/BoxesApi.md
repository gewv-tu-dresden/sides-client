# openapi_client.BoxesApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_box**](BoxesApi.md#create_box) | **POST** /boxes | 
[**create_log**](BoxesApi.md#create_log) | **POST** /boxes/{boxId}/measur_services/{measurServiceId}/log | 
[**create_measur_service**](BoxesApi.md#create_measur_service) | **POST** /boxes/{boxId}/measur_services | 
[**delete_application_variable**](BoxesApi.md#delete_application_variable) | **DELETE** /applications/{applicationName}/variables | 
[**delete_box**](BoxesApi.md#delete_box) | **DELETE** /boxes/{boxId} | 
[**delete_box_variable**](BoxesApi.md#delete_box_variable) | **DELETE** /boxes/{boxId}/variables | 
[**delete_measur_service**](BoxesApi.md#delete_measur_service) | **DELETE** /boxes/{boxId}/measur_services/{measurServiceId} | 
[**get_box**](BoxesApi.md#get_box) | **GET** /boxes/{boxId} | 
[**get_box_config**](BoxesApi.md#get_box_config) | **GET** /boxes/{boxId}/config | 
[**get_box_device**](BoxesApi.md#get_box_device) | **GET** /boxes/{boxId}/device | 
[**get_box_legacy**](BoxesApi.md#get_box_legacy) | **GET** /boxes_legacy/{boxId} | 
[**get_box_variables**](BoxesApi.md#get_box_variables) | **GET** /boxes/{boxId}/variables | 
[**get_boxes**](BoxesApi.md#get_boxes) | **GET** /boxes | 
[**get_boxes_legacy**](BoxesApi.md#get_boxes_legacy) | **GET** /boxes_legacy | 
[**get_boxes_of_datapoint**](BoxesApi.md#get_boxes_of_datapoint) | **GET** /buildings/{buildingId}/devices/{deviceId}/boxes | 
[**get_logs**](BoxesApi.md#get_logs) | **GET** /boxes/{boxId}/measur_services/{measurServiceId}/log | 
[**get_measur_service**](BoxesApi.md#get_measur_service) | **GET** /boxes/{boxId}/measur_services/{measurServiceId} | 
[**get_measur_services**](BoxesApi.md#get_measur_services) | **GET** /boxes/{boxId}/measur_services | 
[**update_box**](BoxesApi.md#update_box) | **PATCH** /boxes/{boxId} | 
[**update_box_variable**](BoxesApi.md#update_box_variable) | **POST** /boxes/{boxId}/variables | 
[**update_measur_service**](BoxesApi.md#update_measur_service) | **PATCH** /boxes/{boxId}/measur_services/{measurServiceId} | 


# **create_box**
> Box create_box(box_prototype)



Create a new box.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.box_prototype import BoxPrototype
from openapi_client.model.box import Box
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_prototype = BoxPrototype(
        hardware_id="hardware_id_example",
        name="name_example",
        is_online=True,
        last_seen="last_seen_example",
        energy_type=EnergyType("electrical"),
    ) # BoxPrototype | The new box, that will be created!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_box(box_prototype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->create_box: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_prototype** | [**BoxPrototype**](BoxPrototype.md)| The new box, that will be created! |

### Return type

[**Box**](Box.md)

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

# **create_log**
> Log create_log(box_id, measur_service_id, log_prototype)



Create a new log for a service.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.log import Log
from openapi_client.model.log_prototype import LogPrototype
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    measur_service_id = ID(1) # ID | 
    log_prototype = LogPrototype(
        level=LogLevel("CRITICAL"),
        message="message_example",
        emitted_at="emitted_at_example",
    ) # LogPrototype | The new log that will be created!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_log(box_id, measur_service_id, log_prototype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->create_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **measur_service_id** | **ID**|  |
 **log_prototype** | [**LogPrototype**](LogPrototype.md)| The new log that will be created! |

### Return type

[**Log**](Log.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created log. |  -  |
**400** | Invalid new log object. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_measur_service**
> MeasurService create_measur_service(box_id, measur_service_prototype)



Create new service for a box

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.measur_service import MeasurService
from openapi_client.model.measur_service_prototype import MeasurServicePrototype
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    measur_service_prototype = MeasurServicePrototype() # MeasurServicePrototype | The new service, that will be created!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_measur_service(box_id, measur_service_prototype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->create_measur_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **measur_service_prototype** | [**MeasurServicePrototype**](MeasurServicePrototype.md)| The new service, that will be created! |

### Return type

[**MeasurService**](MeasurService.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of contacts of a fieldtest |  -  |
**400** | Invalid parameters. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_variable**
> delete_application_variable(application_name, inline_object5)



Delete a variable of application.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.inline_object5 import InlineObject5
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
    api_instance = boxes_api.BoxesApi(api_client)
    application_name = "TEK_EKG_EL" # str | 
    inline_object5 = InlineObject5(
        type="tags",
        key="key_example",
    ) # InlineObject5 | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_application_variable(application_name, inline_object5)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->delete_application_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  |
 **inline_object5** | [**InlineObject5**](InlineObject5.md)|  |

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
**200** | Variable deleted. |  -  |
**400** | Invalid parameter. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_box**
> delete_box(box_id)



Delete a box

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_box(box_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->delete_box: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |

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
**200** | Delete successful |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_box_variable**
> delete_box_variable(box_id, inline_object3)



Delete a variable of box.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.inline_object3 import InlineObject3
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    inline_object3 = InlineObject3(
        type="tags",
        key="key_example",
    ) # InlineObject3 | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_box_variable(box_id, inline_object3)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->delete_box_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  |

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
**200** | Variable deleted. |  -  |
**400** | Invalid parameter. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_measur_service**
> delete_measur_service(box_id, measur_service_id)



Delete a measure service.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    measur_service_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_measur_service(box_id, measur_service_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->delete_measur_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **measur_service_id** | **ID**|  |

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
**200** | The measur service deleted |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_box**
> Box get_box(box_id)



Get a box per id

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.box import Box
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_box(box_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_box: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |

### Return type

[**Box**](Box.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request box |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_box_config**
> get_box_config(box_id)



Get config of a box.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_box_config(box_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_box_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |

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
**200** | Requested configuration |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_box_device**
> get_box_device(box_id)



Get the belonging device of the box.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_box_device(box_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_box_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |

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
**200** | the device |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_box_legacy**
> get_box_legacy(box_id)



Get a box per id

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = "67ebc7ac3af684556421420dbb6570be" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_box_legacy(box_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_box_legacy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **str**|  |

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
**200** | The request box |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_box_variables**
> get_box_variables(box_id)



Get variables of a box.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_box_variables(box_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_box_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |

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

# **get_boxes**
> ArrayOfBoxes get_boxes()



Get boxes.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.array_of_boxes import ArrayOfBoxes
from openapi_client.model.energy_type import EnergyType
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
    api_instance = boxes_api.BoxesApi(api_client)
    enery_type = EnergyType("electrical") # EnergyType | the energy type of the device (optional)
    hardware_id = "hardware_id_example" # str | The hardware id of a box (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_boxes(enery_type=enery_type, hardware_id=hardware_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_boxes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enery_type** | **EnergyType**| the energy type of the device | [optional]
 **hardware_id** | **str**| The hardware id of a box | [optional]

### Return type

[**ArrayOfBoxes**](ArrayOfBoxes.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of boxes |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boxes_legacy**
> ArrayOfFieldtests get_boxes_legacy()



Get boxes.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.array_of_fieldtests import ArrayOfFieldtests
from openapi_client.model.energy_type import EnergyType
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
    api_instance = boxes_api.BoxesApi(api_client)
    enery_type = EnergyType("electrical") # EnergyType | the energy type of the device (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_boxes_legacy(enery_type=enery_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_boxes_legacy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enery_type** | **EnergyType**| the energy type of the device | [optional]

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
**200** | Get a list of boxes |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boxes_of_datapoint**
> [Box] get_boxes_of_datapoint(building_id, device_id)



Get the connected boxes of the device.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.box import Box
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
    api_instance = boxes_api.BoxesApi(api_client)
    building_id = ID(1) # ID | 
    device_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_boxes_of_datapoint(building_id, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_boxes_of_datapoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **ID**|  |
 **device_id** | **ID**|  |

### Return type

[**[Box]**](Box.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the request boxes of the device |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> ArrayOfLogs get_logs(box_id, measur_service_id)



Get all logs of a service.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.array_of_logs import ArrayOfLogs
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    measur_service_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_logs(box_id, measur_service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **measur_service_id** | **ID**|  |

### Return type

[**ArrayOfLogs**](ArrayOfLogs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs of a service |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measur_service**
> MeasurService get_measur_service(box_id, measur_service_id)



Get the service with the service id

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.measur_service import MeasurService
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    measur_service_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_measur_service(box_id, measur_service_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_measur_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **measur_service_id** | **ID**|  |

### Return type

[**MeasurService**](MeasurService.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested measur service! |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measur_services**
> ArrayOfMeasurServices get_measur_services(box_id)



Get services of a box.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.array_of_measur_services import ArrayOfMeasurServices
from openapi_client.model.service_type import ServiceType
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    service_type = ServiceType("modbus-tcp") # ServiceType | the type of measur service (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_measur_services(box_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_measur_services: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_measur_services(box_id, service_type=service_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->get_measur_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **service_type** | **ServiceType**| the type of measur service | [optional]

### Return type

[**ArrayOfMeasurServices**](ArrayOfMeasurServices.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of measur services of a box |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_box**
> Box update_box(box_id, box_prototype)



Update a box

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.box_prototype import BoxPrototype
from openapi_client.model.box import Box
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    box_prototype = BoxPrototype(
        hardware_id="hardware_id_example",
        name="name_example",
        is_online=True,
        last_seen="last_seen_example",
        energy_type=EnergyType("electrical"),
    ) # BoxPrototype | The update of the box!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_box(box_id, box_prototype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->update_box: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **box_prototype** | [**BoxPrototype**](BoxPrototype.md)| The update of the box! |

### Return type

[**Box**](Box.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update successful |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_box_variable**
> update_box_variable(box_id, inline_object2)



Update a variable of box.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.inline_object2 import InlineObject2
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    inline_object2 = InlineObject2(
        type="tags",
        key="key_example",
        value="value_example",
    ) # InlineObject2 | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_box_variable(box_id, inline_object2)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->update_box_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  |

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

# **update_measur_service**
> MeasurService update_measur_service(box_id, measur_service_id, measur_service_update)



Update a existing measure service.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import boxes_api
from openapi_client.model.measur_service_update import MeasurServiceUpdate
from openapi_client.model.measur_service import MeasurService
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
    api_instance = boxes_api.BoxesApi(api_client)
    box_id = ID(1) # ID | 
    measur_service_id = ID(1) # ID | 
    measur_service_update = MeasurServiceUpdate(
        state=ServiceState("RUNNING"),
        messages_queue_size=3.14,
        running_async_tasks=3.14,
        memory_usage=3.14,
        cpu_usage=3.14,
        last_seen="last_seen_example",
    ) # MeasurServiceUpdate | The measur service update!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_measur_service(box_id, measur_service_id, measur_service_update)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BoxesApi->update_measur_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_id** | **ID**|  |
 **measur_service_id** | **ID**|  |
 **measur_service_update** | [**MeasurServiceUpdate**](MeasurServiceUpdate.md)| The measur service update! |

### Return type

[**MeasurService**](MeasurService.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated measure service |  -  |
**400** | Invalid service update. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

