# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/Feedback.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
import os
import typing

import rosidl_pycommon.interface_base_classes

if typing.TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = os.getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Feedback(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'Feedback'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FeedbackConstants(typing.TypedDict):
        pass

    __constants: FeedbackConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('fsd_common_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fsd_common_msgs.msg.Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__msg__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__feedback

            from std_msgs.msg import Header
            if Header._TYPE_SUPPORT is None:
                Header.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Feedback(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_Feedback):
    """Message class 'Feedback'."""

    __slots__ = [
        '_header',
        '_frame_id_num',
        '_wheel_speed_fl',
        '_wheel_speed_fr',
        '_wheel_speed_rl',
        '_wheel_speed_rr',
        '_motor_command_speed_rl',
        '_motor_command_speed_rr',
        '_motor_return_speed_rl',
        '_motor_return_speed_rr',
        '_motor_command_torq_rl',
        '_motor_command_torq_rr',
        '_motor_return_torq_rl',
        '_motor_return_torq_rr',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'frame_id_num': 'uint64',
        'wheel_speed_fl': 'float',
        'wheel_speed_fr': 'float',
        'wheel_speed_rl': 'float',
        'wheel_speed_rr': 'float',
        'motor_command_speed_rl': 'float',
        'motor_command_speed_rr': 'float',
        'motor_return_speed_rl': 'float',
        'motor_return_speed_rr': 'float',
        'motor_command_torq_rl': 'float',
        'motor_command_torq_rr': 'float',
        'motor_return_torq_rl': 'float',
        'motor_return_torq_rr': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 frame_id_num: typing.Optional[int] = None,  # noqa: E501
                 wheel_speed_fl: typing.Optional[float] = None,  # noqa: E501
                 wheel_speed_fr: typing.Optional[float] = None,  # noqa: E501
                 wheel_speed_rl: typing.Optional[float] = None,  # noqa: E501
                 wheel_speed_rr: typing.Optional[float] = None,  # noqa: E501
                 motor_command_speed_rl: typing.Optional[float] = None,  # noqa: E501
                 motor_command_speed_rr: typing.Optional[float] = None,  # noqa: E501
                 motor_return_speed_rl: typing.Optional[float] = None,  # noqa: E501
                 motor_return_speed_rr: typing.Optional[float] = None,  # noqa: E501
                 motor_command_torq_rl: typing.Optional[float] = None,  # noqa: E501
                 motor_command_torq_rr: typing.Optional[float] = None,  # noqa: E501
                 motor_return_torq_rl: typing.Optional[float] = None,  # noqa: E501
                 motor_return_torq_rr: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.frame_id_num = frame_id_num if frame_id_num is not None else int()
        self.wheel_speed_fl = wheel_speed_fl if wheel_speed_fl is not None else float()
        self.wheel_speed_fr = wheel_speed_fr if wheel_speed_fr is not None else float()
        self.wheel_speed_rl = wheel_speed_rl if wheel_speed_rl is not None else float()
        self.wheel_speed_rr = wheel_speed_rr if wheel_speed_rr is not None else float()
        self.motor_command_speed_rl = motor_command_speed_rl if motor_command_speed_rl is not None else float()
        self.motor_command_speed_rr = motor_command_speed_rr if motor_command_speed_rr is not None else float()
        self.motor_return_speed_rl = motor_return_speed_rl if motor_return_speed_rl is not None else float()
        self.motor_return_speed_rr = motor_return_speed_rr if motor_return_speed_rr is not None else float()
        self.motor_command_torq_rl = motor_command_torq_rl if motor_command_torq_rl is not None else float()
        self.motor_command_torq_rr = motor_command_torq_rr if motor_command_torq_rr is not None else float()
        self.motor_return_torq_rl = motor_return_torq_rl if motor_return_torq_rl is not None else float()
        self.motor_return_torq_rr = motor_return_torq_rr if motor_return_torq_rr is not None else float()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    from rosidl_buffer import Buffer as _RosidlBuffer
                    if not isinstance(field, _RosidlBuffer):
                        if self._check_fields:
                            assert fieldstr.startswith('array(')
                        prefix = "array('X', "
                        suffix = ')'
                        fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Feedback):
            return False
        if self.header != other.header:
            return False
        if self.frame_id_num != other.frame_id_num:
            return False
        if self.wheel_speed_fl != other.wheel_speed_fl:
            return False
        if self.wheel_speed_fr != other.wheel_speed_fr:
            return False
        if self.wheel_speed_rl != other.wheel_speed_rl:
            return False
        if self.wheel_speed_rr != other.wheel_speed_rr:
            return False
        if self.motor_command_speed_rl != other.motor_command_speed_rl:
            return False
        if self.motor_command_speed_rr != other.motor_command_speed_rr:
            return False
        if self.motor_return_speed_rl != other.motor_return_speed_rl:
            return False
        if self.motor_return_speed_rr != other.motor_return_speed_rr:
            return False
        if self.motor_command_torq_rl != other.motor_command_torq_rl:
            return False
        if self.motor_command_torq_rr != other.motor_command_torq_rr:
            return False
        if self.motor_return_torq_rl != other.motor_return_torq_rl:
            return False
        if self.motor_return_torq_rr != other.motor_return_torq_rr:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self) -> std_msgs.msg.Header:
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None:
        from std_msgs.msg import Header

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Header), \
                    "The 'header' field must be a sub message of type 'Header'"

        self._header = value

    @builtins.property
    def frame_id_num(self) -> int:
        """Message field 'frame_id_num'."""
        return self._frame_id_num

    @frame_id_num.setter
    def frame_id_num(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'frame_id_num' field must be of type 'int'"
                assert value >= 0 and value < 18446744073709551616, \
                    "The 'frame_id_num' field must be an unsigned integer in [0, 18446744073709551615]"

        self._frame_id_num = value

    @builtins.property
    def wheel_speed_fl(self) -> float:
        """Message field 'wheel_speed_fl'."""
        return self._wheel_speed_fl

    @wheel_speed_fl.setter
    def wheel_speed_fl(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'wheel_speed_fl' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'wheel_speed_fl' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._wheel_speed_fl = value

    @builtins.property
    def wheel_speed_fr(self) -> float:
        """Message field 'wheel_speed_fr'."""
        return self._wheel_speed_fr

    @wheel_speed_fr.setter
    def wheel_speed_fr(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'wheel_speed_fr' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'wheel_speed_fr' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._wheel_speed_fr = value

    @builtins.property
    def wheel_speed_rl(self) -> float:
        """Message field 'wheel_speed_rl'."""
        return self._wheel_speed_rl

    @wheel_speed_rl.setter
    def wheel_speed_rl(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'wheel_speed_rl' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'wheel_speed_rl' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._wheel_speed_rl = value

    @builtins.property
    def wheel_speed_rr(self) -> float:
        """Message field 'wheel_speed_rr'."""
        return self._wheel_speed_rr

    @wheel_speed_rr.setter
    def wheel_speed_rr(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'wheel_speed_rr' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'wheel_speed_rr' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._wheel_speed_rr = value

    @builtins.property
    def motor_command_speed_rl(self) -> float:
        """Message field 'motor_command_speed_rl'."""
        return self._motor_command_speed_rl

    @motor_command_speed_rl.setter
    def motor_command_speed_rl(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_command_speed_rl' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_command_speed_rl' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_command_speed_rl = value

    @builtins.property
    def motor_command_speed_rr(self) -> float:
        """Message field 'motor_command_speed_rr'."""
        return self._motor_command_speed_rr

    @motor_command_speed_rr.setter
    def motor_command_speed_rr(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_command_speed_rr' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_command_speed_rr' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_command_speed_rr = value

    @builtins.property
    def motor_return_speed_rl(self) -> float:
        """Message field 'motor_return_speed_rl'."""
        return self._motor_return_speed_rl

    @motor_return_speed_rl.setter
    def motor_return_speed_rl(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_return_speed_rl' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_return_speed_rl' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_return_speed_rl = value

    @builtins.property
    def motor_return_speed_rr(self) -> float:
        """Message field 'motor_return_speed_rr'."""
        return self._motor_return_speed_rr

    @motor_return_speed_rr.setter
    def motor_return_speed_rr(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_return_speed_rr' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_return_speed_rr' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_return_speed_rr = value

    @builtins.property
    def motor_command_torq_rl(self) -> float:
        """Message field 'motor_command_torq_rl'."""
        return self._motor_command_torq_rl

    @motor_command_torq_rl.setter
    def motor_command_torq_rl(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_command_torq_rl' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_command_torq_rl' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_command_torq_rl = value

    @builtins.property
    def motor_command_torq_rr(self) -> float:
        """Message field 'motor_command_torq_rr'."""
        return self._motor_command_torq_rr

    @motor_command_torq_rr.setter
    def motor_command_torq_rr(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_command_torq_rr' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_command_torq_rr' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_command_torq_rr = value

    @builtins.property
    def motor_return_torq_rl(self) -> float:
        """Message field 'motor_return_torq_rl'."""
        return self._motor_return_torq_rl

    @motor_return_torq_rl.setter
    def motor_return_torq_rl(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_return_torq_rl' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_return_torq_rl' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_return_torq_rl = value

    @builtins.property
    def motor_return_torq_rr(self) -> float:
        """Message field 'motor_return_torq_rr'."""
        return self._motor_return_torq_rr

    @motor_return_torq_rr.setter
    def motor_return_torq_rr(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'motor_return_torq_rr' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'motor_return_torq_rr' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._motor_return_torq_rr = value
