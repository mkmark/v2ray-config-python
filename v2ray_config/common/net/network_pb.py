from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Network(int):
    pass


@dataclass(slots=True)
class NetworkList:
    network: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class x:
    pass
