from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net


@dataclass(slots=True)
class ServerConfig:
    method: Optional[str] = None
    key: Optional[str] = None
    email: Optional[str] = None
    level: Optional[int] = None
    network: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class MultiUserServerConfig:
    method: Optional[str] = None
    key: Optional[str] = None
    users: Optional[list[User]] = field(default_factory=list[User])
    network: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class RelayDestination:
    key: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None
    email: Optional[str] = None
    level: Optional[int] = None


@dataclass(slots=True)
class RelayServerConfig:
    method: Optional[str] = None
    key: Optional[str] = None
    destinations: Optional[list[RelayDestination]] = field(default_factory=list[RelayDestination])
    network: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class User:
    key: Optional[str] = None
    email: Optional[str] = None
    level: Optional[int] = None


@dataclass(slots=True)
class ClientConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    method: Optional[str] = None
    key: Optional[str] = None
    udp_over_tcp: Optional[bool] = None
    udp_over_tcp_version: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
