from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.subscription.entries.nonnative as nonnative
# import v2ray_config.main.commands.base as base


@dataclass(slots=True)
class orderedValueContainer(list[valueContainer]):
    pass


@dataclass(slots=True)
class valueContainer:
    key,: Optional[value] = field(default_factory=value)
