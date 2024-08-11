from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.proxy.wireguard as wireguard


@dataclass(slots=True)
class WireGuardPeerConfig:
    publicKey: Optional[str] = None
    preSharedKey: Optional[str] = None
    endpoint: Optional[str] = None
    keepAlive: Optional[int] = None
    allowedIPs: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class WireGuardConfig:
    kernelMode: Optional[bool] = None
    secretKey: Optional[str] = None
    address: Optional[list[str]] = field(default_factory=list[str])
    peers: Optional[list[WireGuardPeerConfig]] = field(default_factory=list[WireGuardPeerConfig])
    mtu: Optional[int] = None
    workers: Optional[int] = None
    reserved: Optional[list[int]] = field(default_factory=list[int])
    domainStrategy: Optional[str] = None
