from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class node:
    values: Optional[list[int]] = field(default_factory=list[int])
    sub: Optional[dict[str, node]] = field(default_factory=dict[str, node])


@dataclass(slots=True)
class DomainMatcherGroup:
    root: Optional[node] = field(default_factory=node)
