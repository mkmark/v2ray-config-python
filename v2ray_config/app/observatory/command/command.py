from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.observatory as observatory
# import v2ray_config.common as common
# import v2ray_config.features as features
# import v2ray_config.features.extension as extension


@dataclass(slots=True)
class service(UnimplementedObservatoryServiceServer):
    v: Optional[Instance] = field(default_factory=Instance)
    observatory: Optional[Observatory] = field(default_factory=Observatory)
