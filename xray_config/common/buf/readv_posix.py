from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class posixReader:
    iovecs: Optional[list[Iovec]] = field(default_factory=list[Iovec])
