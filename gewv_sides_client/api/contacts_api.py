"""
    The api of the tek ekg boxes and field controller.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gewv_sides_client.api_client import ApiClient, Endpoint as _Endpoint
from gewv_sides_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gewv_sides_client.model.array_of_contacts import ArrayOfContacts
from gewv_sides_client.model.contact import Contact
from gewv_sides_client.model.id import ID


class ContactsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_contact(
            self,
            fieldtest_id,
            contact,
            **kwargs
        ):
            """create_contact  # noqa: E501

            Create a new contact for a fieldtest.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_contact(fieldtest_id, contact, async_req=True)
            >>> result = thread.get()

            Args:
                fieldtest_id (ID):
                contact (Contact): The new contact, that will be created!

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Contact
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['fieldtest_id'] = \
                fieldtest_id
            kwargs['contact'] = \
                contact
            return self.call_with_http_info(**kwargs)

        self.create_contact = _Endpoint(
            settings={
                'response_type': (Contact,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/fieldtests/{fieldtestId}/contacts',
                'operation_id': 'create_contact',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'fieldtest_id',
                    'contact',
                ],
                'required': [
                    'fieldtest_id',
                    'contact',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'fieldtest_id':
                        (ID,),
                    'contact':
                        (Contact,),
                },
                'attribute_map': {
                    'fieldtest_id': 'fieldtestId',
                },
                'location_map': {
                    'fieldtest_id': 'path',
                    'contact': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_contact
        )

        def __delete_contact(
            self,
            fieldtest_id,
            contact_id,
            **kwargs
        ):
            """delete_contact  # noqa: E501

            Delete a contact.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_contact(fieldtest_id, contact_id, async_req=True)
            >>> result = thread.get()

            Args:
                fieldtest_id (ID):
                contact_id (ID):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['fieldtest_id'] = \
                fieldtest_id
            kwargs['contact_id'] = \
                contact_id
            return self.call_with_http_info(**kwargs)

        self.delete_contact = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/fieldtests/{fieldtestId}/contacts/{contactId}',
                'operation_id': 'delete_contact',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'fieldtest_id',
                    'contact_id',
                ],
                'required': [
                    'fieldtest_id',
                    'contact_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'fieldtest_id':
                        (ID,),
                    'contact_id':
                        (ID,),
                },
                'attribute_map': {
                    'fieldtest_id': 'fieldtestId',
                    'contact_id': 'contactId',
                },
                'location_map': {
                    'fieldtest_id': 'path',
                    'contact_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_contact
        )

        def __get_contacts(
            self,
            fieldtest_id,
            **kwargs
        ):
            """get_contacts  # noqa: E501

            Get all contacts of a fieldtest.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_contacts(fieldtest_id, async_req=True)
            >>> result = thread.get()

            Args:
                fieldtest_id (ID):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ArrayOfContacts
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['fieldtest_id'] = \
                fieldtest_id
            return self.call_with_http_info(**kwargs)

        self.get_contacts = _Endpoint(
            settings={
                'response_type': (ArrayOfContacts,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/fieldtests/{fieldtestId}/contacts',
                'operation_id': 'get_contacts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'fieldtest_id',
                ],
                'required': [
                    'fieldtest_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'fieldtest_id':
                        (ID,),
                },
                'attribute_map': {
                    'fieldtest_id': 'fieldtestId',
                },
                'location_map': {
                    'fieldtest_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_contacts
        )

        def __update_contact(
            self,
            fieldtest_id,
            contact_id,
            contact,
            **kwargs
        ):
            """update_contact  # noqa: E501

            Update a existing contact.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_contact(fieldtest_id, contact_id, contact, async_req=True)
            >>> result = thread.get()

            Args:
                fieldtest_id (ID):
                contact_id (ID):
                contact (Contact): The contact to update!

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Contact
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['fieldtest_id'] = \
                fieldtest_id
            kwargs['contact_id'] = \
                contact_id
            kwargs['contact'] = \
                contact
            return self.call_with_http_info(**kwargs)

        self.update_contact = _Endpoint(
            settings={
                'response_type': (Contact,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/fieldtests/{fieldtestId}/contacts/{contactId}',
                'operation_id': 'update_contact',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'fieldtest_id',
                    'contact_id',
                    'contact',
                ],
                'required': [
                    'fieldtest_id',
                    'contact_id',
                    'contact',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'fieldtest_id':
                        (ID,),
                    'contact_id':
                        (ID,),
                    'contact':
                        (Contact,),
                },
                'attribute_map': {
                    'fieldtest_id': 'fieldtestId',
                    'contact_id': 'contactId',
                },
                'location_map': {
                    'fieldtest_id': 'path',
                    'contact_id': 'path',
                    'contact': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_contact
        )
