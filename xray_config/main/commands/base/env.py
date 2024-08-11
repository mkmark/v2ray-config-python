from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class CommandEnvHolder:
    exec: Optional[str] = None
    commandsWidth: Optional[int] = None
