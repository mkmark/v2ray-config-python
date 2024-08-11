from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors


@dataclass(slots=True)
class NoOpReader:
    pass


@dataclass(slots=True)
class NoOpWriter:
    pass


@dataclass(slots=True)
class HeaderReader:
    req: Optional[Request] = field(default_factory=Request)
    expectedHeader: Optional[RequestConfig] = field(default_factory=RequestConfig)


@dataclass(slots=True)
class HeaderWriter:
    header: Optional[Buffer] = field(default_factory=Buffer)


@dataclass(slots=True)
class Conn(Conn):
    readBuffer: Optional[Buffer] = field(default_factory=Buffer)
    oneTimeReader: Optional[Reader] = field(default_factory=Reader)
    oneTimeWriter: Optional[Writer] = field(default_factory=Writer)
    errorWriter: Optional[Writer] = field(default_factory=Writer)
    errorMismatchWriter: Optional[Writer] = field(default_factory=Writer)
    errorTooLongWriter: Optional[Writer] = field(default_factory=Writer)
    errReason: Optional[error] = field(default_factory=error)


@dataclass(slots=True)
class Authenticator:
    config: Optional[Config] = field(default_factory=Config)
