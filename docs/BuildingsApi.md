# gewv_sides_client.BuildingsApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_building**](BuildingsApi.md#create_building) | **POST** /fieldtests/{fieldtestId}/buildings | 
[**get_buildings**](BuildingsApi.md#get_buildings) | **GET** /fieldtests/{fieldtestId}/buildings | 


# **create_building**
> Building create_building(fieldtest_id, building)



Create a new building for a fieldtest.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import buildings_api
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
    api_instance = buildings_api.BuildingsApi(api_client)
    fieldtest_id = ID(1) # ID | 
    building = Building() # Building | The new building, that will be created!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_building(fieldtest_id, building)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling BuildingsApi->create_building: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest_id** | **ID**|  |
 **building** | [**Building**](Building.md)| The new building, that will be created! |

### Return type

[**Building**](Building.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get your building object |  -  |
**400** | Invalid new building object. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buildings**
> ArrayOfBuildings get_buildings(fieldtest_id)



Get all buildings of a fieldtest.

### Example

* Basic Authentication (basicAuth):
```python
import time
import gewv_sides_client
from gewv_sides_client.api import buildings_api
from gewv_sides_client.model.array_of_buildings import ArrayOfBuildings
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
    api_instance = buildings_api.BuildingsApi(api_client)
    fieldtest_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_buildings(fieldtest_id)
        pprint(api_response)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling BuildingsApi->get_buildings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest_id** | **ID**|  |

### Return type

[**ArrayOfBuildings**](ArrayOfBuildings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of buildings of a fieldtest |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

