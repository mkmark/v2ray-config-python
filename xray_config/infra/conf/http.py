from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial
# import xray_config.proxy.http as http


@dataclass(slots=True)
class HTTPAccount:
    user: Optional[str] = None
    pass_: Optional[str] = None


@dataclass(slots=True)
class HTTPServerConfig:
    timeout: Optional[int] = None
    accounts: Optional[list[HTTPAccount]] = field(default_factory=list[HTTPAccount])
    allowTransparent: Optional[bool] = None
    userLevel: Optional[int] = None


@dataclass(slots=True)
class HTTPRemoteConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    users: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class HTTPClientConfig:
    servers: Optional[list[HTTPRemoteConfig]] = field(default_factory=list[HTTPRemoteConfig])
    headers: Optional[dict[str, str]] = field(default_factory=dict[str, str])
