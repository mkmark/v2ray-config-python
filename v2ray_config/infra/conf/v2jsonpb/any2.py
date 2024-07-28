from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class anyresolverv2:
    backgroundResolver: Optional[AnyResolver] = field(default_factory=AnyResolver)
