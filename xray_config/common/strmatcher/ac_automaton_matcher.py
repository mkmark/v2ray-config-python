from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class MatchType:
    matchType: Optional[Type] = field(default_factory=Type)
    exist: Optional[bool] = None


@dataclass(slots=True)
class Edge:
    edgeType: Optional[bool] = None
    nextNode: Optional[int] = None


@dataclass(slots=True)
class ACAutomaton:
    trie: Optional[list[[validCharCount]Edge]] = field(default_factory=list[[validCharCount]Edge])
    fail: Optional[list[int]] = field(default_factory=list[int])
    exists: Optional[list[MatchType]] = field(default_factory=list[MatchType])
    count: Optional[int] = None
