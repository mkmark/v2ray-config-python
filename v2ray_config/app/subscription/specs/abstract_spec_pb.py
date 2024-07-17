from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class ServerConfiguration:
    protocol: Optional[str] = None
    protocol_settings: Optional[Any] = field(default_factory=Any)
    transport: Optional[int] = None
    transport_settings: Optional[Any] = field(default_factory=Any)
    security: Optional[str] = None
    security_settings: Optional[Any] = field(default_factory=Any)


@dataclass(slots=True)
class SubscriptionServerConfig:
    id: Optional[str] = None
    metadata: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    configuration: Optional[ServerConfiguration] = field(
        default_factory=ServerConfiguration
    )


@dataclass(slots=True)
class SubscriptionDocument:
    metadata: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    server: Optional[list[SubscriptionServerConfig]] = field(
        default_factory=list[SubscriptionServerConfig]
    )


@dataclass(slots=True)
class x:
    pass
