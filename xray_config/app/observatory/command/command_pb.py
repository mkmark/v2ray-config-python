from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.observatory as observatory


@dataclass(slots=True)
class GetOutboundStatusRequest:
    pass


@dataclass(slots=True)
class GetOutboundStatusResponse:
    status: Optional[ObservationResult] = field(default_factory=ObservationResult)


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class x:
    pass
