from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# from v2ray_config.common.net.address_pb import IPOrDomain
from v2ray_config.common.protocol.user_pb import User

# import v2ray_config.common.net as net


@dataclass(slots=True)
class ServerEndpoint:
    address: Optional[str] = None
    port: Optional[int] = None
    user: Optional[list[User]] = field(default_factory=list[User])


@dataclass(slots=True)
class x:
    pass
