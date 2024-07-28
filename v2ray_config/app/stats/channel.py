from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common


@dataclass(slots=True)
class Channel:
    channel: Optional[chan] = field(default_factory=chan)
    subscribers: Optional[list[chan]] = field(default_factory=list[chan])
    access: Optional[RWMutex] = field(default_factory=RWMutex)
    closed: Optional[chan] = field(default_factory=chan)
    blocking: Optional[bool] = None
    bufferSize: Optional[int] = None
    subsLimit: Optional[int] = None


@dataclass(slots=True)
class channelMessage:
    context: Optional[Context] = field(default_factory=Context)
    message: Optional[dict] = field(default_factory=dict)
