from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class ClientConfig:
    method: Optional[str] = None
    psk: Optional[list[int]] = field(default_factory=list[int])
    ipsk: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    address: Optional[str] = None
    port: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
