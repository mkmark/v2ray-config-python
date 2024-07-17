from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.proxy.http as http


@dataclass(slots=True)
class HTTPAccount:
    user: Optional[str] = None
    pass_: Optional[str] = None


@dataclass(slots=True)
class HTTPServerConfig:
    timeout: Optional[int] = None
    accounts: Optional[list[HTTPAccount]] = field(default_factory=list[HTTPAccount])
    allow_transparent: Optional[bool] = None
    user_level: Optional[int] = None


@dataclass(slots=True)
class HTTPRemoteConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    users: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class HTTPClientConfig:
    servers: Optional[list[HTTPRemoteConfig]] = field(default_factory=list[HTTPRemoteConfig])
