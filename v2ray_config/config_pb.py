from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport as transport


@dataclass(slots=True)
class Config:
    inbound: Optional[list[InboundHandlerConfig]] = field(default_factory=list[InboundHandlerConfig])
    outbound: Optional[list[OutboundHandlerConfig]] = field(default_factory=list[OutboundHandlerConfig])
    app: Optional[list[Any]] = field(default_factory=list[Any])
    transport: Optional[Config] = field(default_factory=Config)
    extension: Optional[list[Any]] = field(default_factory=list[Any])


@dataclass(slots=True)
class InboundHandlerConfig:
    tag: Optional[str] = None
    receiver_settings: Optional[Any] = field(default_factory=Any)
    proxy_settings: Optional[Any] = field(default_factory=Any)


@dataclass(slots=True)
class OutboundHandlerConfig:
    tag: Optional[str] = None
    sender_settings: Optional[Any] = field(default_factory=Any)
    proxy_settings: Optional[Any] = field(default_factory=Any)
    expire: Optional[int] = None
    comment: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
