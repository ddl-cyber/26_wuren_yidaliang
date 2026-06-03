# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/AsState.idl
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


class Metaclass_AsState(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'AsState'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class AsStateConstants(typing.TypedDict):
        pass

    __constants: AsStateConstants = {
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
                'fsd_common_msgs.msg.AsState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__as_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__as_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__as_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__as_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__as_state

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


class AsState(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_AsState):
    """Message class 'AsState'."""

    __slots__ = [
        '_header',
        '_mission',
        '_which_lap',
        '_end',
        '_finished',
        '_camera_state',
        '_lidar_state',
        '_ins_state',
        '_sensor_state',
        '_ready',
        '_count_time',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'mission': 'string',
        'which_lap': 'uint8',
        'end': 'uint8',
        'finished': 'uint8',
        'camera_state': 'uint8',
        'lidar_state': 'uint8',
        'ins_state': 'uint8',
        'sensor_state': 'uint8',
        'ready': 'uint8',
        'count_time': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 mission: typing.Optional[str] = None,  # noqa: E501
                 which_lap: typing.Optional[int] = None,  # noqa: E501
                 end: typing.Optional[int] = None,  # noqa: E501
                 finished: typing.Optional[int] = None,  # noqa: E501
                 camera_state: typing.Optional[int] = None,  # noqa: E501
                 lidar_state: typing.Optional[int] = None,  # noqa: E501
                 ins_state: typing.Optional[int] = None,  # noqa: E501
                 sensor_state: typing.Optional[int] = None,  # noqa: E501
                 ready: typing.Optional[int] = None,  # noqa: E501
                 count_time: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.mission = mission if mission is not None else str()
        self.which_lap = which_lap if which_lap is not None else int()
        self.end = end if end is not None else int()
        self.finished = finished if finished is not None else int()
        self.camera_state = camera_state if camera_state is not None else int()
        self.lidar_state = lidar_state if lidar_state is not None else int()
        self.ins_state = ins_state if ins_state is not None else int()
        self.sensor_state = sensor_state if sensor_state is not None else int()
        self.ready = ready if ready is not None else int()
        self.count_time = count_time if count_time is not None else float()

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
        if not isinstance(other, AsState):
            return False
        if self.header != other.header:
            return False
        if self.mission != other.mission:
            return False
        if self.which_lap != other.which_lap:
            return False
        if self.end != other.end:
            return False
        if self.finished != other.finished:
            return False
        if self.camera_state != other.camera_state:
            return False
        if self.lidar_state != other.lidar_state:
            return False
        if self.ins_state != other.ins_state:
            return False
        if self.sensor_state != other.sensor_state:
            return False
        if self.ready != other.ready:
            return False
        if self.count_time != other.count_time:
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
    def mission(self) -> str:
        """Message field 'mission'."""
        return self._mission

    @mission.setter
    def mission(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'mission' field must be of type 'str'"

        self._mission = value

    @builtins.property
    def which_lap(self) -> int:
        """Message field 'which_lap'."""
        return self._which_lap

    @which_lap.setter
    def which_lap(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'which_lap' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'which_lap' field must be an unsigned integer in [0, 255]"

        self._which_lap = value

    @builtins.property
    def end(self) -> int:
        """Message field 'end'."""
        return self._end

    @end.setter
    def end(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'end' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'end' field must be an unsigned integer in [0, 255]"

        self._end = value

    @builtins.property
    def finished(self) -> int:
        """Message field 'finished'."""
        return self._finished

    @finished.setter
    def finished(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'finished' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'finished' field must be an unsigned integer in [0, 255]"

        self._finished = value

    @builtins.property
    def camera_state(self) -> int:
        """Message field 'camera_state'."""
        return self._camera_state

    @camera_state.setter
    def camera_state(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'camera_state' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'camera_state' field must be an unsigned integer in [0, 255]"

        self._camera_state = value

    @builtins.property
    def lidar_state(self) -> int:
        """Message field 'lidar_state'."""
        return self._lidar_state

    @lidar_state.setter
    def lidar_state(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'lidar_state' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'lidar_state' field must be an unsigned integer in [0, 255]"

        self._lidar_state = value

    @builtins.property
    def ins_state(self) -> int:
        """Message field 'ins_state'."""
        return self._ins_state

    @ins_state.setter
    def ins_state(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'ins_state' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'ins_state' field must be an unsigned integer in [0, 255]"

        self._ins_state = value

    @builtins.property
    def sensor_state(self) -> int:
        """Message field 'sensor_state'."""
        return self._sensor_state

    @sensor_state.setter
    def sensor_state(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'sensor_state' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'sensor_state' field must be an unsigned integer in [0, 255]"

        self._sensor_state = value

    @builtins.property
    def ready(self) -> int:
        """Message field 'ready'."""
        return self._ready

    @ready.setter
    def ready(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'ready' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'ready' field must be an unsigned integer in [0, 255]"

        self._ready = value

    @builtins.property
    def count_time(self) -> float:
        """Message field 'count_time'."""
        return self._count_time

    @count_time.setter
    def count_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'count_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'count_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._count_time = value
