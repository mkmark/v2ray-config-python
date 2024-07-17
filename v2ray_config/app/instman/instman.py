from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.features.extension as extension


@dataclass(slots=True)
class InstanceMgr:
    config: Optional[Config] = field(default_factory=Config)
    instances: Optional[dict[str, Instance]] = field(default_factory=dict[str, Instance])
