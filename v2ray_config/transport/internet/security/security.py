from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net


@dataclass(slots=True)
class OptionWithALPN:
    alp_ns: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class OptionWithDestination:
    dest: Optional[Destination] = field(default_factory=Destination)
