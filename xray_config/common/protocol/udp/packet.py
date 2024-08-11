from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.net as net


@dataclass(slots=True)
class Packet:
    payload: Optional[Buffer] = field(default_factory=Buffer)
    source: Optional[Destination] = field(default_factory=Destination)
    target: Optional[Destination] = field(default_factory=Destination)
