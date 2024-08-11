from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.app.policy.config_pb import Policy, SystemPolicy

# import xray_config.common as common
# import xray_config.features.policy as policy


@dataclass(slots=True)
class Instance:
    levels: Optional[dict[int, Policy]] = field(default_factory=dict[int, Policy])
    system: Optional[SystemPolicy] = field(default_factory=SystemPolicy)
