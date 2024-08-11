from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class SessionKey(int):
    pass


@dataclass(slots=True)
class ID(int):
    pass
