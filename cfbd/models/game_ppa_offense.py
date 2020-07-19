# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.4
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GamePPAOffense(object):
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
        'overall': 'float',
        'passing': 'float',
        'rushing': 'float',
        'first_down': 'float',
        'second_down': 'float',
        'third_down': 'float'
    }

    attribute_map = {
        'overall': 'overall',
        'passing': 'passing',
        'rushing': 'rushing',
        'first_down': 'firstDown',
        'second_down': 'secondDown',
        'third_down': 'thirdDown'
    }

    def __init__(self, overall=None, passing=None, rushing=None, first_down=None, second_down=None, third_down=None):  # noqa: E501
        """GamePPAOffense - a model defined in Swagger"""  # noqa: E501

        self._overall = None
        self._passing = None
        self._rushing = None
        self._first_down = None
        self._second_down = None
        self._third_down = None
        self.discriminator = None

        if overall is not None:
            self.overall = overall
        if passing is not None:
            self.passing = passing
        if rushing is not None:
            self.rushing = rushing
        if first_down is not None:
            self.first_down = first_down
        if second_down is not None:
            self.second_down = second_down
        if third_down is not None:
            self.third_down = third_down

    @property
    def overall(self):
        """Gets the overall of this GamePPAOffense.  # noqa: E501


        :return: The overall of this GamePPAOffense.  # noqa: E501
        :rtype: float
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this GamePPAOffense.


        :param overall: The overall of this GamePPAOffense.  # noqa: E501
        :type: float
        """

        self._overall = overall

    @property
    def passing(self):
        """Gets the passing of this GamePPAOffense.  # noqa: E501


        :return: The passing of this GamePPAOffense.  # noqa: E501
        :rtype: float
        """
        return self._passing

    @passing.setter
    def passing(self, passing):
        """Sets the passing of this GamePPAOffense.


        :param passing: The passing of this GamePPAOffense.  # noqa: E501
        :type: float
        """

        self._passing = passing

    @property
    def rushing(self):
        """Gets the rushing of this GamePPAOffense.  # noqa: E501


        :return: The rushing of this GamePPAOffense.  # noqa: E501
        :rtype: float
        """
        return self._rushing

    @rushing.setter
    def rushing(self, rushing):
        """Sets the rushing of this GamePPAOffense.


        :param rushing: The rushing of this GamePPAOffense.  # noqa: E501
        :type: float
        """

        self._rushing = rushing

    @property
    def first_down(self):
        """Gets the first_down of this GamePPAOffense.  # noqa: E501


        :return: The first_down of this GamePPAOffense.  # noqa: E501
        :rtype: float
        """
        return self._first_down

    @first_down.setter
    def first_down(self, first_down):
        """Sets the first_down of this GamePPAOffense.


        :param first_down: The first_down of this GamePPAOffense.  # noqa: E501
        :type: float
        """

        self._first_down = first_down

    @property
    def second_down(self):
        """Gets the second_down of this GamePPAOffense.  # noqa: E501


        :return: The second_down of this GamePPAOffense.  # noqa: E501
        :rtype: float
        """
        return self._second_down

    @second_down.setter
    def second_down(self, second_down):
        """Sets the second_down of this GamePPAOffense.


        :param second_down: The second_down of this GamePPAOffense.  # noqa: E501
        :type: float
        """

        self._second_down = second_down

    @property
    def third_down(self):
        """Gets the third_down of this GamePPAOffense.  # noqa: E501


        :return: The third_down of this GamePPAOffense.  # noqa: E501
        :rtype: float
        """
        return self._third_down

    @third_down.setter
    def third_down(self, third_down):
        """Sets the third_down of this GamePPAOffense.


        :param third_down: The third_down of this GamePPAOffense.  # noqa: E501
        :type: float
        """

        self._third_down = third_down

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
        if issubclass(GamePPAOffense, dict):
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
        if not isinstance(other, GamePPAOffense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
