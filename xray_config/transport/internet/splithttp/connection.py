from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class splitConn:
    writer: Optional[WriteCloser] = field(default_factory=WriteCloser)
    reader: Optional[ReadCloser] = field(default_factory=ReadCloser)
    remoteAddr: Optional[Addr] = field(default_factory=Addr)
    localAddr: Optional[Addr] = field(default_factory=Addr)
