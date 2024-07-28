from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class UnparsedServerConf:
    kindHint: Optional[str] = None
    content: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class Container:
    kind: Optional[str] = None
    metadata: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    serverSpecs: Optional[list[UnparsedServerConf]] = field(default_factory=list[UnparsedServerConf])
