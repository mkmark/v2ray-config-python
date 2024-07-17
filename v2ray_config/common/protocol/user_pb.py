from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class User:
    level: Optional[int] = None
    email: Optional[str] = None
    account: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class x:
    pass
