# coding: utf-8

"""
Copyright 2017 Square, Inc.

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


from pprint import pformat
from six import iteritems
import re


class V1Page(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, page_index=None, cells=None):
        """
        V1Page - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'page_index': 'int',
            'cells': 'list[V1PageCell]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'page_index': 'page_index',
            'cells': 'cells'
        }

        self._id = id
        self._name = name
        self._page_index = page_index
        self._cells = cells

    @property
    def id(self):
        """
        Gets the id of this V1Page.
        The page's unique identifier.

        :return: The id of this V1Page.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1Page.
        The page's unique identifier.

        :param id: The id of this V1Page.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this V1Page.
        The page's name, if any.

        :return: The name of this V1Page.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Page.
        The page's name, if any.

        :param name: The name of this V1Page.
        :type: str
        """

        self._name = name

    @property
    def page_index(self):
        """
        Gets the page_index of this V1Page.
        The page's position in the merchant's list of pages. Always an integer between 0 and 6, inclusive.

        :return: The page_index of this V1Page.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this V1Page.
        The page's position in the merchant's list of pages. Always an integer between 0 and 6, inclusive.

        :param page_index: The page_index of this V1Page.
        :type: int
        """

        if page_index is None:
            raise ValueError("Invalid value for `page_index`, must not be `None`")
        if page_index > 6:
            raise ValueError("Invalid value for `page_index`, must be a value less than or equal to `6`")
        if page_index < 0:
            raise ValueError("Invalid value for `page_index`, must be a value greater than or equal to `0`")

        self._page_index = page_index

    @property
    def cells(self):
        """
        Gets the cells of this V1Page.
        The cells included on the page.

        :return: The cells of this V1Page.
        :rtype: list[V1PageCell]
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        """
        Sets the cells of this V1Page.
        The cells included on the page.

        :param cells: The cells of this V1Page.
        :type: list[V1PageCell]
        """

        self._cells = cells

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
