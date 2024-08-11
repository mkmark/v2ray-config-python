from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.session as session
# import xray_config.common.ctx as ctx
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.signal as signal


@dataclass(slots=True)
class Inbound:
    source: Optional[Destination] = field(default_factory=Destination)
    gateway: Optional[Destination] = field(default_factory=Destination)
    tag: Optional[str] = None
    name: Optional[str] = None
    user: Optional[MemoryUser] = field(default_factory=MemoryUser)
    conn: Optional[Conn] = field(default_factory=Conn)
    timer: Optional[ActivityTimer] = field(default_factory=ActivityTimer)
    canSpliceCopy: Optional[int] = None


@dataclass(slots=True)
class Outbound:
    originalTarget: Optional[Destination] = field(default_factory=Destination)
    target: Optional[Destination] = field(default_factory=Destination)
    routeTarget: Optional[Destination] = field(default_factory=Destination)
    gateway: Optional[str] = None
    tag: Optional[str] = None
    name: Optional[str] = None
    conn: Optional[Conn] = field(default_factory=Conn)
    canSpliceCopy: Optional[int] = None


@dataclass(slots=True)
class SniffingRequest:
    excludeForDomain: Optional[list[str]] = field(default_factory=list[str])
    overrideDestinationForProtocol: Optional[list[str]] = field(default_factory=list[str])
    enabled: Optional[bool] = None
    metadataOnly: Optional[bool] = None
    routeOnly: Optional[bool] = None


@dataclass(slots=True)
class Content:
    protocol: Optional[str] = None
    sniffingRequest: Optional[SniffingRequest] = field(default_factory=SniffingRequest)
    attributes: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    skipDNSResolve: Optional[bool] = None


@dataclass(slots=True)
class Sockopt:
    mark: Optional[int] = None
