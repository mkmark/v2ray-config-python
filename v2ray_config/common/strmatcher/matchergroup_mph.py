from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class mphRuleInfo:
    rolling_hash: Optional[int] = None
    matchers: Optional[[mphMatchTypeCount][]uint32] = field(default_factory=[mphMatchTypeCount][]uint32)


@dataclass(slots=True)
class MphMatcherGroup:
    rules: Optional[list[str]] = field(default_factory=list[str])
    values: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    level_0: Optional[list[int]] = field(default_factory=list[int])
    level_0_mask: Optional[int] = None
    level_1: Optional[list[int]] = field(default_factory=list[int])
    level_1_mask: Optional[int] = None
    rule_infos: Optional[dict[str, mphRuleInfo]] = field(default_factory=dict[str, mphRuleInfo])
