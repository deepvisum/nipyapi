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


class ConnectableComponent(object):
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
        'id': 'str',
        'type': 'str',
        'group_id': 'str',
        'name': 'str',
        'comments': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'group_id': 'groupId',
        'name': 'name',
        'comments': 'comments'
    }

    def __init__(self, id=None, type=None, group_id=None, name=None, comments=None):
        """
        ConnectableComponent - a model defined in Swagger
        """

        self._id = None
        self._type = None
        self._group_id = None
        self._name = None
        self._comments = None

        self.id = id
        self.type = type
        self.group_id = group_id
        if name is not None:
          self.name = name
        if comments is not None:
          self.comments = comments

    @property
    def id(self):
        """
        Gets the id of this ConnectableComponent.
        The id of the connectable component.

        :return: The id of this ConnectableComponent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectableComponent.
        The id of the connectable component.

        :param id: The id of this ConnectableComponent.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this ConnectableComponent.
        The type of component the connectable is.

        :return: The type of this ConnectableComponent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConnectableComponent.
        The type of component the connectable is.

        :param type: The type of this ConnectableComponent.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["PROCESSOR", "REMOTE_INPUT_PORT", "REMOTE_OUTPUT_PORT", "INPUT_PORT", "OUTPUT_PORT", "FUNNEL"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def group_id(self):
        """
        Gets the group_id of this ConnectableComponent.
        The id of the group that the connectable component resides in

        :return: The group_id of this ConnectableComponent.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this ConnectableComponent.
        The id of the group that the connectable component resides in

        :param group_id: The group_id of this ConnectableComponent.
        :type: str
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")

        self._group_id = group_id

    @property
    def name(self):
        """
        Gets the name of this ConnectableComponent.
        The name of the connectable component

        :return: The name of this ConnectableComponent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectableComponent.
        The name of the connectable component

        :param name: The name of this ConnectableComponent.
        :type: str
        """

        self._name = name

    @property
    def comments(self):
        """
        Gets the comments of this ConnectableComponent.
        The comments for the connectable component.

        :return: The comments of this ConnectableComponent.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this ConnectableComponent.
        The comments for the connectable component.

        :param comments: The comments of this ConnectableComponent.
        :type: str
        """

        self._comments = comments

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
        if not isinstance(other, ConnectableComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
