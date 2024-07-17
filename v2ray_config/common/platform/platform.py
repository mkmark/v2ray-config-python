from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class EnvFlag:
    name: Optional[str] = None
    alt_name: Optional[str] = None
