# gewv_sides_client.MetersApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reading**](MetersApi.md#create_reading) | **POST** /meters/{meterId}/readings | 
[**delete_reading**](MetersApi.md#delete_reading) | **DELETE** /meters/{meterId}/readings/{readingId} | 
[**get_readings**](MetersApi.md#get_readings) | **GET** /meters/{meterId}/readings | 
[**upsert_reading**](MetersApi.md#upsert_reading) | **POST** /meters/{meterId}/readings/{readingId} | 


# **create_reading**
> Reading create_reading(meter_id, reading)



Create a new reading for a meter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import meters_api
from gewv_sides_client.model.reading import Reading
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
    api_instance = meters_api.MetersApi(api_client)
    meter_id = ID(1) # ID | 
    reading = Reading(
        count=3.14,
        date="date_example",
    ) # Reading | The new reading, that will be created!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_reading(meter_id, reading)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling MetersApi->create_reading: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id** | **ID**|  |
 **reading** | [**Reading**](Reading.md)| The new reading, that will be created! |

### Return type

[**Reading**](Reading.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new reading object |  -  |
**400** | Invalid new reading object. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reading**
> Building delete_reading(meter_id, reading_id)



Delete a reading of a meter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import meters_api
from gewv_sides_client.model.building import Building
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
    api_instance = meters_api.MetersApi(api_client)
    meter_id = ID(1) # ID | 
    reading_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_reading(meter_id, reading_id)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling MetersApi->delete_reading: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id** | **ID**|  |
 **reading_id** | **ID**|  |

### Return type

[**Building**](Building.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get your building object |  -  |
**400** | Invalid new building object. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_readings**
> ArrayOfReadings get_readings(meter_id)



Get all readings of meter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import meters_api
from gewv_sides_client.model.array_of_readings import ArrayOfReadings
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
    api_instance = meters_api.MetersApi(api_client)
    meter_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_readings(meter_id)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling MetersApi->get_readings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id** | **ID**|  |

### Return type

[**ArrayOfReadings**](ArrayOfReadings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of readings |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_reading**
> Reading upsert_reading(meter_id, reading_id, reading)



Create or update a new reading for a meter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import meters_api
from gewv_sides_client.model.reading import Reading
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
    api_instance = meters_api.MetersApi(api_client)
    meter_id = ID(1) # ID | 
    reading_id = ID(1) # ID | 
    reading = Reading(
        count=3.14,
        date="date_example",
    ) # Reading | The new reading, that will be created or updated!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.upsert_reading(meter_id, reading_id, reading)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling MetersApi->upsert_reading: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id** | **ID**|  |
 **reading_id** | **ID**|  |
 **reading** | [**Reading**](Reading.md)| The new reading, that will be created or updated! |

### Return type

[**Reading**](Reading.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new reading object |  -  |
**400** | Invalid new reading object. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

