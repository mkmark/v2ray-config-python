from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.dns as dns
# import xray_config.app.router as router
# import xray_config.common.errors as errors
# import xray_config.common.net as net


@dataclass(slots=True)
class NameServerConfig:
    address: Optional[str] = None
    clientIP: Optional[str] = None
    port: Optional[int] = None
    skipFallback: Optional[bool] = None
    domains: Optional[list[str]] = field(default_factory=list[str])
    expectIPs: Optional[list[str]] = field(default_factory=list[str])
    queryStrategy: Optional[str] = None


@dataclass(slots=True)
class HostAddress:
    addr: Optional[str] = None
    addrs: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class HostsWrapper:
    hosts: Optional[dict[str, HostAddress]] = field(
        default_factory=dict[str, HostAddress]
    )


@dataclass(slots=True)
class DNSConfig:
    servers: Optional[list[NameServerConfig]] = field(
        default_factory=list[NameServerConfig]
    )
    hosts: Optional[HostsWrapper] = field(default_factory=HostsWrapper)
    clientIp: Optional[str] = None
    tag: Optional[str] = None
    queryStrategy: Optional[str] = None
    disableCache: Optional[bool] = None
    disableFallback: Optional[bool] = None
    disableFallbackIfMatch: Optional[bool] = None
