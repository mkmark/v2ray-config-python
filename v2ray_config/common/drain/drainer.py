from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.dice as dice


@dataclass(slots=True)
class BehaviorSeedLimitedDrainer:
    drain_size: Optional[int] = None


@dataclass(slots=True)
class NopDrainer:
    pass
