from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class AddUserOperation:
    user: Optional[User] = field(default_factory=User)


@dataclass(slots=True)
class RemoveUserOperation:
    email: Optional[str] = None


@dataclass(slots=True)
class AddInboundRequest:
    inbound: Optional[InboundHandlerConfig] = field(default_factory=InboundHandlerConfig)


@dataclass(slots=True)
class AddInboundResponse:
    pass


@dataclass(slots=True)
class RemoveInboundRequest:
    tag: Optional[str] = None


@dataclass(slots=True)
class RemoveInboundResponse:
    pass


@dataclass(slots=True)
class AlterInboundRequest:
    tag: Optional[str] = None
    operation: Optional[Any] = field(default_factory=Any)


@dataclass(slots=True)
class AlterInboundResponse:
    pass


@dataclass(slots=True)
class AddOutboundRequest:
    outbound: Optional[OutboundHandlerConfig] = field(default_factory=OutboundHandlerConfig)


@dataclass(slots=True)
class AddOutboundResponse:
    pass


@dataclass(slots=True)
class RemoveOutboundRequest:
    tag: Optional[str] = None


@dataclass(slots=True)
class RemoveOutboundResponse:
    pass


@dataclass(slots=True)
class AlterOutboundRequest:
    tag: Optional[str] = None
    operation: Optional[Any] = field(default_factory=Any)


@dataclass(slots=True)
class AlterOutboundResponse:
    pass


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class x:
    pass
