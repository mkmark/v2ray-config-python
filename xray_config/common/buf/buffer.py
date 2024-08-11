from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.bytespool as bytespool
# import xray_config.common.errors as errors
# import xray_config.common.net as net


@dataclass(slots=True)
class Buffer:
    v: Optional[list[int]] = field(default_factory=list[int])
    start: Optional[int] = None
    end: Optional[int] = None
    unmanaged: Optional[bool] = None
    uDP: Optional[Destination] = field(default_factory=Destination)
