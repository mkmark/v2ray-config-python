from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.proxy.socks as socks


@dataclass(slots=True)
class SocksAccount:
    user: Optional[str] = None
    pass_: Optional[str] = None


@dataclass(slots=True)
class SocksServerConfig:
    auth: Optional[str] = None
    accounts: Optional[list[SocksAccount]] = field(default_factory=list[SocksAccount])
    udp: Optional[bool] = None
    ip: Optional[str] = None
    timeout: Optional[int] = None
    userLevel: Optional[int] = None


@dataclass(slots=True)
class SocksRemoteConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    users: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class SocksClientConfig:
    servers: Optional[list[SocksRemoteConfig]] = field(default_factory=list[SocksRemoteConfig])
    version: Optional[str] = None
