from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class ServerConfig:
    pass


@dataclass(slots=True)
class ClientConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    h1_skip_wait_for_reply: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
