from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.proxy.shadowsocks as shadowsocks


@dataclass(slots=True)
class ShadowsocksServerConfig:
    method: Optional[str] = None
    password: Optional[str] = None
    udp: Optional[bool] = None
    level: Optional[int] = None
    email: Optional[str] = None
    network: Optional[list[str]] = field(default_factory=list[str])
    iv_check: Optional[bool] = None


@dataclass(slots=True)
class ShadowsocksServerTarget:
    address: Optional[str] = None
    port: Optional[int] = None
    method: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    ota: Optional[bool] = None
    level: Optional[int] = None
    iv_check: Optional[bool] = None


@dataclass(slots=True)
class ShadowsocksClientConfig:
    servers: Optional[list[ShadowsocksServerTarget]] = field(default_factory=list[ShadowsocksServerTarget])
