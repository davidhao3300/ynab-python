# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ynab.configuration import Configuration


class SaveSubTransaction(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'amount': 'int',
        'payee_id': 'str',
        'payee_name': 'str',
        'category_id': 'str',
        'memo': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'payee_id': 'payee_id',
        'payee_name': 'payee_name',
        'category_id': 'category_id',
        'memo': 'memo'
    }

    def __init__(self, amount=None, payee_id=None, payee_name=None, category_id=None, memo=None, local_vars_configuration=None):  # noqa: E501
        """SaveSubTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._payee_id = None
        self._payee_name = None
        self._category_id = None
        self._memo = None
        self.discriminator = None

        self.amount = amount
        if payee_id is not None:
            self.payee_id = payee_id
        if payee_name is not None:
            self.payee_name = payee_name
        if category_id is not None:
            self.category_id = category_id
        if memo is not None:
            self.memo = memo

    @property
    def amount(self):
        """Gets the amount of this SaveSubTransaction.  # noqa: E501

        The sub-transaction amount in milliunits format.  # noqa: E501

        :return: The amount of this SaveSubTransaction.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SaveSubTransaction.

        The sub-transaction amount in milliunits format.  # noqa: E501

        :param amount: The amount of this SaveSubTransaction.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def payee_id(self):
        """Gets the payee_id of this SaveSubTransaction.  # noqa: E501

        The payee for the sub-transaction.  Transfer payees are not allowed.  # noqa: E501

        :return: The payee_id of this SaveSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this SaveSubTransaction.

        The payee for the sub-transaction.  Transfer payees are not allowed.  # noqa: E501

        :param payee_id: The payee_id of this SaveSubTransaction.  # noqa: E501
        :type: str
        """

        self._payee_id = payee_id

    @property
    def payee_name(self):
        """Gets the payee_name of this SaveSubTransaction.  # noqa: E501

        The payee name.  If a payee_name value is provided and payee_id has a null value, the payee_name value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified on parent transaction) or (2) a payee with the same name or (3) creation of a new payee.  # noqa: E501

        :return: The payee_name of this SaveSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this SaveSubTransaction.

        The payee name.  If a payee_name value is provided and payee_id has a null value, the payee_name value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified on parent transaction) or (2) a payee with the same name or (3) creation of a new payee.  # noqa: E501

        :param payee_name: The payee_name of this SaveSubTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                payee_name is not None and len(payee_name) > 50):
            raise ValueError("Invalid value for `payee_name`, length must be less than or equal to `50`")  # noqa: E501

        self._payee_name = payee_name

    @property
    def category_id(self):
        """Gets the category_id of this SaveSubTransaction.  # noqa: E501

        The category for the sub-transaction.  Credit Card Payment categories are not permitted and will be ignored if supplied.  # noqa: E501

        :return: The category_id of this SaveSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this SaveSubTransaction.

        The category for the sub-transaction.  Credit Card Payment categories are not permitted and will be ignored if supplied.  # noqa: E501

        :param category_id: The category_id of this SaveSubTransaction.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def memo(self):
        """Gets the memo of this SaveSubTransaction.  # noqa: E501


        :return: The memo of this SaveSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this SaveSubTransaction.


        :param memo: The memo of this SaveSubTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                memo is not None and len(memo) > 200):
            raise ValueError("Invalid value for `memo`, length must be less than or equal to `200`")  # noqa: E501

        self._memo = memo

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SaveSubTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SaveSubTransaction):
            return True

        return self.to_dict() != other.to_dict()
