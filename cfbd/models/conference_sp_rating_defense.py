# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.13
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class ConferenceSPRatingDefense(object):
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
        'rating': 'float',
        'success': 'float',
        'explosiveness': 'float',
        'rushing': 'float',
        'pasing': 'float',
        'standard_downs': 'float',
        'passing_downs': 'float',
        'havoc': 'TeamSPRatingDefenseHavoc'
    }

    attribute_map = {
        'rating': 'rating',
        'success': 'success',
        'explosiveness': 'explosiveness',
        'rushing': 'rushing',
        'pasing': 'pasing',
        'standard_downs': 'standardDowns',
        'passing_downs': 'passingDowns',
        'havoc': 'havoc'
    }

    def __init__(self, rating=None, success=None, explosiveness=None, rushing=None, pasing=None, standard_downs=None, passing_downs=None, havoc=None, _configuration=None):  # noqa: E501
        """ConferenceSPRatingDefense - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rating = None
        self._success = None
        self._explosiveness = None
        self._rushing = None
        self._pasing = None
        self._standard_downs = None
        self._passing_downs = None
        self._havoc = None
        self.discriminator = None

        if rating is not None:
            self.rating = rating
        if success is not None:
            self.success = success
        if explosiveness is not None:
            self.explosiveness = explosiveness
        if rushing is not None:
            self.rushing = rushing
        if pasing is not None:
            self.pasing = pasing
        if standard_downs is not None:
            self.standard_downs = standard_downs
        if passing_downs is not None:
            self.passing_downs = passing_downs
        if havoc is not None:
            self.havoc = havoc

    @property
    def rating(self):
        """Gets the rating of this ConferenceSPRatingDefense.  # noqa: E501


        :return: The rating of this ConferenceSPRatingDefense.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this ConferenceSPRatingDefense.


        :param rating: The rating of this ConferenceSPRatingDefense.  # noqa: E501
        :type: float
        """

        self._rating = rating

    @property
    def success(self):
        """Gets the success of this ConferenceSPRatingDefense.  # noqa: E501


        :return: The success of this ConferenceSPRatingDefense.  # noqa: E501
        :rtype: float
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ConferenceSPRatingDefense.


        :param success: The success of this ConferenceSPRatingDefense.  # noqa: E501
        :type: float
        """

        self._success = success

    @property
    def explosiveness(self):
        """Gets the explosiveness of this ConferenceSPRatingDefense.  # noqa: E501


        :return: The explosiveness of this ConferenceSPRatingDefense.  # noqa: E501
        :rtype: float
        """
        return self._explosiveness

    @explosiveness.setter
    def explosiveness(self, explosiveness):
        """Sets the explosiveness of this ConferenceSPRatingDefense.


        :param explosiveness: The explosiveness of this ConferenceSPRatingDefense.  # noqa: E501
        :type: float
        """

        self._explosiveness = explosiveness

    @property
    def rushing(self):
        """Gets the rushing of this ConferenceSPRatingDefense.  # noqa: E501


        :return: The rushing of this ConferenceSPRatingDefense.  # noqa: E501
        :rtype: float
        """
        return self._rushing

    @rushing.setter
    def rushing(self, rushing):
        """Sets the rushing of this ConferenceSPRatingDefense.


        :param rushing: The rushing of this ConferenceSPRatingDefense.  # noqa: E501
        :type: float
        """

        self._rushing = rushing

    @property
    def pasing(self):
        """Gets the pasing of this ConferenceSPRatingDefense.  # noqa: E501


        :return: The pasing of this ConferenceSPRatingDefense.  # noqa: E501
        :rtype: float
        """
        return self._pasing

    @pasing.setter
    def pasing(self, pasing):
        """Sets the pasing of this ConferenceSPRatingDefense.


        :param pasing: The pasing of this ConferenceSPRatingDefense.  # noqa: E501
        :type: float
        """

        self._pasing = pasing

    @property
    def standard_downs(self):
        """Gets the standard_downs of this ConferenceSPRatingDefense.  # noqa: E501


        :return: The standard_downs of this ConferenceSPRatingDefense.  # noqa: E501
        :rtype: float
        """
        return self._standard_downs

    @standard_downs.setter
    def standard_downs(self, standard_downs):
        """Sets the standard_downs of this ConferenceSPRatingDefense.


        :param standard_downs: The standard_downs of this ConferenceSPRatingDefense.  # noqa: E501
        :type: float
        """

        self._standard_downs = standard_downs

    @property
    def passing_downs(self):
        """Gets the passing_downs of this ConferenceSPRatingDefense.  # noqa: E501


        :return: The passing_downs of this ConferenceSPRatingDefense.  # noqa: E501
        :rtype: float
        """
        return self._passing_downs

    @passing_downs.setter
    def passing_downs(self, passing_downs):
        """Sets the passing_downs of this ConferenceSPRatingDefense.


        :param passing_downs: The passing_downs of this ConferenceSPRatingDefense.  # noqa: E501
        :type: float
        """

        self._passing_downs = passing_downs

    @property
    def havoc(self):
        """Gets the havoc of this ConferenceSPRatingDefense.  # noqa: E501


        :return: The havoc of this ConferenceSPRatingDefense.  # noqa: E501
        :rtype: TeamSPRatingDefenseHavoc
        """
        return self._havoc

    @havoc.setter
    def havoc(self, havoc):
        """Sets the havoc of this ConferenceSPRatingDefense.


        :param havoc: The havoc of this ConferenceSPRatingDefense.  # noqa: E501
        :type: TeamSPRatingDefenseHavoc
        """

        self._havoc = havoc

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
        if issubclass(ConferenceSPRatingDefense, dict):
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
        if not isinstance(other, ConferenceSPRatingDefense):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConferenceSPRatingDefense):
            return True

        return self.to_dict() != other.to_dict()
