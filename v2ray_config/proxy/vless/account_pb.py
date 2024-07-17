from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Account:
    id: Optional[str] = None
    flow: Optional[str] = None
    encryption: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
