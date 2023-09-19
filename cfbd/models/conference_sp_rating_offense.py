# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.5.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class ConferenceSPRatingOffense(object):
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
        'passing': 'float',
        'standard_downs': 'float',
        'passing_downs': 'float',
        'run_rate': 'float',
        'pace': 'float'
    }

    attribute_map = {
        'rating': 'rating',
        'success': 'success',
        'explosiveness': 'explosiveness',
        'rushing': 'rushing',
        'passing': 'passing',
        'standard_downs': 'standardDowns',
        'passing_downs': 'passingDowns',
        'run_rate': 'runRate',
        'pace': 'pace'
    }

    def __init__(self, rating=None, success=None, explosiveness=None, rushing=None, passing=None, standard_downs=None, passing_downs=None, run_rate=None, pace=None, _configuration=None):  # noqa: E501
        """ConferenceSPRatingOffense - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rating = None
        self._success = None
        self._explosiveness = None
        self._rushing = None
        self._passing = None
        self._standard_downs = None
        self._passing_downs = None
        self._run_rate = None
        self._pace = None
        self.discriminator = None

        if rating is not None:
            self.rating = rating
        if success is not None:
            self.success = success
        if explosiveness is not None:
            self.explosiveness = explosiveness
        if rushing is not None:
            self.rushing = rushing
        if passing is not None:
            self.passing = passing
        if standard_downs is not None:
            self.standard_downs = standard_downs
        if passing_downs is not None:
            self.passing_downs = passing_downs
        if run_rate is not None:
            self.run_rate = run_rate
        if pace is not None:
            self.pace = pace

    @property
    def rating(self):
        """Gets the rating of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The rating of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this ConferenceSPRatingOffense.


        :param rating: The rating of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._rating = rating

    @property
    def success(self):
        """Gets the success of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The success of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ConferenceSPRatingOffense.


        :param success: The success of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._success = success

    @property
    def explosiveness(self):
        """Gets the explosiveness of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The explosiveness of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._explosiveness

    @explosiveness.setter
    def explosiveness(self, explosiveness):
        """Sets the explosiveness of this ConferenceSPRatingOffense.


        :param explosiveness: The explosiveness of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._explosiveness = explosiveness

    @property
    def rushing(self):
        """Gets the rushing of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The rushing of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._rushing

    @rushing.setter
    def rushing(self, rushing):
        """Sets the rushing of this ConferenceSPRatingOffense.


        :param rushing: The rushing of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._rushing = rushing

    @property
    def passing(self):
        """Gets the passing of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The passing of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._passing

    @passing.setter
    def passing(self, passing):
        """Sets the passing of this ConferenceSPRatingOffense.


        :param passing: The passing of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._passing = passing

    @property
    def standard_downs(self):
        """Gets the standard_downs of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The standard_downs of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._standard_downs

    @standard_downs.setter
    def standard_downs(self, standard_downs):
        """Sets the standard_downs of this ConferenceSPRatingOffense.


        :param standard_downs: The standard_downs of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._standard_downs = standard_downs

    @property
    def passing_downs(self):
        """Gets the passing_downs of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The passing_downs of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._passing_downs

    @passing_downs.setter
    def passing_downs(self, passing_downs):
        """Sets the passing_downs of this ConferenceSPRatingOffense.


        :param passing_downs: The passing_downs of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._passing_downs = passing_downs

    @property
    def run_rate(self):
        """Gets the run_rate of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The run_rate of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._run_rate

    @run_rate.setter
    def run_rate(self, run_rate):
        """Sets the run_rate of this ConferenceSPRatingOffense.


        :param run_rate: The run_rate of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._run_rate = run_rate

    @property
    def pace(self):
        """Gets the pace of this ConferenceSPRatingOffense.  # noqa: E501


        :return: The pace of this ConferenceSPRatingOffense.  # noqa: E501
        :rtype: float
        """
        return self._pace

    @pace.setter
    def pace(self, pace):
        """Sets the pace of this ConferenceSPRatingOffense.


        :param pace: The pace of this ConferenceSPRatingOffense.  # noqa: E501
        :type: float
        """

        self._pace = pace

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
        if issubclass(ConferenceSPRatingOffense, dict):
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
        if not isinstance(other, ConferenceSPRatingOffense):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConferenceSPRatingOffense):
            return True

        return self.to_dict() != other.to_dict()
