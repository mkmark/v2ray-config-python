from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class Config:
    transport_settings: Optional[list[TransportConfig]] = field(default_factory=list[TransportConfig])


@dataclass(slots=True)
class x:
    pass
