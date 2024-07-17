from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf


@dataclass(slots=True)
class NoOpReader:
    pass


@dataclass(slots=True)
class NoOpWriter:
    pass


@dataclass(slots=True)
class HeaderReader:
    req: Optional[Request] = field(default_factory=Request)
    expected_header: Optional[RequestConfig] = field(default_factory=RequestConfig)


@dataclass(slots=True)
class HeaderWriter:
    header: Optional[Buffer] = field(default_factory=Buffer)


@dataclass(slots=True)
class Conn(Conn):
    read_buffer: Optional[Buffer] = field(default_factory=Buffer)
    one_time_reader: Optional[Reader] = field(default_factory=Reader)
    one_time_writer: Optional[Writer] = field(default_factory=Writer)
    error_writer: Optional[Writer] = field(default_factory=Writer)
    error_mismatch_writer: Optional[Writer] = field(default_factory=Writer)
    error_too_long_writer: Optional[Writer] = field(default_factory=Writer)
    err_reason: Optional[error] = field(default_factory=error)


@dataclass(slots=True)
class Authenticator:
    config: Optional[Config] = field(default_factory=Config)
