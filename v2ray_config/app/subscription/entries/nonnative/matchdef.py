from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class DefMatcher:
    templates: Optional[Template] = field(default_factory=Template)


@dataclass(slots=True)
class ExecutionEnvironment:
    link: Optional[AbstractNonNativeLink] = field(default_factory=AbstractNonNativeLink)
