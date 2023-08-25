# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.14
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class BoxScorePlayersAverage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total': 'float',
        'quarter1': 'float',
        'quarter2': 'float',
        'quarter3': 'float',
        'quarter4': 'float',
        'rushing': 'float',
        'passing': 'float'
    }

    attribute_map = {
        'total': 'total',
        'quarter1': 'quarter1',
        'quarter2': 'quarter2',
        'quarter3': 'quarter3',
        'quarter4': 'quarter4',
        'rushing': 'rushing',
        'passing': 'passing'
    }

    def __init__(self, total=None, quarter1=None, quarter2=None, quarter3=None, quarter4=None, rushing=None, passing=None, _configuration=None):  # noqa: E501
        """BoxScorePlayersAverage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total = None
        self._quarter1 = None
        self._quarter2 = None
        self._quarter3 = None
        self._quarter4 = None
        self._rushing = None
        self._passing = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if quarter1 is not None:
            self.quarter1 = quarter1
        if quarter2 is not None:
            self.quarter2 = quarter2
        if quarter3 is not None:
            self.quarter3 = quarter3
        if quarter4 is not None:
            self.quarter4 = quarter4
        if rushing is not None:
            self.rushing = rushing
        if passing is not None:
            self.passing = passing

    @property
    def total(self):
        """Gets the total of this BoxScorePlayersAverage.  # noqa: E501


        :return: The total of this BoxScorePlayersAverage.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BoxScorePlayersAverage.


        :param total: The total of this BoxScorePlayersAverage.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def quarter1(self):
        """Gets the quarter1 of this BoxScorePlayersAverage.  # noqa: E501


        :return: The quarter1 of this BoxScorePlayersAverage.  # noqa: E501
        :rtype: float
        """
        return self._quarter1

    @quarter1.setter
    def quarter1(self, quarter1):
        """Sets the quarter1 of this BoxScorePlayersAverage.


        :param quarter1: The quarter1 of this BoxScorePlayersAverage.  # noqa: E501
        :type: float
        """

        self._quarter1 = quarter1

    @property
    def quarter2(self):
        """Gets the quarter2 of this BoxScorePlayersAverage.  # noqa: E501


        :return: The quarter2 of this BoxScorePlayersAverage.  # noqa: E501
        :rtype: float
        """
        return self._quarter2

    @quarter2.setter
    def quarter2(self, quarter2):
        """Sets the quarter2 of this BoxScorePlayersAverage.


        :param quarter2: The quarter2 of this BoxScorePlayersAverage.  # noqa: E501
        :type: float
        """

        self._quarter2 = quarter2

    @property
    def quarter3(self):
        """Gets the quarter3 of this BoxScorePlayersAverage.  # noqa: E501


        :return: The quarter3 of this BoxScorePlayersAverage.  # noqa: E501
        :rtype: float
        """
        return self._quarter3

    @quarter3.setter
    def quarter3(self, quarter3):
        """Sets the quarter3 of this BoxScorePlayersAverage.


        :param quarter3: The quarter3 of this BoxScorePlayersAverage.  # noqa: E501
        :type: float
        """

        self._quarter3 = quarter3

    @property
    def quarter4(self):
        """Gets the quarter4 of this BoxScorePlayersAverage.  # noqa: E501


        :return: The quarter4 of this BoxScorePlayersAverage.  # noqa: E501
        :rtype: float
        """
        return self._quarter4

    @quarter4.setter
    def quarter4(self, quarter4):
        """Sets the quarter4 of this BoxScorePlayersAverage.


        :param quarter4: The quarter4 of this BoxScorePlayersAverage.  # noqa: E501
        :type: float
        """

        self._quarter4 = quarter4

    @property
    def rushing(self):
        """Gets the rushing of this BoxScorePlayersAverage.  # noqa: E501


        :return: The rushing of this BoxScorePlayersAverage.  # noqa: E501
        :rtype: float
        """
        return self._rushing

    @rushing.setter
    def rushing(self, rushing):
        """Sets the rushing of this BoxScorePlayersAverage.


        :param rushing: The rushing of this BoxScorePlayersAverage.  # noqa: E501
        :type: float
        """

        self._rushing = rushing

    @property
    def passing(self):
        """Gets the passing of this BoxScorePlayersAverage.  # noqa: E501


        :return: The passing of this BoxScorePlayersAverage.  # noqa: E501
        :rtype: float
        """
        return self._passing

    @passing.setter
    def passing(self, passing):
        """Sets the passing of this BoxScorePlayersAverage.


        :param passing: The passing of this BoxScorePlayersAverage.  # noqa: E501
        :type: float
        """

        self._passing = passing

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(BoxScorePlayersAverage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BoxScorePlayersAverage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoxScorePlayersAverage):
            return True

        return self.to_dict() != other.to_dict()
