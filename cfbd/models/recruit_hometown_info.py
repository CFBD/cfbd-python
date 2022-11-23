# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.12
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class RecruitHometownInfo(object):
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
        'latitude': 'float',
        'longitude': 'float',
        'county_fips': 'str'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude',
        'county_fips': 'countyFips'
    }

    def __init__(self, latitude=None, longitude=None, county_fips=None, _configuration=None):  # noqa: E501
        """RecruitHometownInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._latitude = None
        self._longitude = None
        self._county_fips = None
        self.discriminator = None

        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if county_fips is not None:
            self.county_fips = county_fips

    @property
    def latitude(self):
        """Gets the latitude of this RecruitHometownInfo.  # noqa: E501


        :return: The latitude of this RecruitHometownInfo.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this RecruitHometownInfo.


        :param latitude: The latitude of this RecruitHometownInfo.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this RecruitHometownInfo.  # noqa: E501


        :return: The longitude of this RecruitHometownInfo.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this RecruitHometownInfo.


        :param longitude: The longitude of this RecruitHometownInfo.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def county_fips(self):
        """Gets the county_fips of this RecruitHometownInfo.  # noqa: E501


        :return: The county_fips of this RecruitHometownInfo.  # noqa: E501
        :rtype: str
        """
        return self._county_fips

    @county_fips.setter
    def county_fips(self, county_fips):
        """Sets the county_fips of this RecruitHometownInfo.


        :param county_fips: The county_fips of this RecruitHometownInfo.  # noqa: E501
        :type: str
        """

        self._county_fips = county_fips

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
        if issubclass(RecruitHometownInfo, dict):
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
        if not isinstance(other, RecruitHometownInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecruitHometownInfo):
            return True

        return self.to_dict() != other.to_dict()
