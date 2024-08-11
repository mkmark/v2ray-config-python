from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Severity(int):
    pass


@dataclass(slots=True)
class x:
    pass
