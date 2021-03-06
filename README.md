# gewv-sides-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.2
- Package version: 1.0.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import gewv_sides_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gewv_sides_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import gewv_sides_client
from pprint import pprint
from gewv_sides_client.api import analytics_api
from gewv_sides_client.model.inline_object import InlineObject
from gewv_sides_client.model.inline_object1 import InlineObject1
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    inline_object1 = InlineObject1(
        fieldtest_id=1,
        device_id=1,
        datapoint_name="datapoint_name_example",
    ) # InlineObject1 | 

    try:
        api_instance.get_datalosses(inline_object1)
    except gewv_sides_client.ApiException as e:
        print("Exception when calling AnalyticsApi->get_datalosses: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalyticsApi* | [**get_datalosses**](docs/AnalyticsApi.md#get_datalosses) | **GET** /analytics/datalosses | 
*AnalyticsApi* | [**get_standard_performance**](docs/AnalyticsApi.md#get_standard_performance) | **GET** /analytics/standard_performance | 
*ApplicationsApi* | [**create_configuration_file**](docs/ApplicationsApi.md#create_configuration_file) | **POST** /applications/{applicationName}/configs/{configurationFilename} | 
*ApplicationsApi* | [**get_application**](docs/ApplicationsApi.md#get_application) | **GET** /applications/{applicationName} | 
*ApplicationsApi* | [**get_application_configs**](docs/ApplicationsApi.md#get_application_configs) | **GET** /applications/{applicationName}/configs | 
*ApplicationsApi* | [**get_application_variables**](docs/ApplicationsApi.md#get_application_variables) | **GET** /applications/{applicationName}/variables | 
*ApplicationsApi* | [**get_applications**](docs/ApplicationsApi.md#get_applications) | **GET** /applications | 
*ApplicationsApi* | [**get_configuration_file**](docs/ApplicationsApi.md#get_configuration_file) | **GET** /applications/{applicationName}/configs/{configurationFilename} | 
*ApplicationsApi* | [**trigger_application_action**](docs/ApplicationsApi.md#trigger_application_action) | **POST** /applications/{applicationName}/actions | 
*ApplicationsApi* | [**update_application_variable**](docs/ApplicationsApi.md#update_application_variable) | **POST** /applications/{applicationName}/variables | 
*ApplicationsApi* | [**update_configuration_file**](docs/ApplicationsApi.md#update_configuration_file) | **PUT** /applications/{applicationName}/configs/{configurationFilename} | 
*AuthApi* | [**login**](docs/AuthApi.md#login) | **GET** /auth/gewv/login | 
*AuthApi* | [**logout**](docs/AuthApi.md#logout) | **GET** /auth/gewv/logout | 
*BoxesApi* | [**create_box**](docs/BoxesApi.md#create_box) | **POST** /boxes | 
*BoxesApi* | [**create_log**](docs/BoxesApi.md#create_log) | **POST** /boxes/{boxId}/measur_services/{measurServiceId}/log | 
*BoxesApi* | [**create_measur_service**](docs/BoxesApi.md#create_measur_service) | **POST** /boxes/{boxId}/measur_services | 
*BoxesApi* | [**delete_application_variable**](docs/BoxesApi.md#delete_application_variable) | **DELETE** /applications/{applicationName}/variables | 
*BoxesApi* | [**delete_box**](docs/BoxesApi.md#delete_box) | **DELETE** /boxes/{boxId} | 
*BoxesApi* | [**delete_box_variable**](docs/BoxesApi.md#delete_box_variable) | **DELETE** /boxes/{boxId}/variables | 
*BoxesApi* | [**delete_measur_service**](docs/BoxesApi.md#delete_measur_service) | **DELETE** /boxes/{boxId}/measur_services/{measurServiceId} | 
*BoxesApi* | [**get_box**](docs/BoxesApi.md#get_box) | **GET** /boxes/{boxId} | 
*BoxesApi* | [**get_box_config**](docs/BoxesApi.md#get_box_config) | **GET** /boxes/{boxId}/config | 
*BoxesApi* | [**get_box_device**](docs/BoxesApi.md#get_box_device) | **GET** /boxes/{boxId}/device | 
*BoxesApi* | [**get_box_legacy**](docs/BoxesApi.md#get_box_legacy) | **GET** /boxes_legacy/{boxId} | 
*BoxesApi* | [**get_box_variables**](docs/BoxesApi.md#get_box_variables) | **GET** /boxes/{boxId}/variables | 
*BoxesApi* | [**get_boxes**](docs/BoxesApi.md#get_boxes) | **GET** /boxes | 
*BoxesApi* | [**get_boxes_legacy**](docs/BoxesApi.md#get_boxes_legacy) | **GET** /boxes_legacy | 
*BoxesApi* | [**get_boxes_of_datapoint**](docs/BoxesApi.md#get_boxes_of_datapoint) | **GET** /buildings/{buildingId}/devices/{deviceId}/boxes | 
*BoxesApi* | [**get_logs**](docs/BoxesApi.md#get_logs) | **GET** /boxes/{boxId}/measur_services/{measurServiceId}/log | 
*BoxesApi* | [**get_measur_service**](docs/BoxesApi.md#get_measur_service) | **GET** /boxes/{boxId}/measur_services/{measurServiceId} | 
*BoxesApi* | [**get_measur_services**](docs/BoxesApi.md#get_measur_services) | **GET** /boxes/{boxId}/measur_services | 
*BoxesApi* | [**update_box**](docs/BoxesApi.md#update_box) | **PATCH** /boxes/{boxId} | 
*BoxesApi* | [**update_box_variable**](docs/BoxesApi.md#update_box_variable) | **POST** /boxes/{boxId}/variables | 
*BoxesApi* | [**update_measur_service**](docs/BoxesApi.md#update_measur_service) | **PATCH** /boxes/{boxId}/measur_services/{measurServiceId} | 
*BuildingsApi* | [**create_building**](docs/BuildingsApi.md#create_building) | **POST** /fieldtests/{fieldtestId}/buildings | 
*BuildingsApi* | [**get_buildings**](docs/BuildingsApi.md#get_buildings) | **GET** /fieldtests/{fieldtestId}/buildings | 
*ConfigurationsApi* | [**create_configuration_file**](docs/ConfigurationsApi.md#create_configuration_file) | **POST** /applications/{applicationName}/configs/{configurationFilename} | 
*ConfigurationsApi* | [**get_configuration_file**](docs/ConfigurationsApi.md#get_configuration_file) | **GET** /applications/{applicationName}/configs/{configurationFilename} | 
*ConfigurationsApi* | [**update_configuration_file**](docs/ConfigurationsApi.md#update_configuration_file) | **PUT** /applications/{applicationName}/configs/{configurationFilename} | 
*ContactsApi* | [**create_contact**](docs/ContactsApi.md#create_contact) | **POST** /fieldtests/{fieldtestId}/contacts | 
*ContactsApi* | [**delete_contact**](docs/ContactsApi.md#delete_contact) | **DELETE** /fieldtests/{fieldtestId}/contacts/{contactId} | 
*ContactsApi* | [**get_contacts**](docs/ContactsApi.md#get_contacts) | **GET** /fieldtests/{fieldtestId}/contacts | 
*ContactsApi* | [**update_contact**](docs/ContactsApi.md#update_contact) | **PATCH** /fieldtests/{fieldtestId}/contacts/{contactId} | 
*DevicesApi* | [**create_device**](docs/DevicesApi.md#create_device) | **POST** /buildings/{buildingId}/devices | 
*DevicesApi* | [**delete_device**](docs/DevicesApi.md#delete_device) | **DELETE** /buildings/{buildingId}/devices/{deviceId} | 
*DevicesApi* | [**get_boxes_of_datapoint**](docs/DevicesApi.md#get_boxes_of_datapoint) | **GET** /buildings/{buildingId}/devices/{deviceId}/boxes | 
*DevicesApi* | [**get_datapoint_names**](docs/DevicesApi.md#get_datapoint_names) | **GET** /buildings/{buildingId}/devices/{deviceId}/getDatapointNames | 
*DevicesApi* | [**get_device**](docs/DevicesApi.md#get_device) | **GET** /buildings/{buildingId}/devices/{deviceId} | 
*DevicesApi* | [**get_devices**](docs/DevicesApi.md#get_devices) | **GET** /buildings/{buildingId}/devices | 
*DevicesApi* | [**update_device**](docs/DevicesApi.md#update_device) | **PATCH** /buildings/{buildingId}/devices/{deviceId} | 
*FieldtestApi* | [**create_fieldtest**](docs/FieldtestApi.md#create_fieldtest) | **POST** /fieldtests | 
*FieldtestApi* | [**get_fieldtest**](docs/FieldtestApi.md#get_fieldtest) | **GET** /fieldtests/{fieldtestId} | 
*FieldtestApi* | [**update_fieldtest**](docs/FieldtestApi.md#update_fieldtest) | **PATCH** /fieldtests/{fieldtestId} | 
*FieldtestsApi* | [**get_fieltests**](docs/FieldtestsApi.md#get_fieltests) | **GET** /fieldtests | 
*MetersApi* | [**create_reading**](docs/MetersApi.md#create_reading) | **POST** /meters/{meterId}/readings | 
*MetersApi* | [**delete_reading**](docs/MetersApi.md#delete_reading) | **DELETE** /meters/{meterId}/readings/{readingId} | 
*MetersApi* | [**get_readings**](docs/MetersApi.md#get_readings) | **GET** /meters/{meterId}/readings | 
*MetersApi* | [**upsert_reading**](docs/MetersApi.md#upsert_reading) | **POST** /meters/{meterId}/readings/{readingId} | 
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /user | 


## Documentation For Models

 - [ArrayOfBoxes](docs/ArrayOfBoxes.md)
 - [ArrayOfBuildings](docs/ArrayOfBuildings.md)
 - [ArrayOfContacts](docs/ArrayOfContacts.md)
 - [ArrayOfDevices](docs/ArrayOfDevices.md)
 - [ArrayOfFieldtests](docs/ArrayOfFieldtests.md)
 - [ArrayOfLogs](docs/ArrayOfLogs.md)
 - [ArrayOfMeasurServices](docs/ArrayOfMeasurServices.md)
 - [ArrayOfReadings](docs/ArrayOfReadings.md)
 - [Box](docs/Box.md)
 - [BoxAllOf](docs/BoxAllOf.md)
 - [BoxPrototype](docs/BoxPrototype.md)
 - [Building](docs/Building.md)
 - [BuildingAllOf](docs/BuildingAllOf.md)
 - [BuildingPrototype](docs/BuildingPrototype.md)
 - [Contact](docs/Contact.md)
 - [ContactAllOf](docs/ContactAllOf.md)
 - [ContactPrototype](docs/ContactPrototype.md)
 - [Device](docs/Device.md)
 - [EnergyType](docs/EnergyType.md)
 - [Fieldtest](docs/Fieldtest.md)
 - [FieldtestAllOf](docs/FieldtestAllOf.md)
 - [FieldtestPrototype](docs/FieldtestPrototype.md)
 - [ID](docs/ID.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [InlineObject6](docs/InlineObject6.md)
 - [Log](docs/Log.md)
 - [LogAllOf](docs/LogAllOf.md)
 - [LogLevel](docs/LogLevel.md)
 - [LogPrototype](docs/LogPrototype.md)
 - [MeasurService](docs/MeasurService.md)
 - [MeasurServiceAllOf](docs/MeasurServiceAllOf.md)
 - [MeasurServicePrototype](docs/MeasurServicePrototype.md)
 - [MeasurServicePrototypeAllOf](docs/MeasurServicePrototypeAllOf.md)
 - [MeasurServiceUpdate](docs/MeasurServiceUpdate.md)
 - [Reading](docs/Reading.md)
 - [ServiceState](docs/ServiceState.md)
 - [ServiceType](docs/ServiceType.md)
 - [User](docs/User.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in gewv_sides_client.apis and gewv_sides_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from gewv_sides_client.api.default_api import DefaultApi`
- `from gewv_sides_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import gewv_sides_client
from gewv_sides_client.apis import *
from gewv_sides_client.models import *
```

