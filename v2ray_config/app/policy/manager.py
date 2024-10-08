from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.app.policy.config_pb import Policy, SystemPolicy

# import v2ray_config.common as common
# import v2ray_config.features.policy as policy


@dataclass(slots=True)
class Instance:
    levels: Optional[dict[int, Policy]] = field(default_factory=dict[int, Policy])
    system: Optional[SystemPolicy] = field(default_factory=SystemPolicy)
