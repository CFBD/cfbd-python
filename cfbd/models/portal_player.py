# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.3.2
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class PortalPlayer(object):
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
        'season': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'position': 'str',
        'origin': 'str',
        'destination': 'str',
        'transfer_date': 'str',
        'rating': 'float',
        'stars': 'int',
        'eligibility': 'str'
    }

    attribute_map = {
        'season': 'season',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'position': 'position',
        'origin': 'origin',
        'destination': 'destination',
        'transfer_date': 'transferDate',
        'rating': 'rating',
        'stars': 'stars',
        'eligibility': 'eligibility'
    }

    def __init__(self, season=None, first_name=None, last_name=None, position=None, origin=None, destination=None, transfer_date=None, rating=None, stars=None, eligibility=None, _configuration=None):  # noqa: E501
        """PortalPlayer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._season = None
        self._first_name = None
        self._last_name = None
        self._position = None
        self._origin = None
        self._destination = None
        self._transfer_date = None
        self._rating = None
        self._stars = None
        self._eligibility = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if position is not None:
            self.position = position
        if origin is not None:
            self.origin = origin
        if destination is not None:
            self.destination = destination
        if transfer_date is not None:
            self.transfer_date = transfer_date
        if rating is not None:
            self.rating = rating
        if stars is not None:
            self.stars = stars
        if eligibility is not None:
            self.eligibility = eligibility

    @property
    def season(self):
        """Gets the season of this PortalPlayer.  # noqa: E501


        :return: The season of this PortalPlayer.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PortalPlayer.


        :param season: The season of this PortalPlayer.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def first_name(self):
        """Gets the first_name of this PortalPlayer.  # noqa: E501


        :return: The first_name of this PortalPlayer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PortalPlayer.


        :param first_name: The first_name of this PortalPlayer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PortalPlayer.  # noqa: E501


        :return: The last_name of this PortalPlayer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PortalPlayer.


        :param last_name: The last_name of this PortalPlayer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def position(self):
        """Gets the position of this PortalPlayer.  # noqa: E501


        :return: The position of this PortalPlayer.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PortalPlayer.


        :param position: The position of this PortalPlayer.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def origin(self):
        """Gets the origin of this PortalPlayer.  # noqa: E501


        :return: The origin of this PortalPlayer.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this PortalPlayer.


        :param origin: The origin of this PortalPlayer.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def destination(self):
        """Gets the destination of this PortalPlayer.  # noqa: E501


        :return: The destination of this PortalPlayer.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this PortalPlayer.


        :param destination: The destination of this PortalPlayer.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def transfer_date(self):
        """Gets the transfer_date of this PortalPlayer.  # noqa: E501


        :return: The transfer_date of this PortalPlayer.  # noqa: E501
        :rtype: str
        """
        return self._transfer_date

    @transfer_date.setter
    def transfer_date(self, transfer_date):
        """Sets the transfer_date of this PortalPlayer.


        :param transfer_date: The transfer_date of this PortalPlayer.  # noqa: E501
        :type: str
        """

        self._transfer_date = transfer_date

    @property
    def rating(self):
        """Gets the rating of this PortalPlayer.  # noqa: E501


        :return: The rating of this PortalPlayer.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this PortalPlayer.


        :param rating: The rating of this PortalPlayer.  # noqa: E501
        :type: float
        """

        self._rating = rating

    @property
    def stars(self):
        """Gets the stars of this PortalPlayer.  # noqa: E501


        :return: The stars of this PortalPlayer.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this PortalPlayer.


        :param stars: The stars of this PortalPlayer.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def eligibility(self):
        """Gets the eligibility of this PortalPlayer.  # noqa: E501


        :return: The eligibility of this PortalPlayer.  # noqa: E501
        :rtype: str
        """
        return self._eligibility

    @eligibility.setter
    def eligibility(self, eligibility):
        """Sets the eligibility of this PortalPlayer.


        :param eligibility: The eligibility of this PortalPlayer.  # noqa: E501
        :type: str
        """

        self._eligibility = eligibility

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
        if issubclass(PortalPlayer, dict):
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
        if not isinstance(other, PortalPlayer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortalPlayer):
            return True

        return self.to_dict() != other.to_dict()
