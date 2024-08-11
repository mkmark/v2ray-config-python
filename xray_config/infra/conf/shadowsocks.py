from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial
# import xray_config.proxy.shadowsocks as shadowsocks
# import xray_config.proxy.shadowsocks_2022 as shadowsocks_2022


@dataclass(slots=True)
class ShadowsocksUserConfig:
    method: Optional[str] = None
    password: Optional[str] = None
    level: Optional[int] = None
    email: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None


@dataclass(slots=True)
class ShadowsocksServerConfig:
    method: Optional[str] = None
    password: Optional[str] = None
    level: Optional[int] = None
    email: Optional[str] = None
    clients: Optional[list[ShadowsocksUserConfig]] = field(default_factory=list[ShadowsocksUserConfig])
    network: Optional[list[str]] = field(default_factory=list[str])
    ivCheck: Optional[bool] = None


@dataclass(slots=True)
class ShadowsocksServerTarget:
    address: Optional[str] = None
    port: Optional[int] = None
    method: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    level: Optional[int] = None
    ivCheck: Optional[bool] = None
    uot: Optional[bool] = None
    uotVersion: Optional[int] = None


@dataclass(slots=True)
class ShadowsocksClientConfig:
    servers: Optional[list[ShadowsocksServerTarget]] = field(default_factory=list[ShadowsocksServerTarget])
