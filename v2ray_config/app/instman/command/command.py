from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.features.extension as extension


@dataclass(slots=True)
class service(UnimplementedInstanceManagementServiceServer):
    instman: Optional[InstanceManagement] = field(default_factory=InstanceManagement)
