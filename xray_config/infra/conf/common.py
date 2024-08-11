from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.platform as platform
# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class StringList(list[str]):
    pass


@dataclass(slots=True)
class Network(str):
    pass


@dataclass(slots=True)
class NetworkList(list[str]):
    pass


@dataclass(slots=True)
class Address(str):
    pass


@dataclass(slots=True)
class PortRange:
    from_: Optional[int] = None
    to: Optional[int] = None


@dataclass(slots=True)
class PortList:
    range: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class User:
    email: Optional[str] = None
    level: Optional[int] = None


@dataclass(slots=True)
class Int32Range:
    from_: Optional[int] = None
    to: Optional[int] = None
