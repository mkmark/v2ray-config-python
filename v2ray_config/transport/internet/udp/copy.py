from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.signal as signal
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class dataHandler(Addr)):
    pass


@dataclass(slots=True)
class CopyOption(func(*copyHandler)):
    pass


@dataclass(slots=True)
class copyHandler:
    onData: Optional[list[dataHandler]] = field(default_factory=list[dataHandler])
