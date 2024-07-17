from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class GunConn:
    service: Optional[GunService] = field(default_factory=GunService)
    reader: Optional[Reader] = field(default_factory=Reader)
    over: Optional[CancelFunc] = field(default_factory=CancelFunc)
    local: Optional[Addr] = field(default_factory=Addr)
    remote: Optional[Addr] = field(default_factory=Addr)
