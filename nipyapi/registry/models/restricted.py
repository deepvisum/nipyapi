# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 0.5.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Restricted(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'general_restriction_explanation': 'str',
        'restrictions': 'list[Restriction]'
    }

    attribute_map = {
        'general_restriction_explanation': 'generalRestrictionExplanation',
        'restrictions': 'restrictions'
    }

    def __init__(self, general_restriction_explanation=None, restrictions=None):
        """
        Restricted - a model defined in Swagger
        """

        self._general_restriction_explanation = None
        self._restrictions = None

        if general_restriction_explanation is not None:
          self.general_restriction_explanation = general_restriction_explanation
        if restrictions is not None:
          self.restrictions = restrictions

    @property
    def general_restriction_explanation(self):
        """
        Gets the general_restriction_explanation of this Restricted.
        The general restriction for the extension, or null if only specific restrictions exist

        :return: The general_restriction_explanation of this Restricted.
        :rtype: str
        """
        return self._general_restriction_explanation

    @general_restriction_explanation.setter
    def general_restriction_explanation(self, general_restriction_explanation):
        """
        Sets the general_restriction_explanation of this Restricted.
        The general restriction for the extension, or null if only specific restrictions exist

        :param general_restriction_explanation: The general_restriction_explanation of this Restricted.
        :type: str
        """

        self._general_restriction_explanation = general_restriction_explanation

    @property
    def restrictions(self):
        """
        Gets the restrictions of this Restricted.
        The specific restrictions

        :return: The restrictions of this Restricted.
        :rtype: list[Restriction]
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """
        Sets the restrictions of this Restricted.
        The specific restrictions

        :param restrictions: The restrictions of this Restricted.
        :type: list[Restriction]
        """

        self._restrictions = restrictions

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
        if not isinstance(other, Restricted):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
