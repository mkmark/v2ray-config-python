from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.infra.conf.common import User

# import xray_config.common.net as net


@dataclass(slots=True)
class ServerEndpoint:
    address: Optional[str] = None
    port: Optional[int] = None
    user: Optional[list[User]] = field(default_factory=list[User])


@dataclass(slots=True)
class x:
    pass
