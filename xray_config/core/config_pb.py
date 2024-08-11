from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.serial as serial
# import xray_config.transport.global as global


@dataclass(slots=True)
class Config:
    inbound: Optional[list[InboundHandlerConfig]] = field(
        default_factory=list[InboundHandlerConfig]
    )
    outbound: Optional[list[OutboundHandlerConfig]] = field(
        default_factory=list[OutboundHandlerConfig]
    )
    app: Optional[list[dict]] = field(default_factory=list[dict])
    transport: Optional[Config] = field(default_factory=Config)
    extension: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class InboundHandlerConfig:
    tag: Optional[str] = None
    receiver_settings: Optional[dict] = field(default_factory=dict)
    proxy_settings: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class OutboundHandlerConfig:
    tag: Optional[str] = None
    sender_settings: Optional[dict] = field(default_factory=dict)
    proxy_settings: Optional[dict] = field(default_factory=dict)
    expire: Optional[int] = None
    comment: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
