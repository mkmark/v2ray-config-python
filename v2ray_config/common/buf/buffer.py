from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.bytespool as bytespool


@dataclass(slots=True)
class ownership(int):
    pass


@dataclass(slots=True)
class Buffer:
    v: Optional[list[int]] = field(default_factory=list[int])
    start: Optional[int] = None
    end: Optional[int] = None
    ownership: Optional[ownership] = field(default_factory=ownership)
