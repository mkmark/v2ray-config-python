from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class MessageOpt:
    type: Optional[list[str]] = field(default_factory=list[str])
    short_name: Optional[list[str]] = field(default_factory=list[str])
    transport_original_name: Optional[str] = None
    allow_restricted_mode_load: Optional[bool] = None


@dataclass(slots=True)
class FieldOpt:
    any_wants: Optional[list[str]] = field(default_factory=list[str])
    allowed_values: Optional[list[str]] = field(default_factory=list[str])
    allowed_value_types: Optional[list[str]] = field(default_factory=list[str])
    convert_time_read_file_into: Optional[str] = None
    forbidden: Optional[bool] = None
    convert_time_resource_loading: Optional[str] = None
    convert_time_parse_ip: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
