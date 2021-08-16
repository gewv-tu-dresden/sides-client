# gewv_sides_client.DevicesApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DevicesApi.md#create_device) | **POST** /buildings/{buildingId}/devices | 
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /buildings/{buildingId}/devices/{deviceId} | 
[**get_boxes_of_datapoint**](DevicesApi.md#get_boxes_of_datapoint) | **GET** /buildings/{buildingId}/devices/{deviceId}/boxes | 
[**get_datapoint_names**](DevicesApi.md#get_datapoint_names) | **GET** /buildings/{buildingId}/devices/{deviceId}/getDatapointNames | 
[**get_device**](DevicesApi.md#get_device) | **GET** /buildings/{buildingId}/devices/{deviceId} | 
[**get_devices**](DevicesApi.md#get_devices) | **GET** /buildings/{buildingId}/devices | 
[**update_device**](DevicesApi.md#update_device) | **PATCH** /buildings/{buildingId}/devices/{deviceId} | 


# **create_device**
> Device create_device(building_id, device)



Create a new device for a building.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import devices_api
from gewv_sides_client.model.device import Device
from gewv_sides_client.model.id import ID
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
    api_instance = devices_api.DevicesApi(api_client)
    building_id = ID(1) # ID | 
    device = Device(
        device_type="producer",
        energy_type=EnergyType("electrical"),
        name="name_example",
        description="description_example",
        enery_source="enery_source_example",
        energy_sink="energy_sink_example",
        power_in_kw=3.14,
        annual_power_in_kwh=3.14,
        total_capacity_in_kwh=3.14,
        manufacturer="manufacturer_example",
        model_id="model_id_example",
        note="note_example",
    ) # Device | The new device, that will be created!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_device(building_id, device)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling DevicesApi->create_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **ID**|  |
 **device** | [**Device**](Device.md)| The new device, that will be created! |

### Return type

[**Device**](Device.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get your device object |  -  |
**400** | Invalid new device object. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device(building_id, device_id)



Delete a contact.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import devices_api
from gewv_sides_client.model.id import ID
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
    api_instance = devices_api.DevicesApi(api_client)
    building_id = ID(1) # ID | 
    device_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_device(building_id, device_id)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **ID**|  |
 **device_id** | **ID**|  |

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
**200** | The device deleted |  -  |
**502** | Invalid device id |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boxes_of_datapoint**
> [Box] get_boxes_of_datapoint(building_id, device_id)



Get the connected boxes of the device.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import devices_api
from gewv_sides_client.model.box import Box
from gewv_sides_client.model.id import ID
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
    api_instance = devices_api.DevicesApi(api_client)
    building_id = ID(1) # ID | 
    device_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_boxes_of_datapoint(building_id, device_id)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling DevicesApi->get_boxes_of_datapoint: %s\n" % e)
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

# **get_datapoint_names**
> [str] get_datapoint_names(building_id, device_id)



Get datapoint names of the connected boxes.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import devices_api
from gewv_sides_client.model.id import ID
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
    api_instance = devices_api.DevicesApi(api_client)
    building_id = ID(1) # ID | 
    device_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_datapoint_names(building_id, device_id)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling DevicesApi->get_datapoint_names: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **ID**|  |
 **device_id** | **ID**|  |

### Return type

**[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of names of the datapoints |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> Device get_device(building_id, device_id, device)



Get a device.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import devices_api
from gewv_sides_client.model.device import Device
from gewv_sides_client.model.id import ID
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
    api_instance = devices_api.DevicesApi(api_client)
    building_id = ID(1) # ID | 
    device_id = ID(1) # ID | 
    device = Device(
        device_type="producer",
        energy_type=EnergyType("electrical"),
        name="name_example",
        description="description_example",
        enery_source="enery_source_example",
        energy_sink="energy_sink_example",
        power_in_kw=3.14,
        annual_power_in_kwh=3.14,
        total_capacity_in_kwh=3.14,
        manufacturer="manufacturer_example",
        model_id="model_id_example",
        note="note_example",
    ) # Device | The device to update!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device(building_id, device_id, device)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling DevicesApi->get_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **ID**|  |
 **device_id** | **ID**|  |
 **device** | [**Device**](Device.md)| The device to update! |

### Return type

[**Device**](Device.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated device |  -  |
**400** | Invalid device to update. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> ArrayOfDevices get_devices(building_id)



Get all devices of a building.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import devices_api
from gewv_sides_client.model.array_of_devices import ArrayOfDevices
from gewv_sides_client.model.id import ID
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
    api_instance = devices_api.DevicesApi(api_client)
    building_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_devices(building_id)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **ID**|  |

### Return type

[**ArrayOfDevices**](ArrayOfDevices.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of devices of a building |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> Device update_device(building_id, device_id, device)



Update a existing device.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import devices_api
from gewv_sides_client.model.device import Device
from gewv_sides_client.model.id import ID
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
    api_instance = devices_api.DevicesApi(api_client)
    building_id = ID(1) # ID | 
    device_id = ID(1) # ID | 
    device = Device(
        device_type="producer",
        energy_type=EnergyType("electrical"),
        name="name_example",
        description="description_example",
        enery_source="enery_source_example",
        energy_sink="energy_sink_example",
        power_in_kw=3.14,
        annual_power_in_kwh=3.14,
        total_capacity_in_kwh=3.14,
        manufacturer="manufacturer_example",
        model_id="model_id_example",
        note="note_example",
    ) # Device | The device to update!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_device(building_id, device_id, device)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling DevicesApi->update_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **ID**|  |
 **device_id** | **ID**|  |
 **device** | [**Device**](Device.md)| The device to update! |

### Return type

[**Device**](Device.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated device |  -  |
**400** | Invalid device to update. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

