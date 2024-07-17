from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class jsonDocument(dict[str, dict]):
    pass


@dataclass(slots=True)
class AbstractNonNativeLink:
    values: Optional[dict[str, str]] = field(default_factory=dict[str, str])
