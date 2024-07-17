from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.features.dns as dns


@dataclass(slots=True)
class record:
    a: Optional[IPRecord] = field(default_factory=IPRecord)
    aaaa: Optional[IPRecord] = field(default_factory=IPRecord)


@dataclass(slots=True)
class IPRecord:
    req_id: Optional[int] = None
    ip: Optional[list[str]] = field(default_factory=list[str])
    expire: Optional[Time] = field(default_factory=Time)
    r_code: Optional[RCode] = field(default_factory=RCode)


@dataclass(slots=True)
class dnsRequest:
    req_type: Optional[Type] = field(default_factory=Type)
    domain: Optional[str] = None
    start: Optional[Time] = field(default_factory=Time)
    expire: Optional[Time] = field(default_factory=Time)
    msg: Optional[Message] = field(default_factory=Message)
