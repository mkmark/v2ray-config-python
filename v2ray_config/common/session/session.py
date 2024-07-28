from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class ID(int):
    pass


@dataclass(slots=True)
class Inbound:
    source: Optional[Destination] = field(default_factory=Destination)
    gateway: Optional[Destination] = field(default_factory=Destination)
    tag: Optional[str] = None
    user: Optional[MemoryUser] = field(default_factory=MemoryUser)


@dataclass(slots=True)
class Outbound:
    target: Optional[Destination] = field(default_factory=Destination)
    gateway: Optional[str] = None


@dataclass(slots=True)
class SniffingRequest:
    overrideDestinationForProtocol: Optional[list[str]] = field(default_factory=list[str])
    enabled: Optional[bool] = None
    metadataOnly: Optional[bool] = None


@dataclass(slots=True)
class Content:
    protocol: Optional[str] = None
    sniffingRequest: Optional[SniffingRequest] = field(default_factory=SniffingRequest)
    attributes: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    skipDNSResolve: Optional[bool] = None


@dataclass(slots=True)
class Sockopt:
    mark: Optional[int] = None
