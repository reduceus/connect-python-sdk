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


class V1Discount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, rate=None, amount_money=None, discount_type=None, pin_required=None, color=None, v2_id=None):
        """
        V1Discount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'rate': 'str',
            'amount_money': 'V1Money',
            'discount_type': 'str',
            'pin_required': 'bool',
            'color': 'str',
            'v2_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'rate': 'rate',
            'amount_money': 'amount_money',
            'discount_type': 'discount_type',
            'pin_required': 'pin_required',
            'color': 'color',
            'v2_id': 'v2_id'
        }

        self._id = id
        self._name = name
        self._rate = rate
        self._amount_money = amount_money
        self._discount_type = discount_type
        self._pin_required = pin_required
        self._color = color
        self._v2_id = v2_id

    @property
    def id(self):
        """
        Gets the id of this V1Discount.
        The discount's unique ID.

        :return: The id of this V1Discount.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1Discount.
        The discount's unique ID.

        :param id: The id of this V1Discount.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this V1Discount.
        The discount's name.

        :return: The name of this V1Discount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Discount.
        The discount's name.

        :param name: The name of this V1Discount.
        :type: str
        """

        self._name = name

    @property
    def rate(self):
        """
        Gets the rate of this V1Discount.
        The rate of the discount, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%. This rate is 0 if discount_type is VARIABLE_PERCENTAGE.

        :return: The rate of this V1Discount.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this V1Discount.
        The rate of the discount, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%. This rate is 0 if discount_type is VARIABLE_PERCENTAGE.

        :param rate: The rate of this V1Discount.
        :type: str
        """

        self._rate = rate

    @property
    def amount_money(self):
        """
        Gets the amount_money of this V1Discount.
        The amount of the discount. This amount is 0 if discount_type is VARIABLE_AMOUNT. This field is not included for rate-based discounts.

        :return: The amount_money of this V1Discount.
        :rtype: V1Money
        """
        return self._amount_money

    @amount_money.setter
    def amount_money(self, amount_money):
        """
        Sets the amount_money of this V1Discount.
        The amount of the discount. This amount is 0 if discount_type is VARIABLE_AMOUNT. This field is not included for rate-based discounts.

        :param amount_money: The amount_money of this V1Discount.
        :type: V1Money
        """

        self._amount_money = amount_money

    @property
    def discount_type(self):
        """
        Gets the discount_type of this V1Discount.
        Indicates whether the discount is a FIXED value or entered at the time of sale. See [V1DiscountDiscountType](#type-v1discountdiscounttype) for possible values

        :return: The discount_type of this V1Discount.
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """
        Sets the discount_type of this V1Discount.
        Indicates whether the discount is a FIXED value or entered at the time of sale. See [V1DiscountDiscountType](#type-v1discountdiscounttype) for possible values

        :param discount_type: The discount_type of this V1Discount.
        :type: str
        """

        self._discount_type = discount_type

    @property
    def pin_required(self):
        """
        Gets the pin_required of this V1Discount.
        Indicates whether a mobile staff member needs to enter their PIN to apply the discount to a payment.

        :return: The pin_required of this V1Discount.
        :rtype: bool
        """
        return self._pin_required

    @pin_required.setter
    def pin_required(self, pin_required):
        """
        Sets the pin_required of this V1Discount.
        Indicates whether a mobile staff member needs to enter their PIN to apply the discount to a payment.

        :param pin_required: The pin_required of this V1Discount.
        :type: bool
        """

        self._pin_required = pin_required

    @property
    def color(self):
        """
        Gets the color of this V1Discount.
        The color of the discount's display label in Square Register, if not the default color. The default color is 9da2a6. See [V1DiscountColor](#type-v1discountcolor) for possible values

        :return: The color of this V1Discount.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this V1Discount.
        The color of the discount's display label in Square Register, if not the default color. The default color is 9da2a6. See [V1DiscountColor](#type-v1discountcolor) for possible values

        :param color: The color of this V1Discount.
        :type: str
        """

        self._color = color

    @property
    def v2_id(self):
        """
        Gets the v2_id of this V1Discount.
        The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID.

        :return: The v2_id of this V1Discount.
        :rtype: str
        """
        return self._v2_id

    @v2_id.setter
    def v2_id(self, v2_id):
        """
        Sets the v2_id of this V1Discount.
        The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID.

        :param v2_id: The v2_id of this V1Discount.
        :type: str
        """

        self._v2_id = v2_id

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
