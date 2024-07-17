from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class FullMatcher(str):
    pass


@dataclass(slots=True)
class DomainMatcher(str):
    pass


@dataclass(slots=True)
class SubstrMatcher(str):
    pass


@dataclass(slots=True)
class RegexMatcher:
    pattern: Optional[Regexp] = field(default_factory=Regexp)
