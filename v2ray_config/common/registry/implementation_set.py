from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class CustomLoader(Message, error)):
    pass


@dataclass(slots=True)
class implementationSet:
    aliasLookup: Optional[dict[str, implementation]] = field(default_factory=dict[str, implementation])


@dataclass(slots=True)
class implementation:
    fullName: Optional[str] = None
    alias: Optional[list[str]] = field(default_factory=list[str])
    loader: Optional[CustomLoader] = field(default_factory=CustomLoader)
