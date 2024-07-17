from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class ChannelConfig:
    blocking: Optional[bool] = None
    subscriber_limit: Optional[int] = None
    buffer_size: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
