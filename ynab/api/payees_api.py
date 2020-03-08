# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ynab.api_client import ApiClient
from ynab.exceptions import (
    ApiTypeError,
    ApiValueError
)


class PayeesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_payee_by_id(self, budget_id, payee_id, **kwargs):  # noqa: E501
        """Single payee  # noqa: E501

        Returns single payee  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_by_id(budget_id, payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str budget_id: The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) (required)
        :param str payee_id: The id of the payee (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PayeeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payee_by_id_with_http_info(budget_id, payee_id, **kwargs)  # noqa: E501

    def get_payee_by_id_with_http_info(self, budget_id, payee_id, **kwargs):  # noqa: E501
        """Single payee  # noqa: E501

        Returns single payee  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_by_id_with_http_info(budget_id, payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str budget_id: The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) (required)
        :param str payee_id: The id of the payee (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PayeeResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['budget_id', 'payee_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payee_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['budget_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `budget_id` when calling `get_payee_by_id`")  # noqa: E501
        # verify the required parameter 'payee_id' is set
        if self.api_client.client_side_validation and ('payee_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payee_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payee_id` when calling `get_payee_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in local_var_params:
            path_params['budget_id'] = local_var_params['budget_id']  # noqa: E501
        if 'payee_id' in local_var_params:
            path_params['payee_id'] = local_var_params['payee_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/payees/{payee_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayeeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payees(self, budget_id, **kwargs):  # noqa: E501
        """List payees  # noqa: E501

        Returns all payees  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payees(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str budget_id: The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) (required)
        :param int last_knowledge_of_server: The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PayeesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payees_with_http_info(budget_id, **kwargs)  # noqa: E501

    def get_payees_with_http_info(self, budget_id, **kwargs):  # noqa: E501
        """List payees  # noqa: E501

        Returns all payees  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payees_with_http_info(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str budget_id: The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) (required)
        :param int last_knowledge_of_server: The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PayeesResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['budget_id', 'last_knowledge_of_server']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payees" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['budget_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `budget_id` when calling `get_payees`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in local_var_params:
            path_params['budget_id'] = local_var_params['budget_id']  # noqa: E501

        query_params = []
        if 'last_knowledge_of_server' in local_var_params and local_var_params['last_knowledge_of_server'] is not None:  # noqa: E501
            query_params.append(('last_knowledge_of_server', local_var_params['last_knowledge_of_server']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/payees', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayeesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
