from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class windowsReader:
    bufs: Optional[list[WSABuf]] = field(default_factory=list[WSABuf])
