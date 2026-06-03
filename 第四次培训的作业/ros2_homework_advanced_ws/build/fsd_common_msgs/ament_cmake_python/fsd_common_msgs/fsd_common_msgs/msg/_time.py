# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/Time.idl
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


class Metaclass_Time(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'Time'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class TimeConstants(typing.TypedDict):
        pass

    __constants: TimeConstants = {
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
                'fsd_common_msgs.msg.Time')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__time
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__time
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__time
            cls._TYPE_SUPPORT = module.type_support_msg__msg__time
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__time

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


class Time(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_Time):
    """Message class 'Time'."""

    __slots__ = [
        '_header',
        '_frame_id_num',
        '_sum_compute_time',
        '_control_compute_time',
        '_boundary_detector_compute_time',
        '_line_detector_compute_time',
        '_skidpad_detector_compute_time',
        '_lidar_detection_compute_time',
        '_camera_detection_compute_time',
        '_fusion_detection_compute_time',
        '_time2',
        '_time3',
        '_time4',
        '_time5',
        '_time6',
        '_time7',
        '_time8',
        '_time9',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'frame_id_num': 'uint64',
        'sum_compute_time': 'float',
        'control_compute_time': 'float',
        'boundary_detector_compute_time': 'float',
        'line_detector_compute_time': 'float',
        'skidpad_detector_compute_time': 'float',
        'lidar_detection_compute_time': 'float',
        'camera_detection_compute_time': 'float',
        'fusion_detection_compute_time': 'float',
        'time2': 'float',
        'time3': 'float',
        'time4': 'float',
        'time5': 'float',
        'time6': 'float',
        'time7': 'float',
        'time8': 'float',
        'time9': 'float',
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
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 frame_id_num: typing.Optional[int] = None,  # noqa: E501
                 sum_compute_time: typing.Optional[float] = None,  # noqa: E501
                 control_compute_time: typing.Optional[float] = None,  # noqa: E501
                 boundary_detector_compute_time: typing.Optional[float] = None,  # noqa: E501
                 line_detector_compute_time: typing.Optional[float] = None,  # noqa: E501
                 skidpad_detector_compute_time: typing.Optional[float] = None,  # noqa: E501
                 lidar_detection_compute_time: typing.Optional[float] = None,  # noqa: E501
                 camera_detection_compute_time: typing.Optional[float] = None,  # noqa: E501
                 fusion_detection_compute_time: typing.Optional[float] = None,  # noqa: E501
                 time2: typing.Optional[float] = None,  # noqa: E501
                 time3: typing.Optional[float] = None,  # noqa: E501
                 time4: typing.Optional[float] = None,  # noqa: E501
                 time5: typing.Optional[float] = None,  # noqa: E501
                 time6: typing.Optional[float] = None,  # noqa: E501
                 time7: typing.Optional[float] = None,  # noqa: E501
                 time8: typing.Optional[float] = None,  # noqa: E501
                 time9: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.frame_id_num = frame_id_num if frame_id_num is not None else int()
        self.sum_compute_time = sum_compute_time if sum_compute_time is not None else float()
        self.control_compute_time = control_compute_time if control_compute_time is not None else float()
        self.boundary_detector_compute_time = boundary_detector_compute_time if boundary_detector_compute_time is not None else float()
        self.line_detector_compute_time = line_detector_compute_time if line_detector_compute_time is not None else float()
        self.skidpad_detector_compute_time = skidpad_detector_compute_time if skidpad_detector_compute_time is not None else float()
        self.lidar_detection_compute_time = lidar_detection_compute_time if lidar_detection_compute_time is not None else float()
        self.camera_detection_compute_time = camera_detection_compute_time if camera_detection_compute_time is not None else float()
        self.fusion_detection_compute_time = fusion_detection_compute_time if fusion_detection_compute_time is not None else float()
        self.time2 = time2 if time2 is not None else float()
        self.time3 = time3 if time3 is not None else float()
        self.time4 = time4 if time4 is not None else float()
        self.time5 = time5 if time5 is not None else float()
        self.time6 = time6 if time6 is not None else float()
        self.time7 = time7 if time7 is not None else float()
        self.time8 = time8 if time8 is not None else float()
        self.time9 = time9 if time9 is not None else float()

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
        if not isinstance(other, Time):
            return False
        if self.header != other.header:
            return False
        if self.frame_id_num != other.frame_id_num:
            return False
        if self.sum_compute_time != other.sum_compute_time:
            return False
        if self.control_compute_time != other.control_compute_time:
            return False
        if self.boundary_detector_compute_time != other.boundary_detector_compute_time:
            return False
        if self.line_detector_compute_time != other.line_detector_compute_time:
            return False
        if self.skidpad_detector_compute_time != other.skidpad_detector_compute_time:
            return False
        if self.lidar_detection_compute_time != other.lidar_detection_compute_time:
            return False
        if self.camera_detection_compute_time != other.camera_detection_compute_time:
            return False
        if self.fusion_detection_compute_time != other.fusion_detection_compute_time:
            return False
        if self.time2 != other.time2:
            return False
        if self.time3 != other.time3:
            return False
        if self.time4 != other.time4:
            return False
        if self.time5 != other.time5:
            return False
        if self.time6 != other.time6:
            return False
        if self.time7 != other.time7:
            return False
        if self.time8 != other.time8:
            return False
        if self.time9 != other.time9:
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
    def sum_compute_time(self) -> float:
        """Message field 'sum_compute_time'."""
        return self._sum_compute_time

    @sum_compute_time.setter
    def sum_compute_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'sum_compute_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'sum_compute_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._sum_compute_time = value

    @builtins.property
    def control_compute_time(self) -> float:
        """Message field 'control_compute_time'."""
        return self._control_compute_time

    @control_compute_time.setter
    def control_compute_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'control_compute_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'control_compute_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._control_compute_time = value

    @builtins.property
    def boundary_detector_compute_time(self) -> float:
        """Message field 'boundary_detector_compute_time'."""
        return self._boundary_detector_compute_time

    @boundary_detector_compute_time.setter
    def boundary_detector_compute_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'boundary_detector_compute_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'boundary_detector_compute_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._boundary_detector_compute_time = value

    @builtins.property
    def line_detector_compute_time(self) -> float:
        """Message field 'line_detector_compute_time'."""
        return self._line_detector_compute_time

    @line_detector_compute_time.setter
    def line_detector_compute_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'line_detector_compute_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'line_detector_compute_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._line_detector_compute_time = value

    @builtins.property
    def skidpad_detector_compute_time(self) -> float:
        """Message field 'skidpad_detector_compute_time'."""
        return self._skidpad_detector_compute_time

    @skidpad_detector_compute_time.setter
    def skidpad_detector_compute_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'skidpad_detector_compute_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'skidpad_detector_compute_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._skidpad_detector_compute_time = value

    @builtins.property
    def lidar_detection_compute_time(self) -> float:
        """Message field 'lidar_detection_compute_time'."""
        return self._lidar_detection_compute_time

    @lidar_detection_compute_time.setter
    def lidar_detection_compute_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'lidar_detection_compute_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'lidar_detection_compute_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._lidar_detection_compute_time = value

    @builtins.property
    def camera_detection_compute_time(self) -> float:
        """Message field 'camera_detection_compute_time'."""
        return self._camera_detection_compute_time

    @camera_detection_compute_time.setter
    def camera_detection_compute_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'camera_detection_compute_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'camera_detection_compute_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._camera_detection_compute_time = value

    @builtins.property
    def fusion_detection_compute_time(self) -> float:
        """Message field 'fusion_detection_compute_time'."""
        return self._fusion_detection_compute_time

    @fusion_detection_compute_time.setter
    def fusion_detection_compute_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'fusion_detection_compute_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'fusion_detection_compute_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._fusion_detection_compute_time = value

    @builtins.property
    def time2(self) -> float:
        """Message field 'time2'."""
        return self._time2

    @time2.setter
    def time2(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'time2' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'time2' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._time2 = value

    @builtins.property
    def time3(self) -> float:
        """Message field 'time3'."""
        return self._time3

    @time3.setter
    def time3(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'time3' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'time3' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._time3 = value

    @builtins.property
    def time4(self) -> float:
        """Message field 'time4'."""
        return self._time4

    @time4.setter
    def time4(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'time4' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'time4' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._time4 = value

    @builtins.property
    def time5(self) -> float:
        """Message field 'time5'."""
        return self._time5

    @time5.setter
    def time5(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'time5' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'time5' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._time5 = value

    @builtins.property
    def time6(self) -> float:
        """Message field 'time6'."""
        return self._time6

    @time6.setter
    def time6(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'time6' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'time6' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._time6 = value

    @builtins.property
    def time7(self) -> float:
        """Message field 'time7'."""
        return self._time7

    @time7.setter
    def time7(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'time7' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'time7' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._time7 = value

    @builtins.property
    def time8(self) -> float:
        """Message field 'time8'."""
        return self._time8

    @time8.setter
    def time8(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'time8' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'time8' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._time8 = value

    @builtins.property
    def time9(self) -> float:
        """Message field 'time9'."""
        return self._time9

    @time9.setter
    def time9(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'time9' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'time9' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._time9 = value
