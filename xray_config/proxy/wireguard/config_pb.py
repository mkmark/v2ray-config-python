from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class DeviceConfig_DomainStrategy(int):
    pass


@dataclass(slots=True)
class PeerConfig:
    public_key: Optional[str] = None
    pre_shared_key: Optional[str] = None
    endpoint: Optional[str] = None
    keep_alive: Optional[int] = None
    allowed_ips: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class DeviceConfig:
    secret_key: Optional[str] = None
    endpoint: Optional[list[str]] = field(default_factory=list[str])
    peers: Optional[list[PeerConfig]] = field(default_factory=list[PeerConfig])
    mtu: Optional[int] = None
    num_workers: Optional[int] = None
    reserved: Optional[list[int]] = field(default_factory=list[int])
    domain_strategy: Optional[DeviceConfig_DomainStrategy] = field(default_factory=DeviceConfig_DomainStrategy)
    is_client: Optional[bool] = None
    kernel_mode: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
