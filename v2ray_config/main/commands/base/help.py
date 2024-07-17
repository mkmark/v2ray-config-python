from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class errWriter:
    w: Optional[Writer] = field(default_factory=Writer)
    err: Optional[error] = field(default_factory=error)


@dataclass(slots=True)
class tmplData(Command, CommandEnvHolder):
    pass
