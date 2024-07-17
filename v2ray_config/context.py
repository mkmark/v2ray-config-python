from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class v2rayKeyType(int):
    pass


@dataclass(slots=True)
class temporaryValueDelegationFix(Context):
    value: Optional[Context] = field(default_factory=Context)
