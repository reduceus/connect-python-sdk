# coding: utf-8

"""
Copyright 2016 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CustomerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_customer(self, authorization, body, **kwargs):
        """
        CreateCustomer
        Creates a new customer for a business, which can have associated cards on file.  You must provide __at least one__ of the following values in your request to this endpoint:  - `given_name` - `family_name` - `company_name` - `email_address` - `phone_number`  This endpoint does not accept an idempotency key. If you accidentally create a duplicate customer, you can delete it with the [DeleteCustomer](#endpoint-deletecustomer) endpoint.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_customer(authorization, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param CreateCustomerRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: CreateCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_customer" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `create_customer`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_customer`")


        resource_path = '/v2/customers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateCustomerResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))


    def delete_customer(self, authorization, customer_id, **kwargs):
        """
        DeleteCustomer
        Deletes a customer from a business, along with any linked cards on file.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_customer(authorization, customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str customer_id: The ID of the customer to delete. (required)
        :return: DeleteCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'customer_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_customer" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `delete_customer`")
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `delete_customer`")


        resource_path = '/v2/customers/{customer_id}'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeleteCustomerResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))


    def list_customers(self, authorization, **kwargs):
        """
        ListCustomers
        Lists a business's customers.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_customers(authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](#paginatingresults) for more information.
        :return: ListCustomersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_customers" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `list_customers`")


        resource_path = '/v2/customers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'cursor' in params and params['cursor'] is not None:
            query_params['cursor'] = params['cursor']

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ListCustomersResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))


    def retrieve_customer(self, authorization, customer_id, **kwargs):
        """
        RetrieveCustomer
        Returns details for a single customer.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retrieve_customer(authorization, customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str customer_id: The ID of the customer to retrieve. (required)
        :return: RetrieveCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'customer_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_customer" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `retrieve_customer`")
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `retrieve_customer`")


        resource_path = '/v2/customers/{customer_id}'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RetrieveCustomerResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))


    def update_customer(self, authorization, customer_id, body, **kwargs):
        """
        UpdateCustomer
        Updates the details of an existing customer.  You cannot edit a customer's cards on file with this endpoint. To make changes to a card on file, you must delete the existing card on file with the [DeleteCustomerCard](#endpoint-deletecustomercard) endpoint, then create a new one with the [CreateCustomerCard](#endpoint-createcustomercard) endpoint.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_customer(authorization, customer_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str customer_id: The ID of the customer to update. (required)
        :param UpdateCustomerRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: UpdateCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'customer_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_customer" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `update_customer`")
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `update_customer`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_customer`")


        resource_path = '/v2/customers/{customer_id}'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UpdateCustomerResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))

