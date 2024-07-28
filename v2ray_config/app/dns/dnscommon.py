from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.features.dns as dns


@dataclass(slots=True)
class record:
    a: Optional[IPRecord] = field(default_factory=IPRecord)
    aAAA: Optional[IPRecord] = field(default_factory=IPRecord)


@dataclass(slots=True)
class IPRecord:
    reqID: Optional[int] = None
    iP: Optional[list[str]] = field(default_factory=list[str])
    expire: Optional[Time] = field(default_factory=Time)
    rCode: Optional[RCode] = field(default_factory=RCode)


@dataclass(slots=True)
class dnsRequest:
    reqType: Optional[Type] = field(default_factory=Type)
    domain: Optional[str] = None
    start: Optional[Time] = field(default_factory=Time)
    expire: Optional[Time] = field(default_factory=Time)
    msg: Optional[Message] = field(default_factory=Message)
