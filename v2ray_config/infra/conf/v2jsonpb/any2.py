from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class anyresolverv2:
    background_resolver: Optional[AnyResolver] = field(default_factory=AnyResolver)
