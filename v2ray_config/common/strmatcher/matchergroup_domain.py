from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class trieNode:
    values: Optional[list[int]] = field(default_factory=list[int])
    children: Optional[dict[str, trieNode]] = field(default_factory=dict[str, trieNode])


@dataclass(slots=True)
class DomainMatcherGroup:
    root: Optional[trieNode] = field(default_factory=trieNode)
