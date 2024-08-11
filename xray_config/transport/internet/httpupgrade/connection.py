from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class connection(Conn):
    remoteAddr: Optional[Addr] = field(default_factory=Addr)
