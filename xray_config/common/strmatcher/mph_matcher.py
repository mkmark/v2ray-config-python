from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class bySize(list[indexBucket]):
    pass


@dataclass(slots=True)
class MphMatcherGroup:
    ac: Optional[ACAutomaton] = field(default_factory=ACAutomaton)
    otherMatchers: Optional[list[matcherEntry]] = field(default_factory=list[matcherEntry])
    rules: Optional[list[str]] = field(default_factory=list[str])
    level0: Optional[list[int]] = field(default_factory=list[int])
    level0Mask: Optional[int] = None
    level1: Optional[list[int]] = field(default_factory=list[int])
    level1Mask: Optional[int] = None
    count: Optional[int] = None
    ruleMap: Optional[dict[str, int]] = field(default_factory=dict[str, int])


@dataclass(slots=True)
class indexBucket:
    n: Optional[int] = None
    vals: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class stringStruct:
    str: Optional[Pointer] = field(default_factory=Pointer)
    len: Optional[int] = None
