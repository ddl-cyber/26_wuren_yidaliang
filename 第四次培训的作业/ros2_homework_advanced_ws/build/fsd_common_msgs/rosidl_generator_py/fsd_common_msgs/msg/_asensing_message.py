# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsd_common_msgs:msg/AsensingMessage.idl
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


class Metaclass_AsensingMessage(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'AsensingMessage'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class AsensingMessageConstants(typing.TypedDict):
        pass

    __constants: AsensingMessageConstants = {
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
                'fsd_common_msgs.msg.AsensingMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__asensing_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__asensing_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__asensing_message
            cls._TYPE_SUPPORT = module.type_support_msg__msg__asensing_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__asensing_message

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


class AsensingMessage(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_AsensingMessage):
    """Message class 'AsensingMessage'."""

    __slots__ = [
        '_header',
        '_frame_id_num',
        '_lat',
        '_lon',
        '_h',
        '_vn',
        '_ve',
        '_vh',
        '_roll',
        '_pitch',
        '_heading_angle',
        '_gyro_x',
        '_gyro_y',
        '_gyro_z',
        '_acc_x',
        '_acc_y',
        '_acc_z',
        '_std_lat',
        '_std_lon',
        '_std_local_height',
        '_north_velocity_std',
        '_east_velocity_std',
        '_ground_velocity_std',
        '_roll_std',
        '_pitch_std',
        '_std_heading',
        '_status',
        '_gps_flag_pos',
        '_gps_week_number',
        '_ull_timestamp',
        '_temperature',
        '_car_status',
        '_gps_flag_heading',
        '_num_sv',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'frame_id_num': 'uint64',
        'lat': 'double',
        'lon': 'double',
        'h': 'double',
        'vn': 'double',
        've': 'double',
        'vh': 'double',
        'roll': 'double',
        'pitch': 'double',
        'heading_angle': 'double',
        'gyro_x': 'double',
        'gyro_y': 'double',
        'gyro_z': 'double',
        'acc_x': 'double',
        'acc_y': 'double',
        'acc_z': 'double',
        'std_lat': 'float',
        'std_lon': 'float',
        'std_local_height': 'float',
        'north_velocity_std': 'float',
        'east_velocity_std': 'float',
        'ground_velocity_std': 'float',
        'roll_std': 'float',
        'pitch_std': 'float',
        'std_heading': 'float',
        'status': 'uint32',
        'gps_flag_pos': 'uint32',
        'gps_week_number': 'double',
        'ull_timestamp': 'double',
        'temperature': 'float',
        'car_status': 'uint32',
        'gps_flag_heading': 'uint32',
        'num_sv': 'uint32',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 frame_id_num: typing.Optional[int] = None,  # noqa: E501
                 lat: typing.Optional[float] = None,  # noqa: E501
                 lon: typing.Optional[float] = None,  # noqa: E501
                 h: typing.Optional[float] = None,  # noqa: E501
                 vn: typing.Optional[float] = None,  # noqa: E501
                 ve: typing.Optional[float] = None,  # noqa: E501
                 vh: typing.Optional[float] = None,  # noqa: E501
                 roll: typing.Optional[float] = None,  # noqa: E501
                 pitch: typing.Optional[float] = None,  # noqa: E501
                 heading_angle: typing.Optional[float] = None,  # noqa: E501
                 gyro_x: typing.Optional[float] = None,  # noqa: E501
                 gyro_y: typing.Optional[float] = None,  # noqa: E501
                 gyro_z: typing.Optional[float] = None,  # noqa: E501
                 acc_x: typing.Optional[float] = None,  # noqa: E501
                 acc_y: typing.Optional[float] = None,  # noqa: E501
                 acc_z: typing.Optional[float] = None,  # noqa: E501
                 std_lat: typing.Optional[float] = None,  # noqa: E501
                 std_lon: typing.Optional[float] = None,  # noqa: E501
                 std_local_height: typing.Optional[float] = None,  # noqa: E501
                 north_velocity_std: typing.Optional[float] = None,  # noqa: E501
                 east_velocity_std: typing.Optional[float] = None,  # noqa: E501
                 ground_velocity_std: typing.Optional[float] = None,  # noqa: E501
                 roll_std: typing.Optional[float] = None,  # noqa: E501
                 pitch_std: typing.Optional[float] = None,  # noqa: E501
                 std_heading: typing.Optional[float] = None,  # noqa: E501
                 status: typing.Optional[int] = None,  # noqa: E501
                 gps_flag_pos: typing.Optional[int] = None,  # noqa: E501
                 gps_week_number: typing.Optional[float] = None,  # noqa: E501
                 ull_timestamp: typing.Optional[float] = None,  # noqa: E501
                 temperature: typing.Optional[float] = None,  # noqa: E501
                 car_status: typing.Optional[int] = None,  # noqa: E501
                 gps_flag_heading: typing.Optional[int] = None,  # noqa: E501
                 num_sv: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.frame_id_num = frame_id_num if frame_id_num is not None else int()
        self.lat = lat if lat is not None else float()
        self.lon = lon if lon is not None else float()
        self.h = h if h is not None else float()
        self.vn = vn if vn is not None else float()
        self.ve = ve if ve is not None else float()
        self.vh = vh if vh is not None else float()
        self.roll = roll if roll is not None else float()
        self.pitch = pitch if pitch is not None else float()
        self.heading_angle = heading_angle if heading_angle is not None else float()
        self.gyro_x = gyro_x if gyro_x is not None else float()
        self.gyro_y = gyro_y if gyro_y is not None else float()
        self.gyro_z = gyro_z if gyro_z is not None else float()
        self.acc_x = acc_x if acc_x is not None else float()
        self.acc_y = acc_y if acc_y is not None else float()
        self.acc_z = acc_z if acc_z is not None else float()
        self.std_lat = std_lat if std_lat is not None else float()
        self.std_lon = std_lon if std_lon is not None else float()
        self.std_local_height = std_local_height if std_local_height is not None else float()
        self.north_velocity_std = north_velocity_std if north_velocity_std is not None else float()
        self.east_velocity_std = east_velocity_std if east_velocity_std is not None else float()
        self.ground_velocity_std = ground_velocity_std if ground_velocity_std is not None else float()
        self.roll_std = roll_std if roll_std is not None else float()
        self.pitch_std = pitch_std if pitch_std is not None else float()
        self.std_heading = std_heading if std_heading is not None else float()
        self.status = status if status is not None else int()
        self.gps_flag_pos = gps_flag_pos if gps_flag_pos is not None else int()
        self.gps_week_number = gps_week_number if gps_week_number is not None else float()
        self.ull_timestamp = ull_timestamp if ull_timestamp is not None else float()
        self.temperature = temperature if temperature is not None else float()
        self.car_status = car_status if car_status is not None else int()
        self.gps_flag_heading = gps_flag_heading if gps_flag_heading is not None else int()
        self.num_sv = num_sv if num_sv is not None else int()

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
        if not isinstance(other, AsensingMessage):
            return False
        if self.header != other.header:
            return False
        if self.frame_id_num != other.frame_id_num:
            return False
        if self.lat != other.lat:
            return False
        if self.lon != other.lon:
            return False
        if self.h != other.h:
            return False
        if self.vn != other.vn:
            return False
        if self.ve != other.ve:
            return False
        if self.vh != other.vh:
            return False
        if self.roll != other.roll:
            return False
        if self.pitch != other.pitch:
            return False
        if self.heading_angle != other.heading_angle:
            return False
        if self.gyro_x != other.gyro_x:
            return False
        if self.gyro_y != other.gyro_y:
            return False
        if self.gyro_z != other.gyro_z:
            return False
        if self.acc_x != other.acc_x:
            return False
        if self.acc_y != other.acc_y:
            return False
        if self.acc_z != other.acc_z:
            return False
        if self.std_lat != other.std_lat:
            return False
        if self.std_lon != other.std_lon:
            return False
        if self.std_local_height != other.std_local_height:
            return False
        if self.north_velocity_std != other.north_velocity_std:
            return False
        if self.east_velocity_std != other.east_velocity_std:
            return False
        if self.ground_velocity_std != other.ground_velocity_std:
            return False
        if self.roll_std != other.roll_std:
            return False
        if self.pitch_std != other.pitch_std:
            return False
        if self.std_heading != other.std_heading:
            return False
        if self.status != other.status:
            return False
        if self.gps_flag_pos != other.gps_flag_pos:
            return False
        if self.gps_week_number != other.gps_week_number:
            return False
        if self.ull_timestamp != other.ull_timestamp:
            return False
        if self.temperature != other.temperature:
            return False
        if self.car_status != other.car_status:
            return False
        if self.gps_flag_heading != other.gps_flag_heading:
            return False
        if self.num_sv != other.num_sv:
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
    def lat(self) -> float:
        """Message field 'lat'."""
        return self._lat

    @lat.setter
    def lat(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'lat' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'lat' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._lat = value

    @builtins.property
    def lon(self) -> float:
        """Message field 'lon'."""
        return self._lon

    @lon.setter
    def lon(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'lon' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'lon' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._lon = value

    @builtins.property
    def h(self) -> float:
        """Message field 'h'."""
        return self._h

    @h.setter
    def h(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'h' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'h' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._h = value

    @builtins.property
    def vn(self) -> float:
        """Message field 'vn'."""
        return self._vn

    @vn.setter
    def vn(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'vn' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'vn' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._vn = value

    @builtins.property
    def ve(self) -> float:
        """Message field 've'."""
        return self._ve

    @ve.setter
    def ve(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 've' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 've' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._ve = value

    @builtins.property
    def vh(self) -> float:
        """Message field 'vh'."""
        return self._vh

    @vh.setter
    def vh(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'vh' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'vh' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._vh = value

    @builtins.property
    def roll(self) -> float:
        """Message field 'roll'."""
        return self._roll

    @roll.setter
    def roll(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'roll' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'roll' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._roll = value

    @builtins.property
    def pitch(self) -> float:
        """Message field 'pitch'."""
        return self._pitch

    @pitch.setter
    def pitch(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'pitch' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'pitch' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._pitch = value

    @builtins.property
    def heading_angle(self) -> float:
        """Message field 'heading_angle'."""
        return self._heading_angle

    @heading_angle.setter
    def heading_angle(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'heading_angle' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'heading_angle' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._heading_angle = value

    @builtins.property
    def gyro_x(self) -> float:
        """Message field 'gyro_x'."""
        return self._gyro_x

    @gyro_x.setter
    def gyro_x(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'gyro_x' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'gyro_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._gyro_x = value

    @builtins.property
    def gyro_y(self) -> float:
        """Message field 'gyro_y'."""
        return self._gyro_y

    @gyro_y.setter
    def gyro_y(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'gyro_y' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'gyro_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._gyro_y = value

    @builtins.property
    def gyro_z(self) -> float:
        """Message field 'gyro_z'."""
        return self._gyro_z

    @gyro_z.setter
    def gyro_z(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'gyro_z' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'gyro_z' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._gyro_z = value

    @builtins.property
    def acc_x(self) -> float:
        """Message field 'acc_x'."""
        return self._acc_x

    @acc_x.setter
    def acc_x(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'acc_x' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'acc_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._acc_x = value

    @builtins.property
    def acc_y(self) -> float:
        """Message field 'acc_y'."""
        return self._acc_y

    @acc_y.setter
    def acc_y(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'acc_y' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'acc_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._acc_y = value

    @builtins.property
    def acc_z(self) -> float:
        """Message field 'acc_z'."""
        return self._acc_z

    @acc_z.setter
    def acc_z(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'acc_z' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'acc_z' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._acc_z = value

    @builtins.property
    def std_lat(self) -> float:
        """Message field 'std_lat'."""
        return self._std_lat

    @std_lat.setter
    def std_lat(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'std_lat' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'std_lat' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._std_lat = value

    @builtins.property
    def std_lon(self) -> float:
        """Message field 'std_lon'."""
        return self._std_lon

    @std_lon.setter
    def std_lon(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'std_lon' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'std_lon' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._std_lon = value

    @builtins.property
    def std_local_height(self) -> float:
        """Message field 'std_local_height'."""
        return self._std_local_height

    @std_local_height.setter
    def std_local_height(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'std_local_height' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'std_local_height' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._std_local_height = value

    @builtins.property
    def north_velocity_std(self) -> float:
        """Message field 'north_velocity_std'."""
        return self._north_velocity_std

    @north_velocity_std.setter
    def north_velocity_std(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'north_velocity_std' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'north_velocity_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._north_velocity_std = value

    @builtins.property
    def east_velocity_std(self) -> float:
        """Message field 'east_velocity_std'."""
        return self._east_velocity_std

    @east_velocity_std.setter
    def east_velocity_std(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'east_velocity_std' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'east_velocity_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._east_velocity_std = value

    @builtins.property
    def ground_velocity_std(self) -> float:
        """Message field 'ground_velocity_std'."""
        return self._ground_velocity_std

    @ground_velocity_std.setter
    def ground_velocity_std(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'ground_velocity_std' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'ground_velocity_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._ground_velocity_std = value

    @builtins.property
    def roll_std(self) -> float:
        """Message field 'roll_std'."""
        return self._roll_std

    @roll_std.setter
    def roll_std(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'roll_std' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'roll_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._roll_std = value

    @builtins.property
    def pitch_std(self) -> float:
        """Message field 'pitch_std'."""
        return self._pitch_std

    @pitch_std.setter
    def pitch_std(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'pitch_std' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'pitch_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._pitch_std = value

    @builtins.property
    def std_heading(self) -> float:
        """Message field 'std_heading'."""
        return self._std_heading

    @std_heading.setter
    def std_heading(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'std_heading' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'std_heading' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._std_heading = value

    @builtins.property
    def status(self) -> int:
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'status' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'status' field must be an unsigned integer in [0, 4294967295]"

        self._status = value

    @builtins.property
    def gps_flag_pos(self) -> int:
        """Message field 'gps_flag_pos'."""
        return self._gps_flag_pos

    @gps_flag_pos.setter
    def gps_flag_pos(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'gps_flag_pos' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'gps_flag_pos' field must be an unsigned integer in [0, 4294967295]"

        self._gps_flag_pos = value

    @builtins.property
    def gps_week_number(self) -> float:
        """Message field 'gps_week_number'."""
        return self._gps_week_number

    @gps_week_number.setter
    def gps_week_number(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'gps_week_number' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'gps_week_number' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._gps_week_number = value

    @builtins.property
    def ull_timestamp(self) -> float:
        """Message field 'ull_timestamp'."""
        return self._ull_timestamp

    @ull_timestamp.setter
    def ull_timestamp(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'ull_timestamp' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'ull_timestamp' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._ull_timestamp = value

    @builtins.property
    def temperature(self) -> float:
        """Message field 'temperature'."""
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'temperature' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'temperature' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._temperature = value

    @builtins.property
    def car_status(self) -> int:
        """Message field 'car_status'."""
        return self._car_status

    @car_status.setter
    def car_status(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'car_status' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'car_status' field must be an unsigned integer in [0, 4294967295]"

        self._car_status = value

    @builtins.property
    def gps_flag_heading(self) -> int:
        """Message field 'gps_flag_heading'."""
        return self._gps_flag_heading

    @gps_flag_heading.setter
    def gps_flag_heading(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'gps_flag_heading' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'gps_flag_heading' field must be an unsigned integer in [0, 4294967295]"

        self._gps_flag_heading = value

    @builtins.property
    def num_sv(self) -> int:
        """Message field 'num_sv'."""
        return self._num_sv

    @num_sv.setter
    def num_sv(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'num_sv' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'num_sv' field must be an unsigned integer in [0, 4294967295]"

        self._num_sv = value
