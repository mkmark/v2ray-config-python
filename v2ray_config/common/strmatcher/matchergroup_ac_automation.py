from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class acEdge(int):
    pass


@dataclass(slots=True)
class acValue([acMatchTypeCount][]uint32 // MatcherType -> Registered Matcher Values):
    pass


@dataclass(slots=True)
class acNode:
    next: Optional[[acValidCharCount]uint32] = field(default_factory=[acValidCharCount]uint32)
    edge: Optional[[acValidCharCount]acEdge] = field(default_factory=[acValidCharCount]acEdge)
    fail: Optional[int] = None
    match: Optional[int] = None


@dataclass(slots=True)
class ACAutomatonMatcherGroup:
    nodes: Optional[list[acNode]] = field(default_factory=list[acNode])
    values: Optional[list[acValue]] = field(default_factory=list[acValue])
