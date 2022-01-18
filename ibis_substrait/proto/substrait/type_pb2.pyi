"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Type(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    class _Nullability:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _NullabilityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Nullability.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        NULLABILITY_UNSPECIFIED: Type.Nullability.ValueType = ...
        NULLABILITY_NULLABLE: Type.Nullability.ValueType = ...
        NULLABILITY_REQUIRED: Type.Nullability.ValueType = ...

    class Nullability(_Nullability, metaclass=_NullabilityEnumTypeWrapper):
        pass
    NULLABILITY_UNSPECIFIED: Type.Nullability.ValueType = ...
    NULLABILITY_NULLABLE: Type.Nullability.ValueType = ...
    NULLABILITY_REQUIRED: Type.Nullability.ValueType = ...

    class Boolean(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class I8(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class I16(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class I32(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class I64(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class FP32(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class FP64(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class String(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class Binary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class Timestamp(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class Date(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class Time(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class TimestampTZ(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class IntervalYear(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class IntervalDay(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class UUID(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class FixedChar(google.protobuf.message.Message):
        """Start compound types."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        length: builtins.int = ...
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, length: builtins.int=..., type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['length', b'length', 'nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class VarChar(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        length: builtins.int = ...
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, length: builtins.int=..., type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['length', b'length', 'nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class FixedBinary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        length: builtins.int = ...
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, length: builtins.int=..., type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['length', b'length', 'nullability', b'nullability', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class Decimal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        SCALE_FIELD_NUMBER: builtins.int
        PRECISION_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int
        scale: builtins.int = ...
        precision: builtins.int = ...
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, scale: builtins.int=..., precision: builtins.int=..., type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'precision', b'precision', 'scale', b'scale', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class Struct(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPES_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int

        @property
        def types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Type]:
            ...
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, types: typing.Optional[typing.Iterable[global___Type]]=..., type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type_variation_reference', b'type_variation_reference', 'types', b'types']) -> None:
            ...

    class List(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TYPE_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int

        @property
        def type(self) -> global___Type:
            ...
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, type: typing.Optional[global___Type]=..., type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['type', b'type']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['nullability', b'nullability', 'type', b'type', 'type_variation_reference', b'type_variation_reference']) -> None:
            ...

    class Map(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        NULLABILITY_FIELD_NUMBER: builtins.int

        @property
        def key(self) -> global___Type:
            ...

        @property
        def value(self) -> global___Type:
            ...
        type_variation_reference: builtins.int = ...
        nullability: global___Type.Nullability.ValueType = ...

        def __init__(self, *, key: typing.Optional[global___Type]=..., value: typing.Optional[global___Type]=..., type_variation_reference: builtins.int=..., nullability: global___Type.Nullability.ValueType=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'nullability', b'nullability', 'type_variation_reference', b'type_variation_reference', 'value', b'value']) -> None:
            ...
    BOOL_FIELD_NUMBER: builtins.int
    I8_FIELD_NUMBER: builtins.int
    I16_FIELD_NUMBER: builtins.int
    I32_FIELD_NUMBER: builtins.int
    I64_FIELD_NUMBER: builtins.int
    FP32_FIELD_NUMBER: builtins.int
    FP64_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    BINARY_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    DATE_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    INTERVAL_YEAR_FIELD_NUMBER: builtins.int
    INTERVAL_DAY_FIELD_NUMBER: builtins.int
    TIMESTAMP_TZ_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    FIXED_CHAR_FIELD_NUMBER: builtins.int
    VARCHAR_FIELD_NUMBER: builtins.int
    FIXED_BINARY_FIELD_NUMBER: builtins.int
    DECIMAL_FIELD_NUMBER: builtins.int
    STRUCT_FIELD_NUMBER: builtins.int
    LIST_FIELD_NUMBER: builtins.int
    MAP_FIELD_NUMBER: builtins.int
    USER_DEFINED_TYPE_REFERENCE_FIELD_NUMBER: builtins.int

    @property
    def bool(self) -> global___Type.Boolean:
        ...

    @property
    def i8(self) -> global___Type.I8:
        ...

    @property
    def i16(self) -> global___Type.I16:
        ...

    @property
    def i32(self) -> global___Type.I32:
        ...

    @property
    def i64(self) -> global___Type.I64:
        ...

    @property
    def fp32(self) -> global___Type.FP32:
        ...

    @property
    def fp64(self) -> global___Type.FP64:
        ...

    @property
    def string(self) -> global___Type.String:
        ...

    @property
    def binary(self) -> global___Type.Binary:
        ...

    @property
    def timestamp(self) -> global___Type.Timestamp:
        ...

    @property
    def date(self) -> global___Type.Date:
        ...

    @property
    def time(self) -> global___Type.Time:
        ...

    @property
    def interval_year(self) -> global___Type.IntervalYear:
        ...

    @property
    def interval_day(self) -> global___Type.IntervalDay:
        ...

    @property
    def timestamp_tz(self) -> global___Type.TimestampTZ:
        ...

    @property
    def uuid(self) -> global___Type.UUID:
        ...

    @property
    def fixed_char(self) -> global___Type.FixedChar:
        ...

    @property
    def varchar(self) -> global___Type.VarChar:
        ...

    @property
    def fixed_binary(self) -> global___Type.FixedBinary:
        ...

    @property
    def decimal(self) -> global___Type.Decimal:
        ...

    @property
    def struct(self) -> global___Type.Struct:
        ...

    @property
    def list(self) -> global___Type.List:
        ...

    @property
    def map(self) -> global___Type.Map:
        ...
    user_defined_type_reference: builtins.int = ...

    def __init__(self, *, bool: typing.Optional[global___Type.Boolean]=..., i8: typing.Optional[global___Type.I8]=..., i16: typing.Optional[global___Type.I16]=..., i32: typing.Optional[global___Type.I32]=..., i64: typing.Optional[global___Type.I64]=..., fp32: typing.Optional[global___Type.FP32]=..., fp64: typing.Optional[global___Type.FP64]=..., string: typing.Optional[global___Type.String]=..., binary: typing.Optional[global___Type.Binary]=..., timestamp: typing.Optional[global___Type.Timestamp]=..., date: typing.Optional[global___Type.Date]=..., time: typing.Optional[global___Type.Time]=..., interval_year: typing.Optional[global___Type.IntervalYear]=..., interval_day: typing.Optional[global___Type.IntervalDay]=..., timestamp_tz: typing.Optional[global___Type.TimestampTZ]=..., uuid: typing.Optional[global___Type.UUID]=..., fixed_char: typing.Optional[global___Type.FixedChar]=..., varchar: typing.Optional[global___Type.VarChar]=..., fixed_binary: typing.Optional[global___Type.FixedBinary]=..., decimal: typing.Optional[global___Type.Decimal]=..., struct: typing.Optional[global___Type.Struct]=..., list: typing.Optional[global___Type.List]=..., map: typing.Optional[global___Type.Map]=..., user_defined_type_reference: builtins.int=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['binary', b'binary', 'bool', b'bool', 'date', b'date', 'decimal', b'decimal', 'fixed_binary', b'fixed_binary', 'fixed_char', b'fixed_char', 'fp32', b'fp32', 'fp64', b'fp64', 'i16', b'i16', 'i32', b'i32', 'i64', b'i64', 'i8', b'i8', 'interval_day', b'interval_day', 'interval_year', b'interval_year', 'kind', b'kind', 'list', b'list', 'map', b'map', 'string', b'string', 'struct', b'struct', 'time', b'time', 'timestamp', b'timestamp', 'timestamp_tz', b'timestamp_tz', 'user_defined_type_reference', b'user_defined_type_reference', 'uuid', b'uuid', 'varchar', b'varchar']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['binary', b'binary', 'bool', b'bool', 'date', b'date', 'decimal', b'decimal', 'fixed_binary', b'fixed_binary', 'fixed_char', b'fixed_char', 'fp32', b'fp32', 'fp64', b'fp64', 'i16', b'i16', 'i32', b'i32', 'i64', b'i64', 'i8', b'i8', 'interval_day', b'interval_day', 'interval_year', b'interval_year', 'kind', b'kind', 'list', b'list', 'map', b'map', 'string', b'string', 'struct', b'struct', 'time', b'time', 'timestamp', b'timestamp', 'timestamp_tz', b'timestamp_tz', 'user_defined_type_reference', b'user_defined_type_reference', 'uuid', b'uuid', 'varchar', b'varchar']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['kind', b'kind']) -> typing.Optional[typing_extensions.Literal['bool', 'i8', 'i16', 'i32', 'i64', 'fp32', 'fp64', 'string', 'binary', 'timestamp', 'date', 'time', 'interval_year', 'interval_day', 'timestamp_tz', 'uuid', 'fixed_char', 'varchar', 'fixed_binary', 'decimal', 'struct', 'list', 'map', 'user_defined_type_reference']]:
        ...
global___Type = Type

class NamedStruct(google.protobuf.message.Message):
    """A message for modeling name/type pairs.

    Useful for representing relation schemas.

    Notes:

    * The names field is in depth-first order.

    For example a schema such as:

    a: int64
    b: struct<c: float32, d: string>

    would have a `names` field that looks like:

    ["a", "b", "c", "d"]

    * Only struct fields are contained in this field's elements,
    * Map keys should be traversed first, then values when producing/consuming
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMES_FIELD_NUMBER: builtins.int
    STRUCT_FIELD_NUMBER: builtins.int

    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """list of names in dfs order"""
        pass

    @property
    def struct(self) -> global___Type.Struct:
        ...

    def __init__(self, *, names: typing.Optional[typing.Iterable[typing.Text]]=..., struct: typing.Optional[global___Type.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['struct', b'struct']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['names', b'names', 'struct', b'struct']) -> None:
        ...
global___NamedStruct = NamedStruct