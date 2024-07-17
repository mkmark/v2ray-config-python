from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.observatory as observatory
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class GetOutboundStatusRequest:
    tag: Optional[str] = None


@dataclass(slots=True)
class GetOutboundStatusResponse:
    status: Optional[ObservationResult] = field(default_factory=ObservationResult)


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class x:
    pass
