# openapi_client.ContactsApi

All URIs are relative to *https://tek-ekg.iet.mw.tu-dresden.de/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /fieldtests/{fieldtestId}/contacts | 
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /fieldtests/{fieldtestId}/contacts/{contactId} | 
[**get_contacts**](ContactsApi.md#get_contacts) | **GET** /fieldtests/{fieldtestId}/contacts | 
[**update_contact**](ContactsApi.md#update_contact) | **PATCH** /fieldtests/{fieldtestId}/contacts/{contactId} | 


# **create_contact**
> Contact create_contact(fieldtest_id, contact)



Create a new contact for a fieldtest.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import contacts_api
from openapi_client.model.id import ID
from openapi_client.model.contact import Contact
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
    api_instance = contacts_api.ContactsApi(api_client)
    fieldtest_id = ID(1) # ID | 
    contact = Contact(
        name="name_example",
        email="email_example",
        phone="phone_example",
    ) # Contact | The new contact, that will be created!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_contact(fieldtest_id, contact)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest_id** | **ID**|  |
 **contact** | [**Contact**](Contact.md)| The new contact, that will be created! |

### Return type

[**Contact**](Contact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get your user object |  -  |
**400** | Invalid new contact object. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(fieldtest_id, contact_id)



Delete a contact.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import contacts_api
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
    api_instance = contacts_api.ContactsApi(api_client)
    fieldtest_id = ID(1) # ID | 
    contact_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_contact(fieldtest_id, contact_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ContactsApi->delete_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest_id** | **ID**|  |
 **contact_id** | **ID**|  |

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
**200** | The contact deleted |  -  |
**502** | Invalid contact or fieldtest id. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> ArrayOfContacts get_contacts(fieldtest_id)



Get all contacts of a fieldtest.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import contacts_api
from openapi_client.model.array_of_contacts import ArrayOfContacts
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
    api_instance = contacts_api.ContactsApi(api_client)
    fieldtest_id = ID(1) # ID | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_contacts(fieldtest_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContactsApi->get_contacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest_id** | **ID**|  |

### Return type

[**ArrayOfContacts**](ArrayOfContacts.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of contacts of a fieldtest |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> Contact update_contact(fieldtest_id, contact_id, contact)



Update a existing contact.

### Example

* Basic Authentication (basicAuth):
```python
import time
import openapi_client
from openapi_client.api import contacts_api
from openapi_client.model.id import ID
from openapi_client.model.contact import Contact
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
    api_instance = contacts_api.ContactsApi(api_client)
    fieldtest_id = ID(1) # ID | 
    contact_id = ID(1) # ID | 
    contact = Contact(
        name="name_example",
        email="email_example",
        phone="phone_example",
    ) # Contact | The contact to update!

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_contact(fieldtest_id, contact_id, contact)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldtest_id** | **ID**|  |
 **contact_id** | **ID**|  |
 **contact** | [**Contact**](Contact.md)| The contact to update! |

### Return type

[**Contact**](Contact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated contact |  -  |
**400** | Invalid contact to update. |  -  |
**0** | Unexpecated Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

