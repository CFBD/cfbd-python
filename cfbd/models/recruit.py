# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.2.3
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class Recruit(object):
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
        'id': 'int',
        'athlete_id': 'int',
        'recruit_type': 'str',
        'year': 'int',
        'ranking': 'int',
        'name': 'str',
        'school': 'str',
        'committed_to': 'str',
        'position': 'str',
        'height': 'float',
        'weight': 'int',
        'stars': 'int',
        'rating': 'float',
        'city': 'str',
        'state_province': 'str',
        'country': 'str',
        'hometown_info': 'object'
    }

    attribute_map = {
        'id': 'id',
        'athlete_id': 'athleteId',
        'recruit_type': 'recruitType',
        'year': 'year',
        'ranking': 'ranking',
        'name': 'name',
        'school': 'school',
        'committed_to': 'committedTo',
        'position': 'position',
        'height': 'height',
        'weight': 'weight',
        'stars': 'stars',
        'rating': 'rating',
        'city': 'city',
        'state_province': 'stateProvince',
        'country': 'country',
        'hometown_info': 'hometownInfo'
    }

    def __init__(self, id=None, athlete_id=None, recruit_type=None, year=None, ranking=None, name=None, school=None, committed_to=None, position=None, height=None, weight=None, stars=None, rating=None, city=None, state_province=None, country=None, hometown_info=None, _configuration=None):  # noqa: E501
        """Recruit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._athlete_id = None
        self._recruit_type = None
        self._year = None
        self._ranking = None
        self._name = None
        self._school = None
        self._committed_to = None
        self._position = None
        self._height = None
        self._weight = None
        self._stars = None
        self._rating = None
        self._city = None
        self._state_province = None
        self._country = None
        self._hometown_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if athlete_id is not None:
            self.athlete_id = athlete_id
        if recruit_type is not None:
            self.recruit_type = recruit_type
        if year is not None:
            self.year = year
        if ranking is not None:
            self.ranking = ranking
        if name is not None:
            self.name = name
        if school is not None:
            self.school = school
        if committed_to is not None:
            self.committed_to = committed_to
        if position is not None:
            self.position = position
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight
        if stars is not None:
            self.stars = stars
        if rating is not None:
            self.rating = rating
        if city is not None:
            self.city = city
        if state_province is not None:
            self.state_province = state_province
        if country is not None:
            self.country = country
        if hometown_info is not None:
            self.hometown_info = hometown_info

    @property
    def id(self):
        """Gets the id of this Recruit.  # noqa: E501


        :return: The id of this Recruit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Recruit.


        :param id: The id of this Recruit.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def athlete_id(self):
        """Gets the athlete_id of this Recruit.  # noqa: E501


        :return: The athlete_id of this Recruit.  # noqa: E501
        :rtype: int
        """
        return self._athlete_id

    @athlete_id.setter
    def athlete_id(self, athlete_id):
        """Sets the athlete_id of this Recruit.


        :param athlete_id: The athlete_id of this Recruit.  # noqa: E501
        :type: int
        """

        self._athlete_id = athlete_id

    @property
    def recruit_type(self):
        """Gets the recruit_type of this Recruit.  # noqa: E501


        :return: The recruit_type of this Recruit.  # noqa: E501
        :rtype: str
        """
        return self._recruit_type

    @recruit_type.setter
    def recruit_type(self, recruit_type):
        """Sets the recruit_type of this Recruit.


        :param recruit_type: The recruit_type of this Recruit.  # noqa: E501
        :type: str
        """

        self._recruit_type = recruit_type

    @property
    def year(self):
        """Gets the year of this Recruit.  # noqa: E501


        :return: The year of this Recruit.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Recruit.


        :param year: The year of this Recruit.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def ranking(self):
        """Gets the ranking of this Recruit.  # noqa: E501


        :return: The ranking of this Recruit.  # noqa: E501
        :rtype: int
        """
        return self._ranking

    @ranking.setter
    def ranking(self, ranking):
        """Sets the ranking of this Recruit.


        :param ranking: The ranking of this Recruit.  # noqa: E501
        :type: int
        """

        self._ranking = ranking

    @property
    def name(self):
        """Gets the name of this Recruit.  # noqa: E501


        :return: The name of this Recruit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Recruit.


        :param name: The name of this Recruit.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def school(self):
        """Gets the school of this Recruit.  # noqa: E501


        :return: The school of this Recruit.  # noqa: E501
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this Recruit.


        :param school: The school of this Recruit.  # noqa: E501
        :type: str
        """

        self._school = school

    @property
    def committed_to(self):
        """Gets the committed_to of this Recruit.  # noqa: E501


        :return: The committed_to of this Recruit.  # noqa: E501
        :rtype: str
        """
        return self._committed_to

    @committed_to.setter
    def committed_to(self, committed_to):
        """Sets the committed_to of this Recruit.


        :param committed_to: The committed_to of this Recruit.  # noqa: E501
        :type: str
        """

        self._committed_to = committed_to

    @property
    def position(self):
        """Gets the position of this Recruit.  # noqa: E501


        :return: The position of this Recruit.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Recruit.


        :param position: The position of this Recruit.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def height(self):
        """Gets the height of this Recruit.  # noqa: E501


        :return: The height of this Recruit.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Recruit.


        :param height: The height of this Recruit.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this Recruit.  # noqa: E501


        :return: The weight of this Recruit.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Recruit.


        :param weight: The weight of this Recruit.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def stars(self):
        """Gets the stars of this Recruit.  # noqa: E501


        :return: The stars of this Recruit.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this Recruit.


        :param stars: The stars of this Recruit.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def rating(self):
        """Gets the rating of this Recruit.  # noqa: E501


        :return: The rating of this Recruit.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this Recruit.


        :param rating: The rating of this Recruit.  # noqa: E501
        :type: float
        """

        self._rating = rating

    @property
    def city(self):
        """Gets the city of this Recruit.  # noqa: E501


        :return: The city of this Recruit.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Recruit.


        :param city: The city of this Recruit.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_province(self):
        """Gets the state_province of this Recruit.  # noqa: E501


        :return: The state_province of this Recruit.  # noqa: E501
        :rtype: str
        """
        return self._state_province

    @state_province.setter
    def state_province(self, state_province):
        """Sets the state_province of this Recruit.


        :param state_province: The state_province of this Recruit.  # noqa: E501
        :type: str
        """

        self._state_province = state_province

    @property
    def country(self):
        """Gets the country of this Recruit.  # noqa: E501


        :return: The country of this Recruit.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Recruit.


        :param country: The country of this Recruit.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def hometown_info(self):
        """Gets the hometown_info of this Recruit.  # noqa: E501


        :return: The hometown_info of this Recruit.  # noqa: E501
        :rtype: object
        """
        return self._hometown_info

    @hometown_info.setter
    def hometown_info(self, hometown_info):
        """Sets the hometown_info of this Recruit.


        :param hometown_info: The hometown_info of this Recruit.  # noqa: E501
        :type: object
        """

        self._hometown_info = hometown_info

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
        if issubclass(Recruit, dict):
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
        if not isinstance(other, Recruit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Recruit):
            return True

        return self.to_dict() != other.to_dict()
